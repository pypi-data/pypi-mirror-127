#distutils: language = c++
#cython: language_level=3, boundscheck=False, wraparound=False

#   --------------------------------------------------------------------
#   Pyfhel.pyx
#   Author: Alberto Ibarrondo
#   Date: 24/08/2021
#   --------------------------------------------------------------------
#   License: GNU GPL v3
#
#   Pyfhel is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Pyfhel is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   --------------------------------------------------------------------

# -------------------------------- IMPORTS ------------------------------------
from warnings import warn

# Both numpy and the Cython declarations for numpy
import numpy as np
np.import_array()

# Type checking for only numeric values
from numbers import Number, Real

# Dereferencing pointers in Cython in a secure way
from cython.operator cimport dereference as deref

# Importing it for the fused types
cimport cython

# Define Plaintext types
FLOAT_T = (float, np.float16, np.float32, np.float64)
INT_T =   (int, np.int16, np.int32, np.int64, np.int_, np.intc)

# Import utility functions
include "util/utils.pxi"
include "util/type_converters.pxi"

# ------------------------- PYTHON IMPLEMENTATION -----------------------------
cdef class Pyfhel:
    """Context class encapsulating most of the Homomorphic Encryption functionalities.

    Encrypted addition, multiplication, substraction, exponentiation of 
    integers/doubles. Implementation of homomorphic encryption using 
    SEAL/PALISADE as backend. Pyfhel works with PyPtxt as plaintext class
    and PyCtxt as cyphertext class.
    """
    def __cinit__(self,
                  context_params=None,
                  key_gen=False,
                  pub_key_file=None,
                  sec_key_file=None):
        self.afseal = new Afseal()
        self._qs = []
        self._scale = 0
    
    def __init__(self,
                  context_params=None,
                  key_gen=False,
                  pub_key_file=None,
                  sec_key_file=None):
        """Initializes an empty Pyfhel object, the base for all operations.
        
        To fill the Pyfhel object during initialization you can:
            - Provide a dictionary of context parameters to run Pyfhel.contextGen(**context_params). 
            - Set key_gen to True in order to generate a new public/secret key pair.
            - Provide a pub_key_file and/or sec_key_file to load existing keys from saved files.

        Attributes:
            context_params (dict, optional): dictionary of context parameters to run contextGen().
            key_gen (bool, optional): generate a new public/secret key pair
            pub_key_file (str, pathlib.Path, optional): Load public key from this file.
            sec_key_file (str, pathlib.Path, optional): Load public key from this file.
        """
        if context_params is not None:
            self.contextGen(**context_params)
        if key_gen: # Overrides the key files
            self.keyGen()
        else:
            if pub_key_file is not None:
                self.load_public_key(pub_key_file)
            if sec_key_file is not None:
                self.load_secret_key(sec_key_file)

    def __dealloc__(self):
        if self.afseal != NULL:
            del self.afseal
    
    def __iter__(self):
        return self

    def __repr__(self):
        """A printable string with all the information about the Pyfhel object
        
        Info:
            * at: hex ID, unique identifier and memory location.
            * pk: 'Y' if public key is present. '-' otherwise.
            * sk: 'Y' if secret key is present. '-' otherwise.
            * rtk: 'Y' if rotation keys are present. '-' otherwise.
            * rlk: 'Y' if relinarization keys are present. '-' otherwise.
            * contx: Context, with values of p, m, base, security,
                        # of int and frac digits and wether flagBatching is enabled.
        """
        return "<{} Pyfhel obj at {}, [pk:{}, sk:{}, rtk:{}, rlk:{}, contx({})]>".format(
                self.scheme.name,
                hex(id(self)),
                "-" if self.is_public_key_empty() else "Y",
                "-" if self.is_secret_key_empty() else "Y",
                "-" if self.is_rotate_key_empty() else "Y",
                "-" if self.is_relin_key_empty() else f"Y",
                "-" if self.is_context_empty() else \
                        f"n={self.n}, "\
                        f"p={self.p}, "\
                        f"sec={self.sec}, "\
                        f"qs={self.qs}, "\
                        f"scale={self.scale}, ")

    def __reduce__(self):
        """Required for pickling purposes. Returns a tuple with:
            - A callable object that will be called to create the initial version of the object.
            - A tuple of arguments for the callable object.
        """
        context_params={"scheme": self.scheme,
                        "plain_modulus": self.plain_modulus,
                        "poly_modulus_degree": self.poly_modulus_degree,
                        "sec": self.sec}
        return (Pyfhel, (context_params, False, None, None))

    @property
    def p(self):
        """p, plaintext modulus."""
        return self.get_plain_modulus()

    @property
    def n(self):
        """n, Polynomial coefficient modulus. (1*x^m+1). 
                
        Directly linked to the multiplication depth and the number of slots (bfv)."""
        return self.get_poly_modulus_degree()
    
    @property
    def sec(self):
        """Security (bits). Sets an appropriate coefficient modulus (q). Only applies to BFV scheme."""
        return (<Afseal*>self.afseal).get_sec()

    @property
    def qs(self):
        """Chain of prime sizes (bits). Sets size of each prime in the coefficient modulis (q). Only applies to CKKS scheme."""
        return self._qs

    @property
    def scale(self):
        """Upscale factor for fixed-point values. Only applies to CKKS scheme."""
        return self._scale
    @scale.setter
    def scale(self, value):
        if not isinstance(value, Real) or value < 0:
            raise ValueError("scale must be a positive number")
        self._scale = value
       
    @property
    def scheme(self):
        """Scheme of the current context."""
        return Scheme_t(self.afseal.get_scheme())

    @property
    def total_coeff_modulus_bit_count(self):
        """Scheme of the current context."""
        return (<Afseal*>self.afseal).total_coeff_modulus_bit_count()
    # =========================================================================
    # ============================ CRYPTOGRAPHY ===============================
    # =========================================================================
    # ....................... CONTEXT & KEY GENERATION ........................
    
    cpdef void contextGen(self,
        str scheme, int n, int p_bits=0, int p=0, int sec=128,
        double scale=0, int scale_bits=0, vector[int] qs = {}):
        """Generates Homomorphic Encryption context based on parameters.
        
        Creates a HE context based in parameters, as well as an appropriate
        encoder according to the scheme choice. The HE context contains the
        "public parameters" of the scheme, required for all operations
        (encryption/decryption,scheme/decoding, operations).
        
        *BFV scheme*: vectorized integer operations in Single Instruction Multiple
            Data (SIMD) fashion. The scheme requires a plain_modulus p prime, with
            p-1 being multiple of 2*n (n is the polynomial modulus degree). This 
            p is generated automatically with size p_bits, and it will serve as
            plaintext modulo, the maximum value of all freshly encrypted plaintexts.
            The coefficient modulus (q) is chosen under the hood with the security
            level sec, based on homomorphicencryption.org.
        
        *CKKS scheme*: vectorized approximate fixed point operations in SIMD. The
            underlying coefficient modulus (q) is set with a chain of prime sizes
            qs, which is a vector of integers.

        Args:
            scheme (str): HE scheme ("bfv" or "ckks", for integer or float ops).
            n (int): Polynomial coefficient modulus m. (Poly: 1*x^n+1), directly
                     linked to the multiplication depth, (SEAL's poly_modulus_degree)
                     and equal to the number of slots (nSlots) in bfv.
            -- Only for BFV scheme --
            p(int, optional):  Only for bfv. Plaintext modulus. 
            p_bits (int, optional):  Only for bfv. Plaintext modulus bit size. Overrides p.
            sec (int, optional): Only for bfv. Security level equivalent in AES.
                128, 192 or 256. More means more security but also more costly. Sets q.
            -- Only for CKKS scheme --
            scale (int, optional): Upscale factor for fixed-point values. 
            qs (list of ints, optional): Chain of prime sizes (#bits), to set q.
                      
        Return:
            None
        """
        s = to_Scheme_t(scheme)
        if s==Scheme_t.bfv:
            assert (p_bits>0 or p>0), "BFV scheme requires p_bits > 0 or p > 0"
            assert sec>0, "BFV scheme requires a security level (sec) to be set."
            self._scale = 0
            self._qs = {}
        elif s==Scheme_t.ckks:
            assert not qs.empty(), "CKKS scheme requires a list of prime sizes (qs) to be set."
            if not scale>0 and not scale_bits>0:
                warn("<Pyfhel Warning> initializing CKKS context without default scale."
                     "You will have to provide a scale for each encoding", RuntimeWarning)
            self._scale = 2**scale_bits if scale_bits>0 else scale
            self._qs = qs
        self.afseal.ContextGen(<scheme_t>s.value, n, p_bits * (p_bits>0), p, sec, qs)
        
    cpdef void keyGen(self):
        """Generates a pair of secret/Public Keys.
        
        Based on the current context, initializes a public/secret key pair.
        
        Args:
            None

        Return:
            None
        """
        self.afseal.KeyGen()
        
    cpdef void rotateKeyGen(self):
        """Generates a rotation Key.
        
        Generates a rotation Key, used to rotate cyclically 
        the values inside the encrypted vector.
        
        Based on the current context, initializes one rotation key. 
        
        Args:
            None
                      
        Return:
            None
        """
        self.afseal.rotateKeyGen()
        
    cpdef void relinKeyGen(self):
        """Generates a relinearization Key.
        
        Generates a relinearization Key, used to reduce size of the
        ciphertexts when multiplying or exponentiating them. This is needed
        due to the fact that ciphertexts grow in size after encrypted
        mults/exponentiations.
        
        Based on the current context, initializes one relinearization key. 
        
        Args:
            None

        Return:
            None
        """
        self.afseal.relinKeyGen()        
  
    
    # .............................. ENCYRPTION ...............................
    cpdef PyCtxt encryptInt(self, int64_t[:] arr, PyCtxt ctxt=None):
        """Encrypts a 1D vector of int values into a PyCtxt ciphertext.
        
        If provided a ciphertext, encrypts the value inside it. 
        
        Args:
            value (int): value to encrypt.
            ctxt (PyCtxt, optional): Optional destination ciphertext.  
            
        Return:
            PyCtxt: the ciphertext containing the encrypted plaintext
        """
        if ctxt is None:
            ctxt = PyCtxt(pyfhel=self)
        cdef vector[int64_t] vec
        cdef AfsealPtxt ptxt
        vec.assign(&arr[0], &arr[0]+<Py_ssize_t>arr.size)
        self.afseal.encode_i(vec, ptxt)
        self.afseal.encrypt(ptxt, deref(ctxt._ptr_ctxt))
        ctxt._scheme = scheme_t.bfv
        ctxt._pyfhel = self
        return ctxt
    
    cpdef PyCtxt encryptFrac(self, 
        double[:] arr, PyCtxt ctxt=None, 
        double scale=0, int scale_bits=0):
        """Encrypts a 1D vector of float values into a PyCtxt ciphertext.
        
        Encrypts a fractional vector using the current secret key, based on the
        current context. Value must a decimal (float, double) that will 
        get truncated.
        If provided a ciphertext, encrypts the plaintext inside it. 
        
        Args:
            arr (float[]): values to encrypt.
            ctxt (PyCtxt, optional): Optional destination ciphertext.
            scale (double): scale factor to apply to the values.  
            
        Return:
            PyCtxt: the ciphertext containing the encrypted plaintext
        """
        scale = _get_valid_scale(scale_bits, scale, self._scale)
        if ctxt is None:
            ctxt = PyCtxt(pyfhel=self)
        cdef vector[double] vec
        vec.assign(&arr[0], &arr[0] + <Py_ssize_t>arr.size)
        cdef AfsealPtxt ptxt
        self.afseal.encode_f(vec, scale, ptxt)
        self.afseal.encrypt(ptxt, deref(ctxt._ptr_ctxt))
        ctxt._scheme = scheme_t.ckks
        ctxt._pyfhel = self
        return ctxt


    cpdef PyCtxt encryptComplex(
        self, complex[:] arr, PyCtxt ctxt=None,
        double scale=0, int scale_bits=0):
        """Encrypts a 1D vector of complex values into a PyCtxt ciphertext.
        
        Encrypts a fractional vector using the current secret key, based on the
        current context. Value must be a complex (double, double) that will 
        get truncated.
        If provided a ciphertext, encrypts the plaintext inside it. 
        
        Args:
            arr (complex[]): values to encrypt.
            ctxt (PyCtxt, optional): Optional destination ciphertext.
            scale (double): scale factor to apply to the values.  
            
        Return:
            PyCtxt: the ciphertext containing the encrypted plaintext
        """
        scale = _get_valid_scale(scale_bits, scale, self._scale)
        if ctxt is None:
            ctxt = PyCtxt(pyfhel=self)
        cdef vector[cy_complex] vec
        vec.assign(&arr[0], &arr[0] + <Py_ssize_t>arr.size)
        cdef AfsealPtxt ptxt
        self.afseal.encode_c(vec, scale, ptxt)
        self.afseal.encrypt(ptxt, deref(ctxt._ptr_ctxt))
        ctxt._scheme = scheme_t.ckks
        ctxt._pyfhel = self
        return ctxt
        

    cpdef PyCtxt encryptPtxt(self, PyPtxt ptxt, PyCtxt ctxt=None):
        """Encrypts an encoded PyPtxt plaintext into a PyCtxt ciphertext.
        
        Encrypts an encoded PyPtxt plaintext using the current secret
        key, based on the current context. Plaintext must be a PyPtxt.
        If provided a ciphertext, encrypts the plaintext inside it. 
        
        Args:
            ptxt (PyPtxt): plaintext to encrypt.
            ctxt (PyCtxt, optional): Optional destination ciphertext.  
            
        Return:
            PyCtxt: the ciphertext containing the encrypted plaintext
            
        Raise:
            TypeError: if the plaintext doesn't have a valid type.
        """
        if (ptxt._ptr_ptxt == NULL or ptxt is None):
            raise TypeError("<Pyfhel ERROR> PyPtxt Plaintext is empty")
        if ctxt is None:
            ctxt = PyCtxt(pyfhel=self)
        self.afseal.encrypt(deref(ptxt._ptr_ptxt), deref(ctxt._ptr_ctxt))
        ctxt._scheme = ptxt._scheme
        ctxt._pyfhel = self
        return ctxt

    # vectorized
    cpdef np.ndarray[object, ndim=1] encryptAInt(self, int64_t[:,::1] arr):
        raise NotImplementedError("<Pyfhel ERROR> encryptAInt not implemented")

    cpdef np.ndarray[object, ndim=1] encryptAFrac(self, double[:,::1] arr, double scale=0, int scale_bits=0):
        raise NotImplementedError("<Pyfhel ERROR> encryptAFrac not implemented")
        
    cpdef np.ndarray[object, ndim=1] encryptAComplex(self, complex[:,::1] arr, double scale=0, int scale_bits=0):
        raise NotImplementedError("<Pyfhel ERROR> encryptAComplex not implemented")

    cpdef np.ndarray[object, ndim=1] encryptAPtxt(self, PyPtxt[:] ptxt):
        raise NotImplementedError("<Pyfhel ERROR> encryptAPtxt not implemented")

    def encrypt(self, ptxt not None, PyCtxt ctxt=None, scale=None):
        """Encrypts any valid value into a PyCtxt ciphertext.
        
        Encrypts a plaintext using the current secret key, based on the
        current context. Plaintext must be an integer vector (int), a float vector
        that will get truncated (double), or a PyPtxt encoded plaintext.
        Selects the encryption function based on type.
        
        If provided a ciphertext, encrypts the plaintext inside it. 
        
        Args:
            ptxt (PyPtxt, int, double, np.ndarray): plaintext to encrypt.
            ctxt (PyCtxt, optional): Optional destination ciphertext.  
            
        Return:
            PyCtxt: the ciphertext containing the encrypted plaintext
            
        Raise:
            TypeError: if the plaintext doesn't have a valid type.
        """
        # np arrays or numbers -> encode first!
        if isinstance(ptxt, (np.ndarray, np.number, Number, list)):
            ptxt = self.encode(ptxt, scale=self.scale if scale is None else scale)

        # plaintexts
        if isinstance(ptxt, PyPtxt):
            return self.encryptPtxt(ptxt, ctxt)
        
        raise TypeError('<Pyfhel ERROR> Plaintext type ['+str(type(ptxt))+
                        '] not supported for encryption')
    
    # .............................. DECRYPTION ................................
    cpdef np.ndarray[int64_t, ndim=1] decryptInt(self, PyCtxt ctxt):
        """Decrypts a PyCtxt ciphertext into a single int value.
        
        Decrypts a PyCtxt ciphertext using the current secret key, based on
        the current context. PyCtxt scheme must be bfv.
        
        Args:
            ctxt (PyCtxt, optional): ciphertext to decrypt. 
            
        Return:
            int: the decrypted integer value
            
        Raise:
            RuntimeError: if the ctxt scheme isn't Scheme_t.bfv
        """
        if (ctxt._scheme != scheme_t.bfv):
            raise RuntimeError("<Pyfhel ERROR> wrong scheme type in PyCtxt")
        cdef vector[int64_t] vec
        cdef AfsealPtxt ptxt
        self.afseal.decrypt(deref(ctxt._ptr_ctxt), ptxt)
        self.afseal.decode_i(ptxt, vec)
        return np.asarray(<list>vec)

    cpdef np.ndarray[double, ndim=1] decryptFrac(self, PyCtxt ctxt):
        """Decrypts a PyCtxt ciphertext into a vector of floats
        
        Decrypts a PyCtxt ciphertext using the current secret key, based on
        the current context. PyCtxt scheme must be ckks.
        
        Args:
            ctxt (PyCtxt, optional): ciphertext to decrypt. 
            
        Return:
            np.array[float]: the decrypted float vector
            
        Raise:
            RuntimeError: if the ctxt scheme isn't Scheme_t.ckks
        """
        if (ctxt._scheme != scheme_t.ckks):
            raise RuntimeError("<Pyfhel ERROR> wrong scheme type in PyCtxt")
        cdef vector[double] vec
        cdef AfsealPtxt ptxt
        self.afseal.decrypt(deref(ctxt._ptr_ctxt), ptxt)
        self.afseal.decode_f(ptxt, vec)
        return np.asarray(<list>vec)
    
    cpdef np.ndarray[complex, ndim=1] decryptComplex(self, PyCtxt ctxt):
        """Decrypts a PyCtxt ciphertext into a vector of complex values
        
        Decrypts a PyCtxt ciphertext using the current secret key, based on
        the current context. PyCtxt scheme must be ckks.
        
        Args:
            ctxt (PyCtxt, optional): ciphertext to decrypt. 
            
        Return:
            np.array[complex]: the decrypted complex vector
            
        Raise:
            RuntimeError: if the ctxt scheme isn't Scheme_t.ckks
        """
        if (ctxt._scheme != scheme_t.ckks):
            raise RuntimeError("<Pyfhel ERROR> wrong scheme type in PyCtxt")
        cdef vector[cy_complex] vec
        cdef AfsealPtxt ptxt
        self.afseal.decrypt(deref(ctxt._ptr_ctxt), ptxt)
        self.afseal.decode_c(ptxt, vec)
        return np.asarray(<list>vec)
    
    cpdef PyPtxt decryptPtxt(self, PyCtxt ctxt, PyPtxt ptxt=None):
        """Decrypts a PyCtxt ciphertext into a PyPtxt plaintext.
        
        Decrypts a PyCtxt ciphertext using the current secret key, based on
        the current context. No regard to scheme (decode PyPtxt to obtain 
        value).
        
        Args:
            ctxt (PyCtxt): ciphertext to decrypt. 
            ptxt (PyPtxt, optional): Optional destination plaintext.
            
        Return:
            PyPtxt: the decrypted plaintext
        """
        if ptxt is None:
            ptxt = PyPtxt(pyfhel=self)
        self.afseal.decrypt(deref(ctxt._ptr_ctxt), deref(ptxt._ptr_ptxt))
        ptxt._scheme = ctxt._scheme
        return ptxt

    # vectorized
    cpdef np.ndarray[int64_t, ndim=2] decryptAInt(self, PyCtxt ctxt):
        raise NotImplementedError("<Pyfhel ERROR> decryptAInt not implemented")
    cpdef np.ndarray[double, ndim=2] decryptAFrac(self, PyCtxt ctxt):
        raise NotImplementedError("<Pyfhel ERROR> decryptAFrac not implemented")
    cpdef np.ndarray[double, ndim=2] decryptAComplex(self, PyCtxt ctxt):
        raise NotImplementedError("<Pyfhel ERROR> decryptAComplex not implemented")
    cpdef np.ndarray[object, ndim=1] decryptAPtxt(self, PyCtxt ctxt):
        raise NotImplementedError("<Pyfhel ERROR> decryptAPtxt not implemented")
    def decrypt(self, PyCtxt ctxt, bool decode=False, PyPtxt ptxt=None):
        """Decrypts any valid PyCtxt into either a PyPtxt ciphertext or a value.
        
        Decrypts a PyCtxt ciphertext using the current secret key, based on
        the current context. Outputs an integer (int), a truncated decimal
        (float), a PyPtxt encoded plaintext, or in Batch mode a 1D numpy
        vector of integers. Can also return a PyPtxt by setting decode
        to True.

        Selects the encryption function based on type.
        
        If provided a plaintext, decrypts the ciphertext inside it. 
        
        Args:
            ctxt (PyCtxt): ciphertext to decrypt.
            decode (bool: False): return value or return PyPtxt.
            ptxt (PyPtxt, optional): Optional destination PyPtxt.  
            
        Return:
            PyPtxt, np.array[int|float]: the decrypted result
            
        Raise:
            TypeError: if the cipertext scheme is invalid.
        """
        if (decode):
            if (ctxt._scheme == scheme_t.ckks):
                return self.decryptFrac(ctxt)
            elif (ctxt._scheme == scheme_t.bfv):
                return self.decryptInt(ctxt)
            else:
                raise RuntimeError("<Pyfhel ERROR> wrong scheme type in PyCtxt when decrypting")
        else: # Decrypt to plaintext        
            if ptxt is None:
                ptxt = PyPtxt(pyfhel=self)
            return self.decryptPtxt(ctxt, ptxt)


    # ................................ OTHER ..................................
    cpdef int noise_level(self, PyCtxt ctxt):
        """Computes the invariant noise budget (bits) of a PyCtxt ciphertext.
        
        The invariant noise budget measures the amount of room there is
        for thenoise to grow while ensuring correct decryptions.
        Decrypts a PyCtxt ciphertext using the current secret key, based
        on the current context.
        
        Args:
            ctxt (PyCtxt): ciphertext to be measured.
            
        Return:
            int: the noise budget level
        """
        if self.scheme == Scheme_t.ckks:
            raise RuntimeError("<Pyfhel ERROR> ckks scheme does not support noise level")
        return self.afseal.noise_level(deref(ctxt._ptr_ctxt))

    cpdef void relinearize(self, PyCtxt ctxt):
        """Relinearizes a ciphertext.
        
        Relinearizes a ciphertext. This functions relinearizes ctxt,
        reducing its size down to 2. If the size of encrypted is K+1, the
        given evaluation keys need to have size at least K-1. 
        
        To relinearize a ciphertext of size M >= 2 back to size 2, we
        actually need M-2 evaluation keys. Attempting to relinearize a too
        large ciphertext with too few evaluation keys will result in an
        exception being thrown.
        
        Args:
            bitCount (int): The bigger the faster but noisier (will require
                            relinearization). Needs to be within [1, 60]
                      
        Return:
            None
        """
        self.afseal.relinearize(deref(ctxt._ptr_ctxt))  
    
    # =========================================================================
    # ============================== ENCODING =================================
    # =========================================================================
    # ............................... ENCODE ..................................
    cpdef PyPtxt encodeInt(self, int64_t[::1] arr, PyPtxt ptxt=None):
        """Encodes an integer vector into a PyPtxt plaintext.
        
        Encodes a vector of integer values based on the current context.
        If provided a plaintext, encodes the values inside it. 
        
        Args:
            arr (np.array[int]): values to encode.
            
        Return:
            PyPtxt: the plaintext containing the encoded values
        """
        if ptxt is None:
            ptxt = PyPtxt(pyfhel=self)
        cdef vector[int64_t] vec
        vec.assign(&arr[0], &arr[0]+<Py_ssize_t>arr.size)
        self.afseal.encode_i(vec, deref(ptxt._ptr_ptxt))
        ptxt._scheme = scheme_t.bfv
        return ptxt
    
    cpdef PyPtxt encodeFrac(
        self, double[::1] arr, PyPtxt ptxt=None,
        double scale=0, int scale_bits=0) :
        """Encodes a float vector into a PyPtxt plaintext.
        
        Encodes a vector of float values based on the current context.
        If provided a plaintext, encodes the values inside it. 
        
        Args:
            arr (np.array[float]): values to encode.
            ptxt (PyPtxt, optional): Optional destination plaintext.   
            
        Return:
            PyPtxt: the plaintext containing the encoded values
        """
        scale = _get_valid_scale(scale_bits, scale, self._scale)
        if ptxt is None:
            ptxt = PyPtxt(pyfhel=self)
        cdef vector[double] vec
        vec.assign(&arr[0], &arr[0]+<Py_ssize_t>arr.size)
        self.afseal.encode_f(vec, scale, deref(ptxt._ptr_ptxt))
        ptxt._scheme = scheme_t.ckks
        return ptxt

    cpdef PyPtxt encodeComplex(
        self, complex[::1] arr, PyPtxt ptxt=None,
        double scale=0, int scale_bits=0):
        """Encodes a complex vector into a PyPtxt plaintext.
        
        Encodes a vector of complex values based on the current context.
        If provided a plaintext, encodes the values inside it. 
        
        Args:
            arr (np.array[complex]): values to encode.
            ptxt (PyPtxt, optional): Optional destination plaintext.   
            
        Return:
            PyPtxt: the plaintext containing the encoded values
        """
        scale = _get_valid_scale(scale_bits, scale, self._scale)
        if ptxt is None:
            ptxt = PyPtxt(pyfhel=self)
        cdef vector[cy_complex] vec
        vec.assign(&arr[0], &arr[0]+<Py_ssize_t>arr.size)
        self.afseal.encode_c(vec, scale, deref(ptxt._ptr_ptxt))
        ptxt._scheme = scheme_t.ckks
        return ptxt 

    cpdef np.ndarray[object, ndim=1] encodeAInt(self, int[:,::1] arr):
        raise NotImplementedError("<Pyfhel ERROR> encodeAFrac not implemented")

    cpdef np.ndarray[object, ndim=1] encodeAFrac(self, double[:,::1] arr, double scale=0, int scale_bits=0):
        raise NotImplementedError("<Pyfhel ERROR> encodeAFrac not implemented")

    cpdef np.ndarray[object, ndim=1] encodeAComplex(self, complex[:,::1] arr, double scale=0, int scale_bits=0):
        raise NotImplementedError("<Pyfhel ERROR> encodeAFrac not implemented")

    def encode(self, val_vec not None, double scale=0, int scale_bits=0, PyPtxt ptxt=None):
        """Encodes any valid value/vector into a PyPtxt plaintext.
        
        Encodes any valid value/vector based on the current context.
        Value/Vector must be an integer (int), a decimal that will get 
        truncated (float), or in Batch mode a 1D vector of integers.
        
        If provided a plaintext, encodes the vector inside it. 
        
        Args:
            val_vec (int, float, list[int]): value/vector to encode.
            ptxt (PyPtxt, optional): Optional destination plaintext. 
            
        Return:
            PyPtxt: the plaintext containing the encoded vector.
            
        Raise:
            TypeError: if the val_vec doesn't have a valid type.
        """
        scale = _get_valid_scale(scale_bits, scale, self._scale)
        val_vec = np.array(val_vec)
        if (val_vec.ndim==0):     # nSlots = n in bfv, nSlots = n//2 in ckks
            val_vec = np.repeat(val_vec, self.n // (1 + (self.scheme==Scheme_t.ckks)))
        if (val_vec.ndim > 2) or \
            (not np.issubdtype(val_vec.dtype, np.number)):
            raise TypeError('<Pyfhel ERROR> Plaintext numpy array is not'
                            '1D vector of numeric values, cannot encrypt.')
        elif val_vec.ndim == 1:
            if self.scheme == Scheme_t.bfv:
                return self.encodeInt(val_vec.astype(np.int64), ptxt)
            elif self.scheme == Scheme_t.ckks:
                if np.issubdtype(val_vec.dtype, np.complexfloating):
                    return self.encodeComplex(val_vec.astype(complex), ptxt, scale)
                else:
                    return self.encodeFrac(val_vec.astype(np.float64), ptxt, scale)
        elif val_vec.ndim == 2:
            if np.issubdtype(val_vec.dtype, np.integer):
                return self.encryptAInt(val_vec.astype(np.int64))
            elif np.issubdtype(val_vec.dtype, np.floating):
                return self.encryptAFrac(val_vec.astype(np.float64), scale)
            elif np.issubdtype(val_vec.dtype, np.complexfloating):
                return self.encryptAComplex(val_vec.astype(complex), scale)
        raise TypeError('<Pyfhel ERROR> Value/Vector type ['+str(type(val_vec))+
                        '] not supported for scheme')

    # ................................ DECODE .................................
    cpdef np.ndarray[int64_t, ndim=1] decodeInt(self, PyPtxt ptxt):
        """Decodes a PyPtxt plaintext into a single int value.
        
        Decodes a PyPtxt plaintext into a single int value based on
        the current context. PyPtxt scheme must be bfv.
        
        Args:
            ptxt (PyPtxt, optional): plaintext to decode. 
            
        Return:
            int: the decoded integer value
            
        Raise:
            RuntimeError: if the ciphertext scheme isn't Scheme_t.bfv
        """
        if ptxt._scheme != scheme_t.bfv:
            raise RuntimeError('<Pyfhel ERROR> PyPtxt scheme must be bfv')
        cdef vector[int64_t] output_vector
        self.afseal.decode_i(deref(ptxt._ptr_ptxt), output_vector)
        return vec_to_array_i(output_vector)
    
    cpdef np.ndarray[double, ndim=1] decodeFrac(self, PyPtxt ptxt):
        """Decodes a PyPtxt plaintext into a single float value.
        
        Decodes a PyPtxt plaintext into a single float value based on
        the current context. PyPtxt scheme must be ckks.
        
        Args:
            ptxt (PyPtxt): plaintext to decode.
            
        Return:
            float: the decoded float value
            
        Raise:
            RuntimeError: if the ciphertext scheme isn't Scheme_t.ckks
        """
        if ptxt._scheme != scheme_t.ckks:
            raise RuntimeError('<Pyfhel ERROR> PyPtxt scheme must be ckks')
        cdef vector[double] output_vector
        self.afseal.decode_f(deref(ptxt._ptr_ptxt), output_vector)
        return np.copy(<double [:output_vector.size()]>output_vector.data())
    

    cpdef np.ndarray[complex, ndim=1] decodeComplex(self, PyPtxt ptxt):
        """Decodes a PyPtxt plaintext into a single float value.
        
        Decodes a PyPtxt plaintext into a single float value based on
        the current context. PyPtxt scheme must be ckks.
        
        Args:
            ptxt (PyPtxt): plaintext to decode.
            
        Return:
            float: the decoded float value
            
        Raise:
            RuntimeError: if the ciphertext scheme isn't Scheme_t.ckks
        """
        if ptxt._scheme != scheme_t.ckks:
            raise RuntimeError('<Pyfhel ERROR> PyPtxt scheme must be ckks')
        cdef vector[cy_complex] output_vector
        self.afseal.decode_c(deref(ptxt._ptr_ptxt), output_vector)  
        return np.asarray(output_vector)
    
    cpdef np.ndarray[int64_t, ndim=2] decodeAInt(self, PyPtxt[:] ptxt):
        raise NotImplementedError("<Pyfhel ERROR> decodeAInt not implemented")

    cpdef np.ndarray[double, ndim=2] decodeAFrac(self, PyPtxt[:] ptxt):
        raise NotImplementedError("<Pyfhel ERROR> decodeAFrac not implemented")
        
    cpdef np.ndarray[complex, ndim=2] decodeAComplex(self, PyPtxt[:] ptxt):
        raise NotImplementedError("<Pyfhel ERROR> decodeAFrac not implemented")

    def decode(self, PyPtxt ptxt):
        """Decodes any valid PyPtxt into a value or vector.
        
        Decodes a PyPtxt plaintext based on the current context.
        Outputs an integer (int), a truncated decimal (float), or in 
        Batch mode a 1D vector of integers. Automatically selects the
        decoding function based on type.
    
        Args:
            ptxt (PyPtxt, int, float, np.array): plaintext to decode.
            
        Return:
            int, float, list[int]: the decoded value or vector.
            
        Raise:
            TypeError: if the plaintext doesn't have a valid type.
        """
        if (ptxt._scheme == scheme_t.ckks):
            return self.decodeFrac(ptxt)
        elif (ptxt._scheme == scheme_t.bfv):
            return self.decodeInt(ptxt)
        else:
            raise RuntimeError("<Pyfhel ERROR> wrong scheme in PyPtxt. Cannot decode")

            
    # =========================================================================
    # ============================= OPERATIONS ================================
    # =========================================================================
    cpdef PyCtxt square(self, PyCtxt ctxt, bool in_new_ctxt=False):
        """Square PyCtxt ciphertext value/s.
    
        Args:
            ctxt (PyCtxt): ciphertext whose values are squared.  
            in_new_ctxt (bool): result in a newly created ciphertext
        Return:
            PyCtxt: resulting ciphertext, the input transformed or a new one
        """
        if (in_new_ctxt):
            ctxt = PyCtxt(ctxt)
        self.afseal.square(deref(ctxt._ptr_ctxt))
        return ctxt
        
    cpdef PyCtxt negate(self, PyCtxt ctxt, bool in_new_ctxt=False):
        """Negate PyCtxt ciphertext value/s.
    
        Args:
            ctxt (PyCtxt): ciphertext whose values are negated.   
            in_new_ctxt (bool): result in a newly created ciphertext
            
        Return:
            PyCtxt: resulting ciphertext, the input transformed or a new one
        """
        if (in_new_ctxt):
            new_ctxt = PyCtxt(ctxt)
            self.afseal.negate(deref(new_ctxt._ptr_ctxt))
            return new_ctxt
        else:
            self.afseal.negate(deref(ctxt._ptr_ctxt))
            return ctxt

        
    cpdef PyCtxt add(self, PyCtxt ctxt, PyCtxt ctxt_other, bool in_new_ctxt=False):
        """Sum two PyCtxt ciphertexts homomorphically.
        
        Sums two ciphertexts. Encoding must be the same. Requires same
        context and encryption with same public key. The result is applied
        to the first ciphertext.
    
        Args:
            ctxt (PyCtxt): ciphertext whose values are added with ctxt_other.  
            ctxt_other (PyCtxt): ciphertext left untouched.  
            in_new_ctxt (bool): result in a newly created ciphertext
            
        Return:
            PyCtxt: resulting ciphertext, the input transformed or a new one
        """
        if (ctxt._scheme != ctxt_other._scheme):
            raise RuntimeError(f"<Pyfhel ERROR> scheme type mistmatch in add terms"
                                " ({ctxt._scheme} VS {ctxt_other._scheme})")
        if (in_new_ctxt):
            ctxt = PyCtxt(copy_ctxt=ctxt)
        self.afseal.add(deref(ctxt._ptr_ctxt), deref(ctxt_other._ptr_ctxt))
        return ctxt
        
        
    cpdef PyCtxt add_plain(self, PyCtxt ctxt, PyPtxt ptxt, bool in_new_ctxt=False):
        """Sum a PyCtxt ciphertext and a PyPtxt plaintext.
        
        Sums a ciphertext and a plaintext. Encoding must be the same. 
        Requiressame context and encryption with same public key. The result
        is applied to the first ciphertext.
    
        Args:
            ctxt (PyCtxt): ciphertext whose values are added with ptxt.  
            ptxt (PyPtxt): plaintext left untouched.  
            in_new_ctxt (bool): result in a newly created ciphertext
            
        Return:
            PyCtxt: resulting ciphertext, the input transformed or a new one
        """
        if (ctxt._scheme != ptxt._scheme):
            raise RuntimeError("<Pyfhel ERROR> scheme type mistmatch in add terms"
                                " ({ctxt._scheme} VS {ptxt._scheme})")
        if (in_new_ctxt):
            ctxt = PyCtxt(copy_ctxt=ctxt)
        self.afseal.add_plain(deref(ctxt._ptr_ctxt), deref(ptxt._ptr_ptxt))
        return ctxt

            
    cpdef PyCtxt sub(self, PyCtxt ctxt, PyCtxt ctxt_other, bool in_new_ctxt=False):
        """Substracts one PyCtxt ciphertext from another.
        
        Substracts one ciphertext from another. Encoding must be the same.
        Requires same context and encryption with same public key.
        The result is stored/applied to the first ciphertext.
    
        Args:
            ctxt (PyCtxt): ciphertext substracted by ctxt_other.    
            ctxt_other (PyCtxt): ciphertext being substracted from ctxt.
            in_new_ctxt (bool): result in a newly created ciphertext
            
        Return:
            PyCtxt: resulting ciphertext, the input transformed or a new one
        """
        if (ctxt._scheme != ctxt_other._scheme):
            raise RuntimeError("<Pyfhel ERROR> scheme type mistmatch in sub terms"
                                " ({ctxt._scheme} VS {ctxt_other._scheme})")
        if (in_new_ctxt):
            new_ctxt = PyCtxt(ctxt)
            self.afseal.sub(deref(new_ctxt._ptr_ctxt), deref(ctxt_other._ptr_ctxt))
            return new_ctxt
        else:
            self.afseal.sub(deref(ctxt._ptr_ctxt), deref(ctxt_other._ptr_ctxt))
            return ctxt
        
    cpdef PyCtxt sub_plain (self, PyCtxt ctxt, PyPtxt ptxt, bool in_new_ctxt=False):
        """Substracts a PyCtxt ciphertext and a plaintext.
        
        Performs ctxt = ctxt - ptxt. Encoding must be the same. Requires 
        same context and encryption with same public key. The result is 
        stored/applied to the ciphertext.
    
        Args:
            ctxt (PyCtxt): ciphertext substracted by ptxt.   
            * ptxt (PyPtxt): plaintext substracted from ctxt.
            in_new_ctxt (bool): result in a newly created ciphertext
            
        Return:
            PyCtxt: resulting ciphertext, the input transformed or a new one
        """
        if (ctxt._scheme != ptxt._scheme):
            raise RuntimeError("<Pyfhel ERROR> scheme type mistmatch in sub terms"
                                " ({ctxt._scheme} VS {ptxt._scheme})")
        
        if (in_new_ctxt):
            ctxt = PyCtxt(ctxt)
        self.afseal.sub_plain(deref(ctxt._ptr_ctxt), deref(ptxt._ptr_ptxt))
        return ctxt

        
    cpdef PyCtxt multiply (self, PyCtxt ctxt, PyCtxt ctxt_other, bool in_new_ctxt=False):
        """Multiply first PyCtxt ciphertext by the second PyCtxt ciphertext.
        
        Multiplies two ciphertexts. Encoding must be the same. Requires 
        same context and encryption with same public key. The result is 
        applied to the first ciphertext.
    
        Args:
            ctxt (PyCtxt): ciphertext multiplied with ctxt_other.   
            ctxt_other (PyCtxt): ciphertext left untouched.  
            in_new_ctxt (bool): result in a newly created ciphertext.
            
        Return:
            PyCtxt: resulting ciphertext, the input transformed or a new one
        """
        if (ctxt._scheme != ctxt_other._scheme):
            raise RuntimeError("<Pyfhel ERROR> scheme type mistmatch in mult terms"
                                " ({ctxt._scheme} VS {ctxt_other._scheme})")
        
        if (in_new_ctxt):
            new_ctxt = PyCtxt(ctxt)
            self.afseal.multiply(deref(new_ctxt._ptr_ctxt), deref(ctxt_other._ptr_ctxt))
            return new_ctxt
        else:
            self.afseal.multiply(deref(ctxt._ptr_ctxt), deref(ctxt_other._ptr_ctxt))
            return ctxt
        
    cpdef PyCtxt multiply_plain (self, PyCtxt ctxt, PyPtxt ptxt, bool in_new_ctxt=False):
        """Multiply a PyCtxt ciphertext and a PyPtxt plaintext.
        
        Multiplies a ciphertext and a plaintext. Encoding must be the same. 
        Requires same context and encryption with same public key. The 
        result is applied to the first ciphertext.
    
        Args:
            ctxt (PyCtxt): ciphertext whose values are multiplied with ptxt.  
            ptxt (PyPtxt): plaintext left untouched.  
            
        Return:
            PyCtxt: resulting ciphertext, either the input transformed or a new one
        """
        if (ctxt._scheme != ptxt._scheme):
            raise RuntimeError("<Pyfhel ERROR> scheme type mistmatch in mult terms"
                                " ({ctxt._scheme} VS {ptxt._scheme})")   
        if (in_new_ctxt):
            ctxt = PyCtxt(ctxt)
        self.afseal.multiply_plain(deref(ctxt._ptr_ctxt), deref(ptxt._ptr_ptxt))     
        return ctxt
        
    cpdef PyCtxt rotate(self, PyCtxt ctxt, int k, bool in_new_ctxt=False):
        """Rotates cyclically PyCtxt ciphertext values k positions.
        
        Performs a cyclic rotation over a cyphertext encoded in BATCH mode. 
        Requires previously initialized rotation keys with rotateKeyGen().
    
        Args:
            ctxt (PyCtxt): ciphertext whose values are rotated.
            k (int): number of positions to rotate.
            in_new_ctxt (bool): result in a newly created ciphertext
            
        Return:
            PyCtxt: resulting ciphertext, the input transformed or a new one
        """
        if self.is_rotate_key_empty():
            warn("<Pyfhel Warning> rot_key empty, initializing it for rotation.", RuntimeWarning)
            self.rotateKeyGen()
        if (in_new_ctxt):
            new_ctxt = PyCtxt(ctxt)
            self.afseal.rotate(deref(new_ctxt._ptr_ctxt), k)
            return new_ctxt
        else:
            self.afseal.rotate(deref(ctxt._ptr_ctxt), k)
            return ctxt
        
    cpdef PyCtxt power(self, PyCtxt ctxt, uint64_t expon, bool in_new_ctxt=False):
        """Exponentiates PyCtxt ciphertext value/s to expon power.
        
        Performs an exponentiation over a cyphertext. Requires previously
        initialized relinearization keys with relinearizeKeyGen(), since
        it applies relinearization after each multiplication.
    
        Args:
            ctxt (PyCtxt): ciphertext whose value/s are exponetiated.  
            expon (int): exponent.
            in_new_ctxt (bool): result in a newly created ciphertext
            
        Return:
            PyCtxt: resulting ciphertext, the input transformed or a new one
        """
        if (in_new_ctxt):
            new_ctxt = PyCtxt(ctxt)
            self.afseal.exponentiate(deref(new_ctxt._ptr_ctxt), expon)  
            return new_ctxt
        else:
            self.afseal.exponentiate(deref(ctxt._ptr_ctxt), expon) 
            return ctxt

    # CKKS
    cpdef void rescale_to_next(self, PyCtxt ctxt):
        """Rescales a ciphertext by dividing it by one scale factor.

        Args:
            ctxt (PyCtxt): Ciphertext to rescale.

        Return:
            None

        """
        if self.scheme != Scheme_t.ckks:
            raise RuntimeError("<Pyfhel ERROR> Scheme must be CKKS for rescaling")
        self.afseal.rescale_to_next(deref(ctxt._ptr_ctxt))

    def mod_switch_to_next(self, cipher_or_plain):
        """Reduces the ciphertext/plaintext modulus with next prime in the qs chain.

        Args:
            cipher_or_plain (PyCtxt|PyPtxt): Ciphertext to reduce.

        Return:
            None
        """
        if isinstance(cipher_or_plain, PyCtxt):
            self.afseal.mod_switch_to_next(deref((<PyCtxt>cipher_or_plain)._ptr_ctxt))
        elif isinstance(cipher_or_plain, PyPtxt):
            self.afseal.mod_switch_to_next_plain(deref((<PyPtxt>cipher_or_plain)._ptr_ptxt))
        else:
            raise TypeError("<Pyfhel ERROR> Expected PyCtxt or PyPtxt for mod switching.")
        
    # =========================================================================
    # ================================ I/O ====================================
    # =========================================================================   

    # FILES

    cpdef size_t save_context(self, fileName, str compr_mode="zstd"):
        """Saves current context in a file
        
        Args:
            fileName (str, pathlib.Path): Name of the file.  
            compr_mode (str): Compression. One of "none", "zlib", "zstd" 
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef string f_name = _to_valid_file_str(fileName, check=False).encode()
        cdef ofstream outputter = ofstream(f_name, binary)
        return self.afseal.save_context(outputter, compr_mode.encode())
    
    cpdef size_t load_context(self, fileName):
        """Restores context from a file
        
        Args:
            fileName (str, pathlib.Path): Name of the file.   
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef string f_name = _to_valid_file_str(fileName, check=False).encode()
        cdef ifstream inputter = ifstream(f_name, binary)
        return self.afseal.load_context(inputter)

    cpdef size_t save_public_key(self, fileName, str compr_mode="zstd"):
        """Saves current public key in a file
        
        Args:
            fileName (str, pathlib.Path): Name of the file.   
            compr_mode (str): Compression. One of "none", "zlib", "zstd" 
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef string f_name = _to_valid_file_str(fileName, check=False).encode()
        cdef ofstream outputter = ofstream(f_name, binary)
        return self.afseal.save_public_key(outputter, compr_mode.encode())
            
    cpdef size_t load_public_key(self, fileName):
        """Restores current public key from a file
        
        Args:
            fileName (str, pathlib.Path): Name of the file.   
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef string f_name = _to_valid_file_str(fileName, check=False).encode()
        cdef ifstream inputter = ifstream(f_name, binary)
        return self.afseal.load_public_key(inputter)

    cpdef size_t save_secret_key(self, fileName, str compr_mode="zstd"):
        """Saves current secret key in a file
        
        Args:
            fileName (str, pathlib.Path): Name of the file.   
            compr_mode (str): Compression. One of "none", "zlib", "zstd"
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef string f_name = _to_valid_file_str(fileName, check=False).encode()
        cdef ofstream outputter = ofstream(f_name, binary)
        return self.afseal.save_secret_key(outputter, compr_mode.encode())
    
    cpdef size_t load_secret_key(self, fileName):
        """Restores current secret key from a file
        
        Args:
            fileName (str, pathlib.Path): Name of the file.   
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef string f_name = _to_valid_file_str(fileName, check=False).encode()
        cdef ifstream inputter = ifstream(f_name, binary)
        return self.afseal.load_secret_key(inputter)
    
    cpdef size_t save_relin_key(self, fileName, str compr_mode="zstd"):
        """Saves current relinearization keys in a file
        
        Args:
            fileName (str, pathlib.Path): Name of the file.   
            compr_mode (str): Compression. One of "none", "zlib", "zstd"
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef string f_name = _to_valid_file_str(fileName, check=False).encode()
        cdef ofstream outputter = ofstream(f_name, binary)
        return self.afseal.save_relin_keys(outputter, compr_mode.encode())
    
    cpdef size_t load_relin_key(self, fileName):
        """Restores current relinearization keys from a file
        
        Args:
            fileName (str, pathlib.Path): Name of the file.   
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef string f_name = _to_valid_file_str(fileName, check=False).encode()
        cdef ifstream inputter = ifstream(f_name, binary)
        return self.afseal.load_relin_keys(inputter)
    
    cpdef size_t save_rotate_key(self, fileName, str compr_mode="zstd"):
        """Saves current rotation Keys from a file
        
        Args:
            fileName (str, pathlib.Path): Name of the file.   
            compr_mode (str): Compression. One of "none", "zlib", "zstd"
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef string f_name = _to_valid_file_str(fileName, check=False).encode()
        cdef ofstream outputter = ofstream(f_name, binary)
        return self.afseal.save_rotate_keys(outputter, compr_mode.encode())
    
    cpdef size_t load_rotate_key(self, fileName):
        """Restores current rotation Keys from a file
        
        Args:
            fileName (str, pathlib.Path): Name of the file.   
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef string f_name = _to_valid_file_str(fileName, check=False).encode()
        cdef ifstream inputter = ifstream(f_name, binary)
        return self.afseal.load_rotate_keys(inputter)
    
    
    # BYTES

    cpdef bytes to_bytes_context(self, str compr_mode="zstd"):
        """Saves current context in a bytes string
        
        Args:
            compr_mode (str): Compression. One of "none", "zlib", "zstd" 
            
        Return:
            bytes: Serialized Context.
        """
        cdef ostringstream outputter
        self.afseal.save_context(outputter, compr_mode.encode())
        return outputter.str()
    
    cpdef size_t from_bytes_context(self, bytes content):
        """Restores current context from a bytes object
        
        Args:
            content (bytes): bytes object obtained from to_bytes_context   
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef stringstream inputter
        inputter.write(content,len(content))
        return self.afseal.load_context(inputter)

    cpdef bytes to_bytes_public_key(self, str compr_mode="zstd"):
        """Saves current public key in a bytes string
        
        Args:
            compr_mode (str): Compression. One of "none", "zlib", "zstd" 
            
        Return:
            bytes: Serialized public key.
        """
        cdef ostringstream outputter
        self.afseal.save_public_key(outputter, compr_mode.encode())
        return outputter.str()
            
    cpdef size_t from_bytes_public_key(self, bytes content):
        """Restores current public key from a bytes object
        
        Args:
            content (bytes): bytes object obtained from to_bytes_public_key   
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef stringstream inputter
        inputter.write(content,len(content))
        return self.afseal.load_public_key(inputter)

    cpdef bytes to_bytes_secret_key(self, str compr_mode="zstd"):
        """Saves current secret key in a bytes string
        
        Args:
            compr_mode (str): Compression. One of "none", "zlib", "zstd" 
            
        Return:
            bytes: Serialized secret key.
        """
        cdef ostringstream outputter
        self.afseal.save_secret_key(outputter, compr_mode.encode())
        return outputter.str()
    
    cpdef size_t from_bytes_secret_key(self, bytes content):
        """Restores current secret key from a bytes object
        
        Args:
            content (bytes): bytes object obtained from to_bytes_secret_key   
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef stringstream inputter
        inputter.write(content,len(content))
        return self.afseal.load_secret_key(inputter)
    
    cpdef bytes to_bytes_relin_key(self, str compr_mode="zstd"):
        """Saves current relinearization key in a bytes string
        
        Args:
            compr_mode (str): Compression. One of "none", "zlib", "zstd" 
            
        Return:
            bytes: Serialized relinearization key.
        """
        cdef ostringstream outputter
        self.afseal.save_relin_keys(outputter, compr_mode.encode())
        return outputter.str()
    
    cpdef size_t from_bytes_relin_key(self, bytes content):
        """Restores current relin key from a bytes object
        
        Args:
            content (bytes): bytes object obtained from to_bytes_relin_key   
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef stringstream inputter
        inputter.write(content,len(content))
        return self.afseal.load_relin_keys(inputter)
    
    cpdef bytes to_bytes_rotate_key(self, str compr_mode="zstd"):
        """Saves current context in a bytes string
        
        Args:
            compr_mode (str): Compression. One of "none", "zlib", "zstd" 
            
        Return:
            bytes: Serialized rotation key.
        """
        cdef ostringstream outputter
        self.afseal.save_rotate_keys(outputter, compr_mode.encode())
        return outputter.str()
    
    cpdef size_t from_bytes_rotate_key(self, bytes content):
        """Restores current rotation key from a bytes object
        
        Args:
            content (bytes): bytes object obtained from to_bytes_rotateKey   
            
        Return:
            bool: Result, True if OK, False otherwise.
        """
        cdef stringstream inputter
        inputter.write(content,len(content))
        return self.afseal.load_rotate_keys(inputter)
         
    
    # =========================================================================
    # ============================== AUXILIARY ================================
    # =========================================================================
    cpdef long maxBitCount(self, long poly_modulus_degree, int sec_level):
        """Returns the maximum number of bits that can be used to encode a number.

        Args:
            poly_modulus_degree (long): Polynomial modulus degree.
            sec_level (int): Security level.

        Return:
            long: Maximum number of bits that can be used to encode a number.
        """
        return (<Afseal*>self.afseal).maxBitCount(poly_modulus_degree, sec_level)

    def multDepth(self, max_depth=64, delta=0.1, x_y_z=(1, 10, 0.1), verbose=False):
        """Empirically determines the multiplicative depth of a Pyfhel Object
        for a given context. For this, it encrypts the inputs x, y and z with
        Fractional scheme and performs the following chained multiplication
        until the result deviates more than delta in absolute value:
        
        >    x * y * z * y * z * y * z * y * z ...

        After each multiplication, the ciphertext is relinearized and checked.
        Ideally, y and z should be inverses to avoid wrapping over modulo p.
        Requires the Pyfhel Object to have initialized context and pub/sec/relin keys.
        """
        # x,y,z = x_y_z
        # cx = self.encryptFrac(x)
        # cy = self.encryptFrac(y)
        # cz = self.encryptFrac(z)
        # for m_depth in range(1, max_depth+1):
        #     if m_depth%2: # Multiply by y and relinearize
        #         x *= y
        #         cx *= cy
        #     else:         # Multiply by z and relinearize
        #         x *= z
        #         cx *= cz
        #     ~cx           # Relinearize after every multiplication
        #     x_hat = self.decryptFrac(cx)
        #     if verbose:
        #         print(f'Mult {m_depth} [budget: {self.noiseLevel(cx)} dB]: {x_hat} (expected {x})')
        #     if abs(x - x_hat) > delta:
        #         break
        # return m_depth
        raise NotImplementedError("multDepth is not implemented yet")

    # GETTERS
    cpdef bool batchEnabled(self):
        """Flag of batch enabled. 
            
        Return:
            bool: Result, True if enabled, False if disabled.
        """
        return (<Afseal*>self.afseal).batchEnabled()
    

    cpdef int get_nSlots(self):
        """Maximum number of slots fitting in a ciphertext in BATCH mode.
        
        Generally it matches with `m`.

        Return:
            int: Maximum umber of slots.
        """
        return (<Afseal*>self.afseal).get_nSlots()
    
    cpdef uint64_t get_plain_modulus(self):
        """Plaintext modulus of the current context.
            
        Return:
            int: Plaintext modulus.
        """
        return self.afseal.get_plain_modulus()
    
    cpdef size_t get_poly_modulus_degree(self):
        """Plaintext coefficient of the current context.
        
        The more, the bigger the ciphertexts are, thus allowing for 
        more operations with correct decryption. Also, number of 
        values in a ciphertext in both schemes. 
        
            
        Return:
            int: Plaintext coefficient.
        """
        return self.afseal.get_poly_modulus_degree()

    cpdef scheme_t get_scheme(self):
        """Scheme of the current context.

        Return:
            scheme_t: Scheme.
        """
        return self.afseal.get_scheme()
    
    cpdef bool is_secret_key_empty(self):
        """True if the current Pyfhel instance has no secret Key.

        Return:
            bool: True if there is no secret Key. False if there is.
        """
        return (<Afseal*>self.afseal).is_secretKey_empty()

    cpdef bool is_public_key_empty(self):
        """True if the current Pyfhel instance has no public Key.

        Return:
            bool: True if there is no public Key. False if there is.
        """
        return (<Afseal*>self.afseal).is_publicKey_empty()

    cpdef bool is_rotate_key_empty(self):
        """True if the current Pyfhel instance has no rotation key.

        Return:
            bool: True if there is no rotation Key. False if there is.
        """
        return (<Afseal*>self.afseal).is_rotKey_empty()

    cpdef bool is_relin_key_empty(self):
        """True if the current Pyfhel instance has no relinearization key.

        Return:
            bool: True if there is no relinearization Key. False if there is.
        """
        return (<Afseal*>self.afseal).is_relinKeys_empty()

    cpdef bool is_context_empty(self):
        """True if the current Pyfhel instance has no context.

        Return:
            bool: True if there is no context. False if there is.
        """
        return (<Afseal*>self.afseal).is_context_empty()



    # =========================================================================
    # =============================== PyPoly ==================================
    # =========================================================================  
    # CREATION
    cpdef PyPoly empty_poly(self, PyCtxt ref):
        """Generates an empty polynomial using `ref` as reference"""
        # poly._afpoly =  <AfsealPoly *> self.afseal.empty_poly(deref(ref._ptr_ctxt))
        return PyPoly(ref=ref)
    
    cpdef PyPoly poly_from_ciphertext(self, PyCtxt ctxt, size_t i):
        """Gets the i-th underlying polynomial of a ciphertext"""
        return PyPoly(ref=ctxt, index=i)

    cpdef PyPoly poly_from_plaintext(self, PyCtxt ref, PyPtxt ptxt):
        """Gets the underlying polynomial of a plaintext"""
        return PyPoly(ref=ref, ptxt=ptxt)

    cpdef PyPoly poly_from_coeff_vector(self, vector[cy_complex] coeff_vector, PyCtxt ref):
        """Generates a polynomial with given coefficients"""
        return PyPoly(coeff_vector, ref=ref)
    
    cpdef list polys_from_ciphertext(self, PyCtxt ctxt):
        """Generates a list of polynomials of the given ciphertext"""
        raise NotImplementedError("TODO: Not yet there")

    # OPS
    cpdef PyPoly poly_add(self, PyPoly p, PyPoly p_other, bool in_new_poly=False):
        """Sum two PyPoly polynomials: p + p_other.
        
        Encoding must be consistent (TODO).  The result is applied
        to the first polynomial or to a newly created one.
    
        Args:
            p (PyPoly): polynomial whose values are added with p_other.  
            p_other (PyPoly): polynomial left untouched.  
            in_new_poly (bool): result in a newly created polynomial
            
        Return:
            PyPoly: resulting polynomial, the input transformed or a new one.
        """
        res_poly = PyPoly(p) if in_new_poly else p
        self.afseal.add_inplace(deref(res_poly._afpoly), deref(p_other._afpoly))
        return res_poly

    cpdef PyPoly poly_subtract(self, PyPoly p, PyPoly p_other, bool in_new_poly=False):
        """Subtract two PyPoly polynomials: p - p_other.
        
        Encoding must be consistent (TODO).  The result is applied
        to the first polynomial or to a newly created one.
    
        Args:
            p (PyPoly): polynomial whose values are subtracted with p_other.  
            p_other (PyPoly): polynomial left untouched.  
            in_new_poly (bool): result in a newly created polynomial
            
        Return:
            PyPoly: resulting polynomial, the input transformed or a new one.
        """
        res_poly = PyPoly(p) if in_new_poly else p
        self.afseal.subtract_inplace(deref(res_poly._afpoly), deref(p_other._afpoly))
        return res_poly

    cpdef PyPoly poly_multiply(self, PyPoly p, PyPoly p_other, bool in_new_poly=False):
        """Multiply two PyPoly polynomials: p * p_other.
        
        Encoding must be consistent (TODO).  The result is applied
        to the first polynomial or to a newly created one.
    
        Args:
            p (PyPoly): polynomial whose values are multiplied with p_other.  
            p_other (PyPoly): polynomial left untouched.  
            in_new_poly (bool): result in a newly created polynomial
            
        Return:
            PyPoly: resulting polynomial, the input transformed or a new one.
        """
        res_poly = PyPoly(p) if in_new_poly else p
        self.afseal.multiply_inplace(deref(res_poly._afpoly), deref(p_other._afpoly))
        return res_poly

    cpdef PyPoly poly_invert(self, PyPoly p, bool in_new_poly=False):
        """Invert PyPoly polynomial: inverse(p)
        
        Encoding must be consistent (TODO).  The result is applied
        to the polynomial or to a newly created one.
    
        Args:
            p (PyPoly): polynomial whose values are inverted.  
            in_new_poly (bool): result in a newly created polynomial
            
        Return:
            PyPoly: resulting polynomial, the input transformed or a new one.
        """
        res_poly = PyPoly(p) if in_new_poly else p
        self.afseal.invert_inplace(deref(res_poly._afpoly))
        return res_poly

    # I/O
    cpdef void poly_to_ciphertext(self, PyPoly p, PyCtxt ctxt, size_t i):
        """Set chosen i-th polynimial in ctxt to p.
        
        Encoding must be consistent (TODO).
    
        Args:
            p (PyPoly): polynomial to be inserted.  
            ctxt (PyCtxt): base ciphertext.
            i (int): number of polynomial in ctxt to be set.
            
        Return:
            None
        """
        self.afseal.poly_to_ciphertext(deref(p._afpoly), deref(ctxt._ptr_ctxt), i)

    cpdef void poly_to_plaintext(self, PyPoly p, PyPtxt ptxt):
        """Set the polynimial in ptxt to p.
        
        Encoding must be consistent (TODO).
    
        Args:
            p (PyPoly): polynomial to be inserted.  
            ptxt (PyPtxt): base plaintext.
            
        Return:
            None
        """
        self.afseal.poly_to_plaintext(deref(p._afpoly), deref(ptxt._ptr_ptxt))


    