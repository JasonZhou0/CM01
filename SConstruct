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
	'#Tools\\gcc-arm-none-eabi\\arm-none-eabi\\lib\\',
    ]

# lib files
env.Append(LIBPATH = [
	'Tools\\gcc-arm-none-eabi\\arm-none-eabi\\lib\\',
	'Tools\\gcc-arm-none-eabi\\lib\gcc\\arm-none-eabi\\5.4.1'
	])
	
# compiler flags
env.Append(CCFLAGS = [
    '-mcpu=cortex-m4',
    '-mthumb',
	'-Wfatal-errors',
	'-Wall',
	'-Wextra',
    '-c',
	'-g',
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
	'-TTools\\LinkerFile\\stm32_rom.ld',
    '-ffunction-sections',
    '-fdata-sections',
    '-Xlinker',
    '--gc-sections',
    '--specs=nano.specs',
    ]) 

# defines
env.Append(CPPDEFINES = [
    'STM32F407xx',
])

# Export Environment
Export('env')


def CallAllSConscript(dir_name):
	firt = 0
	Scon_Object = []
	for dirpath, dirnames, filenames in os.walk(dir_name):
		#for filename in filenames:
			if ("SConscript" in filenames):
				SConscript_path_file = os.path.join(dirpath,"SConscript")
				Scon_Object += SConscript([SConscript_path_file])
	return Scon_Object

Object = CallAllSConscript(os.getcwd()+'\\Source')

# build everything
TARGETNAME = 'Build\\bin\\TestCode-g++'
FILELIST = Object #Glob('*.cpp')
prg = env.Program(
    target = TARGETNAME,
    source = FILELIST,
)

MapEnv = env.Clone(LINKFLAGS = [
	'-TTools\\LinkerFile\\stm32_rom.ld',
	'-Map=Build\\bin\\TestCode-ld.map',
	],
	PROGSUFFIX = [
	'.elf'
	],
	CXX = [
	'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-ld',
	],
	LINK =[
	'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-ld',
	],)
	
MapEnv.Program(
    target = 'Build\\bin\\TestCode-ld',
    source = FILELIST,
	)

# binary file builder -O ihex
def arm_generator_bin(source, target, env, for_signature):
    return '$OBJCOPY -g -O binary %s %s'%(source[0], target[0])
def arm_generator_hex(source, target, env, for_signature):
    return '$OBJCOPY -g -O ihex %s %s'%(source[0], target[0])
def arm_generator_sre(source, target, env, for_signature):
    return '$OBJCOPY -g -O srec %s %s'%(source[0], target[0])
env.Append(BUILDERS = {
    'Objcopy_bin': Builder(
        generator=arm_generator_bin,
        suffix='.bin',
        src_suffix='.elf'
    ),
    'Objcopy_hex': Builder(
        generator=arm_generator_hex,
        suffix='.hex',
        src_suffix='.elf'
    ),
    'Objcopy_sre': Builder(
        generator=arm_generator_sre,
        suffix='.sre',
        src_suffix='.elf'
    ),
})

def CheckObjectPath(Object):
	ObjectPath = ''
	for path in Object:
		ObjectPath = os.path.join(ObjectPath+' ',str(path))
	return ObjectPath

env.Objcopy_bin(prg)
env.Objcopy_hex(prg)
env.Objcopy_sre(prg)
