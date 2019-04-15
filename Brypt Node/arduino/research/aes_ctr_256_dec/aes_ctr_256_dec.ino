#include <Crypto.h>
#include <AES.h>
#include <CTR.h>

#define HASH_SIZE 32

byte ctxt[44] = {0x09, 0xf1, 0xe4, 0x64, 0x98, 0x3a, 0x7d, 0x25, 0x30, 0x5d, 0x5b,
                 0x86, 0x53, 0x86, 0xe4, 0x77, 0xae, 0xc3, 0x59, 0x54, 0xfc, 0x08,
                 0x79, 0xce, 0xbf, 0xe9, 0xbd, 0x04, 0x13, 0x27, 0x07, 0x7c, 0x21,
                 0xfb, 0xc9, 0x60, 0x80, 0x7c, 0x86, 0x6c, 0xad, 0x02, 0x85, 0xb5};

void aes256_dec(byte *key, byte *iv, byte *buffer){
  CTR<AES256> aes_ctr_256;
  memset(buffer, 0x00, 128);

  crypto_feed_watchdog();
  aes_ctr_256.setKey(key, 32);
  aes_ctr_256.setIV(iv, 16);
  aes_ctr_256.setCounterSize(4);
  aes_ctr_256.decrypt(buffer, ctxt, 44);
}

void setup() {}

void loop() {
  byte key256[] = "01234567890123456789012345678901";
  byte iv[] = "0123456789012345";
  byte buffer[128];

	while(1){
    aes256_dec(key256, iv, buffer);
	}
}
