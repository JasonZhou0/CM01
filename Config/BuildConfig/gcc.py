import os

CompileToolPath   = 'Tools\\gcc-arm-none-eabi\\bin\\'

# Compile path define
AR                = CompileToolPath+'arm-none-eabi-ar'
AS                = CompileToolPath+'arm-none-eabi-as'
CC                = CompileToolPath+'arm-none-eabi-gcc'
CXX               = CompileToolPath+'arm-none-eabi-g++'
LINK              = CompileToolPath+'arm-none-eabi-g++'     # predefined is 'arm-none-eabi-gcc'
RANLIB            = CompileToolPath+'arm-none-eabi-ranlib'
OBJCOPY           = CompileToolPath+'arm-none-eabi-objcopy'
PROGSUFFIX        = '.elf'

# Libraries path
   # public
PublicLibPath     = [
   'Tools\\gcc-arm-none-eabi\\arm-none-eabi\\lib\\',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv6-m',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv7e-m',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv7-m',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv8-m.base',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv8-m.main',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv8-m.main\\fpu\\fpv5-d16',
	]
   
   # private