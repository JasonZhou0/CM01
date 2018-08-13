# gnu arm toolchain must be already in system path

# toolchains options
ARCH='arm'
CPU='cortex-m4'
CROSS_TOOL='gcc'

BUILD = 'debug'
STM32_TYPE = 'STM32F4XX'


CompileToolBacePath  = 'Tools\\gcc-arm-none-eabi\\bin\\'

BOOT_TargetPath      = 'Build\\Bootloader\\obj\\'
BOOT_OutPath         = 'Build\\Bootloader\\bin\\'
BOOT_OutName         = 'BOOT_TestCode'
BOOT_Out             = BOOT_OutPath+BOOT_OutName
BOOT_LD              = 'Config\\LinkerFile\\STM32F407VETx_FLASH_BOOT.ld'

APP_TargetPath       = 'Build\\Application\\obj\\'
APP_OutPath          = 'Build\\Application\\bin\\'
APP_OutName          = 'APP_TestCode'
APP_Out              = APP_OutPath+APP_OutName
APP_LD               = 'Config\\LinkerFile\\STM32F407VETx_FLASH_APP.ld'

# BOOT

# Compile tool path define
BOOT_CompileTool = {
   'AR':CompileToolBacePath+'arm-none-eabi-ar',
   'AS':CompileToolBacePath+'arm-none-eabi-gcc',
   'CC':CompileToolBacePath+'arm-none-eabi-gcc',
   'CXX':CompileToolBacePath+'arm-none-eabi-g++',
   'LINK':CompileToolBacePath+'arm-none-eabi-gcc',
   'SIZE':CompileToolBacePath+'arm-none-eabi-size',
   'RANLIB':CompileToolBacePath+'arm-none-eabi-ranlib',
   'OBJDUMP':CompileToolBacePath+'arm-none-eabi-objdump',
   'OBJCOPY':CompileToolBacePath+'arm-none-eabi-objcopy',
   'PROGSUFFIX':'.elf',
}
BOOT_DEVICE = '  -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard -fsigned-char -ffunction-sections -fdata-sections -std=gnu11 -fmessage-length=0'

BOOT_CompileTool['CCFLAGS']      = BOOT_DEVICE + ' -g -Wfatal-errors -Wall -Wextra' # -DSTM32F407VE -DSTM32F4XX -DUSE_STDPERIPH_DRIVER -D__ASSEMBLY__ -D__FPU_USED'

BOOT_CompileTool['ASFLAGS']      = ' -c' + BOOT_DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '

BOOT_CompileTool['LINKFLAGS']    = BOOT_DEVICE + ' -lm -lgcc -lc' + ' -nostartfiles -Wl,--gc-sections,-Map=%s.map,-cref,-u,Reset_Handler -T %s'%(BOOT_Out,BOOT_LD)

if BUILD == 'debug':
   BOOT_CompileTool['CCFLAGS']   += ' -O0 -gdwarf-2'
   BOOT_CompileTool['ASFLAGS']   += ' -gdwarf-2'
else:
   BOOT_CompileTool['CCFLAGS'] += ' -O2'

BOOT_CompileTool['TargetPath']   = BOOT_TargetPath
BOOT_CompileTool['OutPath']      = BOOT_OutPath
BOOT_CompileTool['OutName']      = BOOT_OutName
BOOT_CompileTool['Out']          = BOOT_Out


# APP

# Compile tool path define
APP_CompileTool = {
   'AR':CompileToolBacePath+'arm-none-eabi-ar',
   'AS':CompileToolBacePath+'arm-none-eabi-gcc',
   'CC':CompileToolBacePath+'arm-none-eabi-gcc',
   'CXX':CompileToolBacePath+'arm-none-eabi-g++',
   'LINK':CompileToolBacePath+'arm-none-eabi-gcc',
   'SIZE':CompileToolBacePath+'arm-none-eabi-size',
   'RANLIB':CompileToolBacePath+'arm-none-eabi-ranlib',
   'OBJDUMP':CompileToolBacePath+'arm-none-eabi-objdump',
   'OBJCOPY':CompileToolBacePath+'arm-none-eabi-objcopy',
   'PROGSUFFIX':'.elf',
}
APP_DEVICE = '  -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard -fsigned-char -ffunction-sections -fdata-sections -std=gnu11 -fmessage-length=0'

APP_CompileTool['CCFLAGS']      = APP_DEVICE + ' -g -Wfatal-errors -Wall -Wextra' # -DSTM32F407ZG -DSTM32F4XX -DUSE_STDPERIPH_DRIVER -D__ASSEMBLY__ -D__FPU_USED'

APP_CompileTool['ASFLAGS']      = ' -c' + APP_DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '

APP_CompileTool['LINKFLAGS']    = APP_DEVICE + ' -lm -lgcc -lc' + ' -nostartfiles -Wl,--gc-sections,-Map=%s.map,-cref,-u,Reset_Handler -T %s'%(APP_Out,APP_LD)

if BUILD == 'debug':
   APP_CompileTool['CCFLAGS']   += ' -O0 -gdwarf-2'
   APP_CompileTool['ASFLAGS']   += ' -gdwarf-2'
else:
   APP_CompileTool['CCFLAGS'] += ' -O2'

APP_CompileTool['TargetPath']   = APP_TargetPath
APP_CompileTool['OutPath']      = APP_OutPath
APP_CompileTool['OutName']      = APP_OutName
APP_CompileTool['Out']          = APP_Out
   