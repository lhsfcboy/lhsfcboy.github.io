#include <stdio.h>
#define SQUARE(x) ((x)*(x))


int main(void) {
   int a = 1;
   printf("a++_1:              %i\n"
          "SQUARE(a++):        %i\n"
          "a++_2:              %i\n",a++,SQUARE(a++),a++);
   return 0;
}
