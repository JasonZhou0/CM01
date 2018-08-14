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
for name in Compiler.BOOT_CompileTool.keys():
   BOOT_env['%s'%name] = Compiler.BOOT_CompileTool['%s'%name]

for name in Compiler.APP_CompileTool.keys():
   APP_env['%s'%name] = Compiler.APP_CompileTool['%s'%name]

# work space path
BOOT_env['WorkSpace']   = os.getcwd()+'\\'

APP_env['WorkSpace']    = os.getcwd()+'\\'

# project defines
BOOT_env['CPPDEFINES']  = Define.BOOT_CPPDEFINES

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


def GetAllObject(source):
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

def GetAllObjectPath(Object):
	ObjectPath = ''
	for path in Object:
		ObjectPath = os.path.join(ObjectPath+' ',str(path))
	return ObjectPath


BOOT_POST_ACTION = BOOT_env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(BOOT_prg[0], BOOT_env['Out']) + BOOT_env['SIZE'] + ' %s \n'%BOOT_prg[0] \
            + BOOT_env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(BOOT_prg[0], BOOT_env['Out']) + BOOT_env['SIZE'] + ' %s \n'%BOOT_prg[0] \
            + BOOT_env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(BOOT_prg[0], BOOT_env['Out']) + BOOT_env['SIZE'] + ' %s \n'%BOOT_prg[0] \
            + ' Tools\\ELF\\elfdump.exe %s > %s.txt'%(BOOT_prg[0], BOOT_prg[0])
            
BOOT_env.AddPostAction(BOOT_prg, BOOT_POST_ACTION)

APP_POST_ACTION = APP_env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(APP_prg[0], APP_env['Out']) + APP_env['SIZE'] + ' %s \n'%APP_prg[0] \
            + APP_env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(APP_prg[0], APP_env['Out']) + APP_env['SIZE'] + ' %s \n'%APP_prg[0] \
            + APP_env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(APP_prg[0], APP_env['Out']) + APP_env['SIZE'] + ' %s \n'%APP_prg[0] \
            + ' Tools\\ELF\\elfdump.exe %s > %s.txt'%(APP_prg[0], APP_prg[0])
APP_env.AddPostAction(APP_prg, APP_POST_ACTION)
