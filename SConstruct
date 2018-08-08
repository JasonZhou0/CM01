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
    '#Source\\Generic\\Driver\\Mcu\\Libraries\\CMSIS\\Include',
    '#Source\\Generic\\Driver\\Mcu\\Libraries\\CMSIS\\Device\\ST\\STM32F4xx\\Include',
    '#Source\\Generic\\Driver\\Mcu\\Libraries\\STM32F4xx_StdPeriph_Driver\\inc',
    ]

# lib files
env.Append(LIBPATH = [
	'Tools\\gcc-arm-none-eabi\\arm-none-eabi\\lib\\',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv6-m',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv7e-m',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv7-m',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv8-m.base',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv8-m.main',
	'Tools\\gcc-arm-none-eabi\\lib\\gcc\\arm-none-eabi\\5.4.1\\armv8-m.main\\fpu\\fpv5-d16',
	])
	
# compiler flags
env.Append(CCFLAGS = [
    '-mcpu=cortex-m4',
    # '-mthumb-interwork',
	'-Wfatal-errors',
	'-Wall',
	'-Wextra',
	'-g3',
	# '-M',
	'-C',
    '-O0',
    '-fsigned-char',
    '-ffunction-sections',
    '-fdata-sections',
    '-mthumb',
    '-std=gnu11',
    '-fmessage-length=0',
	# '-c',
    ])
 
# linker flags
env.Append(LINKFLAGS = [
	'-TTools\\LinkerFile\\stm32_rom.ld',
    # '-ffunction-sections',
    # '-fdata-sections',
    '-Xlinker',
	'-Map',
	'-Xlinker',
	'Build\\bin\\TestCode-ld.map',
	'-Xlinker',
    '--gc-sections',
    '--specs=nano.specs',
    ]) 

# defines
env.Append(CPPDEFINES = [
    'STM32F407xx',
	'__GNUC__',
	'__FPU_PRESENT=1',
	'__FPU_USED=1',
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

# MapEnv = env.Clone(LINKFLAGS = [
	# '-TTools\\LinkerFile\\stm32_rom.ld',
	# '-Map=Build\\bin\\TestCode-ld.map',
	# ],
	# PROGSUFFIX = [
	# '.elf'
	# ],
	# LINK =[
	# 'Tools\\gcc-arm-none-eabi\\bin\\arm-none-eabi-ld',
	# ],)
	
# MapEnv.Program(
    # target = 'Build\\bin\\TestCode-ld',
    # source = FILELIST,
	# )

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
