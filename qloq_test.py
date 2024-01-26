from qloq import keygen, encrypt, decrypt, sign, verify

sk, pk, n, M = keygen(512)
msg = 123
ctxt = encrypt(msg, pk, n, M)
print(ctxt)
ptxt = decrypt(ctxt, sk, n, M)
print(ptxt)

s = sign(ctxt, sk, n, M)
v = verify(ptxt, ctxt, pk, n, M)
print(v) 
