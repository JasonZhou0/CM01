#include <stdio.h>

// #include "Generic\Driver\Display\display.h"

// void _exit(void)
// {
//    while(1);
// }
unsigned char test_value;
float test_fvalue;
int main(void)
{
   // Display();

   while (1)
   {
      test_value = 1;
      test_value = 2;
      test_value *= 3;
      test_value /= 2;
      test_fvalue = 3.2*test_value;
      test_fvalue = 5.2*test_value;
   }
   return test_value;
}
