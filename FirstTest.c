#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define FILENAME "data.csv"

int main(int argc, char *argv[]) {
    float a = (float)rand() / (float)RAND_MAX;
    float b = (float)rand() / (float)RAND_MAX;
    float c = (float)rand() / (float)RAND_MAX;


    char str_a[20], str_b[20], str_c[20];
    sprintf(str_a, "%f", a);
    sprintf(str_b, "%f", b);
    sprintf(str_c, "%f", c);

}
