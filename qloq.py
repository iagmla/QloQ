from Crypto.Util import number
import hashlib

# requires pycrypto

def encrypt(ptxt, pk, n, M):
    phase1 = pow(ptxt, pk, M)
    return pow(phase1, pk, n)

def decrypt(ctxt, sk, n, M):
    phase1 = pow(ctxt, sk, n)
    return pow(phase1, sk, M)

def sign(h, sk, n, M):
    phase1 = pow(h, sk, M)
    return pow(phase1, sk, n)

def verify(s, h, pk, n, M):
    phase1 = pow(s, pk, n)
    phase2 = pow(phase1, pk, M)
    if phase2 == h:
        return True
    else:
        return False

def testencrypt(pk, sk, n, M):
    msg = b"01234567890ABCDEF"
    m = number.bytes_to_long(msg)
    ctxt = encrypt(m, pk, n, M)
    if sk != None:

        ptxt = decrypt(ctxt, sk, n, M)
        if ptxt == m:
            return True
        else:
            return False
    return False

def genBasePrimes(psize):
    p = number.getPrime(psize)
    q = number.getPrime(psize)
    while q == p:
        q = number.getPrime(psize)
    a = number.getPrime(psize)
    while a == p or a == q:
        a = number.getPrime(psize)
    b = number.getPrime(psize)
    while b == p or b == q or b == a:
        b = number.getPrime(psize)
    return p, q, a, b

def keygen(psize):
    good = 0
    # Generate base primes
    p, q, a, b = genBasePrimes(psize)
    n = p * q
    M = a * b
    t = ((a - 1) * (b - 1) * (p - 1) * (q - 1))
    # Generate the public key
    pk = (number.getRandomRange(1, t))
    g = number.GCD(pk, t)
    while g != 1:
        pk = (number.getRandomRange(1, t))
        g = number.GCD(pk, t)
        if g == 1:
            break
    # Generate the secret key
    sk = number.inverse(pk, t)
    if n < M:
        tmp = M
        M = n
        n = M
    if pk != None:
        if testencrypt(pk, sk, n, M):
            good = 1
    return sk, pk, n, M

def oaep_encrypt(m, mod):
    # This is for testing purposes only
    n = len(bin(abs(mod))[2:]) 
    k0 = 1
    k1 = 0
    ks0 = len(bin(abs(k0))[2:])
    ks1 = len(bin(abs(k1))[2:])
    r = number.getRandomNBitInteger(n)
    G = number.bytes_to_long(hashlib.sha256(number.long_to_bytes(r)).digest())
    X = m ^ G
    H = number.bytes_to_long(hashlib.sha256(number.long_to_bytes(X)).digest())
    Y = r ^ H
    return X, Y

def oaep_decrypt(X, Y):
    r = number.bytes_to_long(hashlib.sha256(X).digest()) ^ number.bytes_to_long(Y)
    m = (number.bytes_to_long(hashlib.sha256(number.long_to_bytes(r)).digest()) ^ number.bytes_to_long(X))
    return m
