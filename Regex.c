#include<stdio.h>
#include<stdlib.h>
bool isMatch(char* s, char* p) {
    int i = 0;
    for (i = 0; i < strlen(p); i++) {

        if (*(p + i) == '*')
            *(p + i) = *(p + i - 1);
    }
    for (i = 0; i < strlen(p); i++) {
        if (*(p + i) == '.')
            *(p + i) = *(s + i);
    }
    if (strcmp(p, s) == 0)
        return true;
    else
        return false;
}