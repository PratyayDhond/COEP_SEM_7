#include<stdio.h>
#include "cipher.h"

int main(int argc, char** argv){
    printf("To update the passkey, edit the file `.encryptKey`\n");
    if(argc > 1){
        char* plaintText = argv[1];
        printf("Encrypted Data = %s\n", Encrypt(plaintText));

        printf("Decrypted Data = %s\n", Decrypt(Encrypt(plaintText)));
    }
    return 0;
}