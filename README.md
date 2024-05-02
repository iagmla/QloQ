# QloQ

Python implementation of the RSA based encryption algorithm QloQ created by Karl Zander.

# Description

Generate 4 primes not equal (a, b, p, q)

n = p * q

m = a * b

t = ((a - 1) * (b - 1) * (p - 1) * (q - 1)

pk = random integer such that GCD of integer and t = 1.

sk = modular inverse of (pk, t)

if n < m swap n and m

Encryption and decryption are achieved with 2 exponentiations. Encryption m first then n, decryption, n first then m. Signing and verification are achieved similarly to RSA signing modulus order (m, n) verification modulus order (n, m).
