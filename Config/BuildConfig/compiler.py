try:
   import Config.BuildConfig.path as Path
except:
   try:
      import path as Path
   except:
      print('Cannot found "path" module, please check it!')
      exit(main())
# gnu arm toolchain must be already in system path

BuildMode      = 'debug'
CompilerTool   = 'gcc'
Compiler       = {}
CompileToolBacePath  = 'Tools\\gcc-arm-none-eabi\\bin\\'
# bootloader
Compiler['bootloader']={
   'ARCH'      :'arm',
   'CPU'       :'cortex-m4',
   
   'AR'        :CompileToolBacePath+'arm-none-eabi-ar',
   'AS'        :CompileToolBacePath+'arm-none-eabi-as',
   'CC'        :CompileToolBacePath+'arm-none-eabi-gcc',
   'CXX'       :CompileToolBacePath+'arm-none-eabi-g++',
   'LINK'      :CompileToolBacePath+'arm-none-eabi-gcc',
   'SIZE'      :CompileToolBacePath+'arm-none-eabi-size',
   'RANLIB'    :CompileToolBacePath+'arm-none-eabi-ranlib',
   'OBJDUMP'   :CompileToolBacePath+'arm-none-eabi-objdump',
   'OBJCOPY'   :CompileToolBacePath+'arm-none-eabi-objcopy',
   'PROGSUFFIX':'.elf',
   }
DEVICE = ' -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard -fsigned-char -std=gnu11 -fmessage-length=0'
Compiler['bootloader']['CCFLAGS']   = DEVICE + ' -ffunction-sections -fdata-sections -Wfatal-errors -Wall -Wextra'
# Compiler['bootloader']['ASFLAGS'] = ' -c' + BOOT_DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '
Compiler['bootloader']['LINKFLAGS'] = DEVICE + ' -flto -Wl,--gc-sections,-Map=%s.map -T %s'%(Path.Path['bootloader']['Target'],Path.Path['bootloader']['LinkerFile'])
if BuildMode == 'debug':
   Compiler['bootloader']['CCFLAGS'] += ' -g -O0'# -gdwarf-2'
   # Compiler['bootloader']['ASFLAGS'].Append = ' -g -gdwarf-2'
else:
   Compiler['bootloader']['CCFLAGS'] += ' -O2'

# application
Compiler['application']={
   'ARCH'      :'arm',
   'CPU'       :'cortex-m4',
   
   'AR'        :CompileToolBacePath+'arm-none-eabi-ar',
   'AS'        :CompileToolBacePath+'arm-none-eabi-as',
   'CC'        :CompileToolBacePath+'arm-none-eabi-gcc',
   'CXX'       :CompileToolBacePath+'arm-none-eabi-g++',
   'LINK'      :CompileToolBacePath+'arm-none-eabi-gcc',
   'SIZE'      :CompileToolBacePath+'arm-none-eabi-size',
   'RANLIB'    :CompileToolBacePath+'arm-none-eabi-ranlib',
   'OBJDUMP'   :CompileToolBacePath+'arm-none-eabi-objdump',
   'OBJCOPY'   :CompileToolBacePath+'arm-none-eabi-objcopy',
   'PROGSUFFIX':'.elf',
   }
DEVICE = ' -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard -fsigned-char -std=gnu11 -fmessage-length=0'
Compiler['application']['CCFLAGS']   = DEVICE + ' -ffunction-sections -fdata-sections -Wfatal-errors -Wall -Wextra'
# Compiler['application']['ASFLAGS'] = ' -c' + BOOT_DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '
Compiler['application']['LINKFLAGS'] = DEVICE + ' -flto -Wl,--gc-sections,-Map=%s.map -T %s'%(Path.Path['application']['Target'],Path.Path['application']['LinkerFile'])
if BuildMode == 'debug':
   Compiler['application']['CCFLAGS'] += ' -g -O0'# -gdwarf-2'
   # Compiler['application']['ASFLAGS'].Append = ' -g -gdwarf-2'
else:
   Compiler['application']['CCFLAGS'] += ' -O2'

if __name__ == '__main__':
   import os
   print(Compiler)
   os.system('pause')


# # toolchains options
# ARCH='arm'
# CPU='cortex-m4'
# CROSS_TOOL='gcc'

# BUILD = 'debug'
# STM32_TYPE = 'STM32F4XX'

# CompileToolBacePath  = 'Tools\\gcc-arm-none-eabi\\bin\\'

# # BOOT

# # Compile tool path define
# BOOT_CompileTool = {
   # 'AR':CompileToolBacePath+'arm-none-eabi-ar',
   # 'AS':CompileToolBacePath+'arm-none-eabi-as',
   # 'CC':CompileToolBacePath+'arm-none-eabi-gcc',
   # 'CXX':CompileToolBacePath+'arm-none-eabi-g++',
   # 'LINK':CompileToolBacePath+'arm-none-eabi-gcc',
   # 'SIZE':CompileToolBacePath+'arm-none-eabi-size',
   # 'RANLIB':CompileToolBacePath+'arm-none-eabi-ranlib',
   # 'OBJDUMP':CompileToolBacePath+'arm-none-eabi-objdump',
   # 'OBJCOPY':CompileToolBacePath+'arm-none-eabi-objcopy',
   # 'PROGSUFFIX':'.elf',
# }
# BOOT_DEVICE = '  -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard -fsigned-char -std=gnu11 -fmessage-length=0'

# BOOT_CompileTool['CCFLAGS']      = BOOT_DEVICE + ' -ffunction-sections -fdata-sections -Wfatal-errors -Wall -Wextra' # -DSTM32F407ZG -DSTM32F4XX -DUSE_STDPERIPH_DRIVER -D__ASSEMBLY__ -D__FPU_USED'

# # BOOT_CompileTool['ASFLAGS']      = ' -c' + BOOT_DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '

# BOOT_CompileTool['LINKFLAGS']    = BOOT_DEVICE + ' -flto -Wl,--gc-sections,-Map=%s.map -T %s'%(path.BOOT_Out,path.BOOT_LD)

# if BUILD == 'debug':
   # BOOT_CompileTool['CCFLAGS']   += ' -g -O0'# -gdwarf-2'
   # # BOOT_CompileTool['ASFLAGS']   += ' -g -gdwarf-2'
# else:
   # BOOT_CompileTool['CCFLAGS'] += ' -O2'

# BOOT_CompileTool['TargetPath']   = path.BOOT_TargetPath
# BOOT_CompileTool['OutPath']      = path.BOOT_OutPath
# BOOT_CompileTool['OutName']      = path.BOOT_OutName
# BOOT_CompileTool['Out']          = path.BOOT_Out

# # APP

# # Compile tool path define
# APP_CompileTool = {
   # 'AR':CompileToolBacePath+'arm-none-eabi-ar',
   # 'AS':CompileToolBacePath+'arm-none-eabi-as',
   # 'CC':CompileToolBacePath+'arm-none-eabi-gcc',
   # 'CXX':CompileToolBacePath+'arm-none-eabi-g++',
   # 'LINK':CompileToolBacePath+'arm-none-eabi-gcc',
   # 'SIZE':CompileToolBacePath+'arm-none-eabi-size',
   # 'RANLIB':CompileToolBacePath+'arm-none-eabi-ranlib',
   # 'OBJDUMP':CompileToolBacePath+'arm-none-eabi-objdump',
   # 'OBJCOPY':CompileToolBacePath+'arm-none-eabi-objcopy',
   # 'PROGSUFFIX':'.elf',
# }
# APP_DEVICE = '  -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard -fsigned-char -std=gnu11 -fmessage-length=0'

# APP_CompileTool['CCFLAGS']      = APP_DEVICE + ' -ffunction-sections -fdata-sections -Wfatal-errors -Wall -Wextra' # -DSTM32F407ZG -DSTM32F4XX -DUSE_STDPERIPH_DRIVER -D__ASSEMBLY__ -D__FPU_USED'

# # APP_CompileTool['ASFLAGS']      = ' -c' + APP_DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '

# APP_CompileTool['LINKFLAGS']    = APP_DEVICE + ' -flto -Wl,--gc-sections,-Map=%s.map -T %s '%(path.APP_Out,path.APP_LD)#-Ttext %x 0x08003000

# if BUILD == 'debug':
   # APP_CompileTool['CCFLAGS']   += ' -g -O0'# -gdwarf-2'
   # # APP_CompileTool['ASFLAGS']   += ' -g -gdwarf-2'
# else:
   # APP_CompileTool['CCFLAGS'] += ' -O2'

# APP_CompileTool['TargetPath']   = path.APP_TargetPath
# APP_CompileTool['OutPath']      = path.APP_OutPath
# APP_CompileTool['OutName']      = path.APP_OutName
# APP_CompileTool['Out']          = path.APP_Out
   