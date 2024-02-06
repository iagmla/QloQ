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

msg = 123
s = sign(msg, skA, nA, MA)
v = verify(s, msg, pkA, nA, MA)
print(v) 
