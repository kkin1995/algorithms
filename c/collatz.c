#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int collatz_step(int n) {
    if (n % 2 == 0) {
        return n / 2;
    }
    else {
        return 3*n + 1;
    }
}

void print_collatz_numbers(int start) {
    printf("Number = %d\n", start);
    while (start > 1) {
        start = collatz_step(start);
        printf("Number = %d\n", start);
    }
}

int count_no_of_steps(int start) {
    int no_of_steps = 0;
    while (start > 1) {
        start = collatz_step(start);
        no_of_steps++;
    }
    return no_of_steps;
}

void print_no_of_steps(int last_number) {
    FILE *f = fopen("steps_taken_by_collatz_no.dat", "w");
    fprintf(f, "Number\tSteps\n");
    for (int i = 1; i <= last_number; i++) {
        int no_of_steps = count_no_of_steps(i);
        fprintf(f, "%d\t%d\n", i, no_of_steps);
        printf("Number of Steps taken for %d is %d\n", i, no_of_steps);
    }
    fclose(f);
}

int main(int argc, char **argv) {

    time_t now1, now2;

    if (argc < 2) {
        printf("Requires 2 Command Line Arguments\n");
        printf("Usage: ./collatz [FLAG](--start, --print-steps) [START / LAST_NUMBER]\n");
        exit(1);
    }
    char* flag = argv[1];
    if (strcmp(flag,  "--start") == 0) {
        int start = atoi(argv[2]);
        time(&now1);
        print_collatz_numbers(start);
        time(&now2);
        printf("Time Taken = %.4f seconds\n", difftime(now2, now1));
    }
    else if (strcmp(flag, "--print-steps") == 0) {
        int last_number = atoi(argv[2]);
        time(&now1);
        print_no_of_steps(last_number);
        time(&now2);
        printf("Time Taken = %.4f seconds\n", difftime(now2, now1));
    }
}