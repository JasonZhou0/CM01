

# Include path
BOOT_IncludePath = [
   '#Source\\Generic\\Driver\\Mcu\\config\\',
   '#Source\\Generic\\Driver\\Mcu\\Libraries\\CMSIS\\Include\\',
   '#Source\\Generic\\Driver\\Mcu\\Libraries\\CMSIS\\Device\\ST\\STM32F4xx\\Include\\',
   '#Source\\Generic\\Driver\\Mcu\\Libraries\\STM32F4xx_StdPeriph_Driver\\inc\\',
   '#Source\\Generic\\Driver\\Mcu\\',
   '#Source\\Generic\\Support\\mcu_common\\',
   
   ]
APP_IncludePath = BOOT_IncludePath

BOOT_CPPPATH   = BOOT_IncludePath
APP_CPPPATH    = APP_IncludePath
# End of Include path
