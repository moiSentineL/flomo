#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char ALPHANUMERIC[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const int BASE = 62;

char *encode_timestamp(unsigned long long timestamp)
{
    char *encoded = (char *)malloc((sizeof(timestamp) * CHAR_BIT + 5) / 6 + 1);
    int index = 0;

    if (timestamp == 0)
    {
        encoded[index++] = ALPHANUMERIC[0];
    }

    do
    {
        int rem = timestamp % BASE;
        encoded[index++] = ALPHANUMERIC[rem];
        timestamp /= BASE;
    } while (timestamp > 0);

    for (int i = 0; i < index / 2; i++)
    {
        char temp = encoded[i];
        encoded[i] = encoded[index - i - 1];
        encoded[index - i - 1] = temp;
    }

    encoded[index] = '\0';
    return encoded;
}

unsigned long long decode_timestamp(const char *encoded)
{
    unsigned long long timestamp = 0;
    size_t length = strlen(encoded);

    for (size_t i = 0; i < length; i++)
    {
        char *ptr = strchr(ALPHANUMERIC, encoded[i]);
        if (ptr)
        {
            int index = ptr - ALPHANUMERIC;
            timestamp = timestamp * BASE + index;
        }
        else
        {
            fprintf(stderr, "Error: Invalid character '%c' in encoded string.\n", encoded[i]);
            return 0;
        }
    }

    return timestamp;
}
