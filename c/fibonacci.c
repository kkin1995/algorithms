#include <stdio.h>
#include <stdlib.h>

void print_fibonacci(int N) {
    FILE *f = fopen("fibonacci.dat", "w");
    int i = 0;
    int j = 1;
    int temp;
    printf("%d\n", i);
    fprintf(f, "%d\n", i);
    while (j <= N) {
        printf("%d\n", j);
        fprintf(f, "%d\n", j);
        temp = j;
        j = i + j;
        i = temp;
    }
    fclose(f);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Usage: Requires 1 command line argument. ./fibonacci [N]\n");
        exit(1);
    }
    int N = atoi(argv[1]);
    print_fibonacci(N);
}