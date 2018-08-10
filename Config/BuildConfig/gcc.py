# gnu arm toolchain must be already in system path

CompileToolBacePath  = 'Tools\\gcc-arm-none-eabi\\bin\\'
BOOT_TargetPath      = 'Build\\Bootloader\\obj\\'
BOOT_OutPath         = 'Build\\Bootloader\\bin\\'
BOOT_OutName         = 'BOOT_TestCode'
BOOT_Out             = BOOT_OutPath+BOOT_OutName
APP_TargetPath       = 'Build\\Application\\obj\\'
APP_OutPath          = 'Build\\Application\\bin\\'
APP_OutName          = 'APP_TestCode'
APP_Out              = APP_OutPath+APP_OutName

# Compile tool path define
BOOT_CompileToolPath = {
   'AR':CompileToolBacePath+'arm-none-eabi-ar',
   'AS':CompileToolBacePath+'arm-none-eabi-as',
   'CC':CompileToolBacePath+'arm-none-eabi-gcc',
   'CXX':CompileToolBacePath+'arm-none-eabi-g++',
   'LINK':CompileToolBacePath+'arm-none-eabi-g++',
   'RANLIB':CompileToolBacePath+'arm-none-eabi-ranlib',
   'OBJCOPY':CompileToolBacePath+'arm-none-eabi-objcopy',
   'PROGSUFFIX':'.elf',
}
APP_CompileToolPath = BOOT_CompileToolPath

# compile flags
BOOT_CCFLAGS = [
   '-mcpu=cortex-m4',
   '-mthumb',
   # '-interwork',
   '-Wfatal-errors',
   '-Wall',
   '-Wextra',
   # '-mfloat-abi=hard',
   # '-mfpu=fpv4-sp-d16',
   '-g3',
   # '-M',
   '-C',
   '-O0',
   '-fsigned-char',
   '-ffunction-sections',
   '-fdata-sections',
   '-std=gnu11',
   '-fmessage-length=0',
   ]
APP_CCFLAGS = BOOT_CCFLAGS

# link flags
BOOT_LINKFLAGS = [
   '-mcpu=cortex-m4',
   '-mthumb',
   '-TConfig\\LinkerFile\\STM32F407VETx_FLASH_BOOT.ld',
   '-ffunction-sections',
   '-fdata-sections',
   '-mfloat-abi=hard',
   # '-mfloat-abi=soft',
   '-Xlinker',
   '-Map',
   '-Xlinker',
   BOOT_Out+'.map',
   '-Xlinker',
   '--gc-sections',
   '--specs=nano.specs',
   ]
APP_LINKFLAGS = [
   '-mcpu=cortex-m4',
   '-mthumb',
   '-TConfig\\LinkerFile\\STM32F407VETx_FLASH_APP.ld',
   '-ffunction-sections',
   '-fdata-sections',
   '-mfloat-abi=hard',
   # '-mfloat-abi=soft',
   '-Xlinker',
   '-Map',
   '-Xlinker',
   APP_Out+'.map',
   '-Xlinker',
   '--gc-sections',
   '--specs=nano.specs',
   ]
   