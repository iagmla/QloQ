from qloq import keygen, encrypt, decrypt, sign, verify
from Crypto.Util import number

psize = 64
skA, pkA, nA, MA = keygen(psize)
skB, pkB, nB, MB = keygen(psize)
msg = 65
ctxt = encrypt(msg, pkB, nB, MB)
print(ctxt)
ptxt = decrypt(ctxt, skB, nB, MB)
print(ptxt)

s = sign(ctxt, skA, nA, MA)
v = verify(s, ctxt, pkA, nA, MA)
print(v) 
