import os
import Config.BuildConfig.gcc       as Compiler
import Config.BuildConfig.include   as Include
import Config.BuildConfig.define    as Define
import Config.BuildConfig.library   as Lib

# import shutil
# # delete folder "Build" and all files
# if os.path.exists('Build'):
	# shutil.rmtree('Build')

# Great Environment
BOOT_env  = Environment(ENV = os.environ)
APP_env   = Environment(ENV = os.environ)

# Compiler
BOOT_env['AR']          = Compiler.BOOT_CompileToolPath['AR']
BOOT_env['AS']          = Compiler.BOOT_CompileToolPath['AS']
BOOT_env['CC']          = Compiler.BOOT_CompileToolPath['CC']
BOOT_env['CXX']         = Compiler.BOOT_CompileToolPath['CXX']
BOOT_env['LINK']        = Compiler.BOOT_CompileToolPath['LINK']
BOOT_env['RANLIB']      = Compiler.BOOT_CompileToolPath['RANLIB']
BOOT_env['OBJCOPY']     = Compiler.BOOT_CompileToolPath['OBJCOPY']
BOOT_env['PROGSUFFIX']  = Compiler.BOOT_CompileToolPath['PROGSUFFIX']
BOOT_env['CCFLAGS']     += Compiler.BOOT_CCFLAGS
BOOT_env['LINKFLAGS']   += Compiler.BOOT_LINKFLAGS

APP_env['AR']           = Compiler.APP_CompileToolPath['AR']
APP_env['AS']           = Compiler.APP_CompileToolPath['AS']
APP_env['CC']           = Compiler.APP_CompileToolPath['CC']
APP_env['CXX']          = Compiler.APP_CompileToolPath['CXX']
APP_env['LINK']         = Compiler.APP_CompileToolPath['LINK']
APP_env['RANLIB']       = Compiler.APP_CompileToolPath['RANLIB']
APP_env['OBJCOPY']      = Compiler.APP_CompileToolPath['OBJCOPY']
APP_env['PROGSUFFIX']   = Compiler.APP_CompileToolPath['PROGSUFFIX']
APP_env['CCFLAGS']      += Compiler.APP_CCFLAGS
APP_env['LINKFLAGS']    += Compiler.APP_LINKFLAGS

# work space path
BOOT_env['WorkSpace']   = os.getcwd()
BOOT_env['TargetPath']  = Compiler.BOOT_TargetPath
BOOT_env['OutPath']     = Compiler.BOOT_OutPath
BOOT_env['OutName']     = Compiler.BOOT_OutName
BOOT_env['Out']         = Compiler.BOOT_Out

APP_env['WorkSpace']    = os.getcwd()
APP_env['TargetPath']   = Compiler.APP_TargetPath
APP_env['OutPath']      = Compiler.APP_OutPath
APP_env['OutName']      = Compiler.APP_OutName
APP_env['Out']          = Compiler.APP_Out

# project defines
BOOT_env['CPPDEFINES']  = Define.APP_CPPDEFINES

APP_env['CPPDEFINES']   = Define.APP_CPPDEFINES

# lib file paths
BOOT_env['LIBPATH']     = Lib.BOOT_LIBPATH

APP_env['LIBPATH']      = Lib.APP_LIBPATH

# lib files
BOOT_env['LIB']         = Lib.BOOT_LIB

APP_env['LIB']          = Lib.APP_LIB

# include file paths
BOOT_env['CPPPATH']     = Include.BOOT_CPPPATH

APP_env['CPPPATH']      = Include.APP_CPPPATH

# Export Environment
Export('BOOT_env')
Export('APP_env')


# def CallAllSConscript(dir_name):
	# firt = 0
	# Scon_Object = []
	# for dirpath, dirnames, filenames in os.walk(dir_name):
		# #for filename in filenames:
			# if ("SConscript" in filenames):
				# SConscript_path_file = os.path.join(dirpath,"SConscript")
				# Scon_Object += SConscript([SConscript_path_file])
	# return Scon_Object

def GetAllObject(source):
   Export('BOOT_env')
   B_Object = []
   A_Object = []
   for dirpath, dirnames, filenames in os.walk(source):
      if ("SConscript" in filenames):
         SConscript_path_file = os.path.join(dirpath,"SConscript")
         B,A = SConscript([SConscript_path_file])
         B_Object += B
         A_Object += A
   return B_Object,A_Object

BOOT_Object,APP_Object = GetAllObject(os.getcwd()+'\\Source')

#   CallAllSConscript(BOOT_env['WorkSpace']+'\\Source')

# build everything
BOOT_prg = BOOT_env.Program(
    target = BOOT_env['Out'],
    source = BOOT_Object,
)
APP_prg = APP_env.Program(
    target = APP_env['Out'],
    source = APP_Object,
)

# binary file builder -O ihex
def arm_generator_bin(source, target, env, for_signature):
    return '$OBJCOPY -g -O binary %s %s'%(source[0], target[0])
def arm_generator_hex(source, target, env, for_signature):
    return '$OBJCOPY -g -O ihex %s %s'%(source[0], target[0])
def arm_generator_sre(source, target, env, for_signature):
    return '$OBJCOPY -g -O srec %s %s'%(source[0], target[0])
BOOT_env.Append(BUILDERS = {
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
APP_env.Append(BUILDERS = {
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

def GetAllObjectPath(Object):
	ObjectPath = ''
	for path in Object:
		ObjectPath = os.path.join(ObjectPath+' ',str(path))
	return ObjectPath

BOOT_env.Objcopy_bin(BOOT_prg)
BOOT_env.Objcopy_hex(BOOT_prg)
BOOT_env.Objcopy_sre(BOOT_prg)
APP_env.Objcopy_bin(APP_prg)
APP_env.Objcopy_hex(APP_prg)
APP_env.Objcopy_sre(APP_prg)
