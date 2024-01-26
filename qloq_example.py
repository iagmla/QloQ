from qloq import keygen, encrypt, decrypt, sign, verify
from Crypto.Util import number

skA, pkA, nA, MA = keygen(512)
skB, pkB, nB, MB = keygen(512)
msg = 65
ctxt = encrypt(msg, pkB, nB, MB)
print(ctxt)
ptxt = decrypt(ctxt, skB, nB, MB)
print(ptxt)

s = sign(ctxt, skA, nA, MA)
v = verify(s, ctxt, pkA, nA, MA)
print(v) 
