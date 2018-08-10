# lib file paths
BOOT_LIBPATH = [
   'Tools\\gcc-arm-none-eabi\\arm-none-eabi\\lib\\',
   'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1',
   'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv6-m',
   'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv7e-m',
   'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv7-m',
   'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv8-m.base',
   'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv8-m.main',
   'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv8-m.main\\fpu\\fpv4-sp-d16',
   ]
APP_LIBPATH = BOOT_LIBPATH

BOOT_LIB = []
APP_LIB  = BOOT_LIB