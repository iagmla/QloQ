#include <stdlib.h>
#include <string.h>
#include <termios.h>
#include <openssl/bn.h>
#include "pki/qloqRSA.c"

int main(int argc, char *argv[]) {
    if (argc != 5) {
        exit(1);
    }
    char *pkfilenameA = argv[1];
    char *skfilenameA = argv[2];
    char *pkfilenameB = argv[3];
    char *skfilenameB = argv[4];
    unsigned char *msg;
    msg = "Hello World!";
    struct qloq_ctx Actx;
    struct qloq_ctx ASctx;
    struct qloq_ctx Bctx;
    struct qloq_ctx BSctx;
    load_pkfile(pkfilenameA, &Actx, &ASctx);
    load_skfile(skfilenameA, &Actx, &ASctx);
    load_pkfile(pkfilenameB, &Bctx, &BSctx);
    load_skfile(skfilenameB, &Bctx, &BSctx);
    BIGNUM *msg_BN;
    BIGNUM *ctxt;
    BIGNUM *ptxt;
    BIGNUM *S;
    msg_BN = BN_new();
    ctxt = BN_new();
    ptxt = BN_new();
    S = BN_new();
    BN_bin2bn(msg, 12, msg_BN);
    cloak(&Actx, ctxt, msg_BN);
    decloak(&Actx, ptxt, ctxt);
    printf("Running...\n");
    if (BN_cmp(ptxt, msg_BN) == 0) {
        printf("Encryption successful!\n");
    }
    sign(&BSctx, S, ctxt);
    if (verify(&BSctx, S, ctxt) == 0) {
        printf("Signing successful!\n");
    }
}
