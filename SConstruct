# gnu arm toolchain must be already in system path

import os
import shutil

#define out put file .bin or .hex
BUILD_OUT_PUT_FILE = hex


# delete folder "Build"
if os.path.exists('Build'):
	shutil.rmtree('Build')


env = Environment(ENV = os.environ)

env['AR'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-ar'
env['AS'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-as'
env['CC'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-gcc'
env['CXX'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-g++'
env['LINK'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-g++'                # predefined is 'arm-none-eabi-gcc'
env['RANLIB'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-ranlib'
env['OBJCOPY'] = 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-objcopy'
env['PROGSUFFIX'] = '.elf'
env['WorkSpace'] = os.getcwd()

# include locations
env['CPPPATH'] = [
    '#Inc',
    '#Drivers/CMSIS/Include',
    '#Drivers/CMSIS/Device/ST/STM32F4xx/Include',
    '#Drivers/STM32F4xx_HAL_Driver/Inc',
    '#Drivers/STM32F4xx_HAL_Driver/Inc/Legacy',
    ]
 
# compiler flags
env.Append(CCFLAGS = [
    '-mcpu=cortex-m4',
    '-mthumb',
    '-c',
    '-O1',
    '-fsigned-char',
    '-ffunction-sections',
    '-fdata-sections',
    '-std=gnu11',
    '-fmessage-length=0',
    '-mthumb-interwork',
    ])
 
# linker flags
env.Append(LINKFLAGS = [
    '-ffunction-sections',
    '-fdata-sections',
    '-TTools\\LinkerFile\\stm32_rom.ld',
    '-Xlinker',
    '--gc-sections',
    '--specs=nano.specs',
    ]) 
 
# defines
env.Append(CPPDEFINES = [
    'STM32F407xx',
])

# WorkSpace path
#env.Append(WorkSpace = [ os.getcwd() ])

# Export Environment
Export('env')


def FindSConscriptPath(dir_name):
	firt = 0
	Scon_Object = []
	for dirpath, dirnames, filenames in os.walk(dir_name):
		#for filename in filenames:
			if ("SConscript" in filenames):
				SConscript_path_file = os.path.join(dirpath,"SConscript")
				Scon_Object += SConscript([SConscript_path_file])
	return Scon_Object

Object = FindSConscriptPath(os.getcwd()+'\\Source')

# build everything
TARGETNAME = 'Build\\bin\\TestCode'
FILELIST = Object #Glob('*.cpp')
prg = env.Program(
    target = TARGETNAME,
    source = FILELIST
)

# binary file builder -O ihex
if BUILD_OUT_PUT_FILE == bin:
    def arm_generator(source, target, env, for_signature):
        return '$OBJCOPY -O binary %s %s'%(source[0], target[0])
    env.Append(BUILDERS = {
        'Objcopy': Builder(
            generator=arm_generator,
            suffix='.bin',
            src_suffix='.elf'
        )
    })
elif BUILD_OUT_PUT_FILE == hex:
    def arm_generator(source, target, env, for_signature):
        return '$OBJCOPY -O ihex %s %s'%(source[0], target[0])
    env.Append(BUILDERS = {
        'Objcopy': Builder(
            generator=arm_generator,
            suffix='.hex',
            src_suffix='.elf'
        )
    })

env.Objcopy(prg)

