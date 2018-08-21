#include <stdio.h>
#include "mcu.h"
// #include "Generic\Driver\Display\display.h"

void RTC_Alarm_IRQHandler(void)
{
   while(1);
}
void TIM1_CC_IRQHandler(void)
{
   while(1);
}
unsigned char test_value;
float test_fvalue;
int main(void)
{
   mcu_McuInit();
   // Display();

   while (1)
   {
      test_value = 1;
      test_value = 2;
      test_value *= 3;
      test_value /= 2;
      test_fvalue = 3.2*test_value;
      test_fvalue = 5.2*test_value;
      //arm_sqrt_f32(0.2, &test_fvalue);
   }
   return test_value;
}
