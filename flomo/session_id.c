#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char ALPHANUMERIC[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const int BASE = 62;

char* encode_timestamp(unsigned long timestamp) {
    char *encoded = (char*)malloc(12);
    int index = 0;

    do {
        int rem = timestamp % BASE;
        encoded[index++] = ALPHANUMERIC[rem];
        timestamp /= BASE;
    } while (timestamp > 0);

    for (int i = 0; i < index/2; i++) {
        char temp = encoded[i];
        encoded[i] = encoded[index - i - 1];
        encoded[index - i - 1] = temp;
    }

    encoded[index] = '\0';
    return encoded;
}

unsigned long decode_timestamp(const char* encoded) {
    unsigned long timestamp = 0;
    size_t length = strlen(encoded);

    for (size_t i = 0; i < length; i++) {
        char *ptr = strchr(ALPHANUMERIC, encoded[i]);
        if (ptr) {
            int index = ptr - ALPHANUMERIC;
            timestamp = timestamp * BASE + index;
        }
    }

    return timestamp;
}
