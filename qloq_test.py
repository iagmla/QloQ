from qloq import keygen, encrypt, decrypt, sign, verify
from Crypto.Util import number

sk, pk, n, M = keygen(512)
msg = 65
ctxt = encrypt(msg, pk, n, M)
print(ctxt)
ptxt = decrypt(ctxt, sk, n, M)
print(ptxt)

s = sign(ctxt, sk, n, M)
v = verify(s, ctxt, pk, n, M)
print(v) 
