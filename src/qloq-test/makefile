CC=gcc
CFLAGS=-O3 -std=c99 -w -lssl -lcrypto -I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib -g
TARGET=qloq-test
KEYGEN=qloq-keygen
all: $(TARGET) $(KEYGEN)

$(TARGET): qloq_test.c
	$(CC) qloq_test.c $(CFLAGS) -o $(TARGET)

$(KEYGEN): qloq_keygen.c
	$(CC) qloq_keygen.c $(CFLAGS) -o $(KEYGEN)

clean:
	$(RM) $(TARGET) $(RM) $(KEYGEN)
