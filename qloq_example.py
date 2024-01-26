from qloq import keygen, encrypt, decrypt, sign, verify
from Crypto.Util import number

psize = 128
skA, pkA, nA, MA = keygen(psize)
skB, pkB, nB, MB = keygen(psize)
msg = 65
ctxt = encrypt(msg, pkA, nA, MA)
print(ctxt)
ptxt = decrypt(ctxt, skA, nA, MA)
print(ptxt)

s = sign(ctxt, skA, nA, MA)
v = verify(s, ctxt, pkA, nA, MA)
print(v) 
