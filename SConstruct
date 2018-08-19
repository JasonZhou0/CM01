import os
import sys
import Config.BuildConfig.gcc       as Compiler
import Config.BuildConfig.include   as Include
import Config.BuildConfig.define    as Define
import Config.BuildConfig.library   as Lib
import Config.BuildConfig.path   	as path
# import shutil
# # delete folder "Build" and all files
# if os.path.exists('Build'):
	# shutil.rmtree('Build')

env  = Environment(ENV = os.environ)
env['CCCOMSTR']    = "Compiling $TARGET"
env['LINKCOMSTR']  = "Linking $TARGET"

CmdOptions = sys.argv

def GetAllObject():
   AllObject = []
   AllSConscript = []
   for source_path in path.BOOT_Source.values():
      for dirpath, dirnames, filenames in os.walk(source_path):
         if ("SConscript" in filenames):
            SConscript_path_file = os.path.join(dirpath,"SConscript")
            if SConscript_path_file not in AllSConscript:
               AllSConscript.append(SConscript_path_file)
               O = SConscript([SConscript_path_file])
               if O not in AllObject:
                  AllObject+=O
   return AllObject
   
# build all
if ('=bootloader' in CmdOptions or '=Bootloader' in CmdOptions or '=Boot' in CmdOptions or '=BOOT' in CmdOptions or '=boot' in CmdOptions):
   if '=delete' in CmdOptions or '=Delete' in CmdOptions:
      print('Start delete \'Build\\Bootloader\' floder...')
      import shutil
      # delete folder "Build\\Bootloader" and all files
      if os.path.exists('Build\\Bootloader'):
         shutil.rmtree('Build\\Bootloader')
      print('Complete delete \'Build\\Bootloader\' floder.')
   print('Start build bootloader...')
   env['BUILD']  = "bootloader"
   # Compiler
   for name in Compiler.BOOT_CompileTool.keys():
      env['%s'%name] = Compiler.BOOT_CompileTool['%s'%name]

   # work space path
   env['WorkSpace']   = path.WorkSpace

   # project defines
   env['CPPDEFINES']  = Define.BOOT_CPPDEFINES

   # lib file paths
   env['LIBPATH']     = Lib.BOOT_LIBPATH

   # lib files
   env['LIB']         = Lib.BOOT_LIB

   # include file paths
   env['CPPPATH']     = Include.BOOT_CPPPATH

   # Export Environment
   print('env: ',env)
   Export('env')
   
   Object = GetAllObject()
   
   prg = env.Program( target = env['Out'], source = Object, )
   
   if '=ELF' in CmdOptions or '=Elf' in CmdOptions or '=elf' in CmdOptions:
      POST_ACTION = ' Tools\\ELF\\elfdump.exe %s > %s.txt'%(prg[0], prg[0])
      env.AddPostAction(prg, POST_ACTION)
   
   if '=size' in CmdOptions or '=Size' in CmdOptions or '=SIZE' in CmdOptions:
      POST_ACTION = env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(prg[0], env['Out']) + env['SIZE'] + ' %s \n'%prg[0]\
                  + env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(prg[0], env['Out'])   + env['SIZE'] + ' %s \n'%prg[0]\
                  + env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(prg[0], env['Out'])  + env['SIZE'] + ' %s \n'%prg[0]
   else:
      POST_ACTION = env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(prg[0], env['Out']) \
                  + env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(prg[0], env['Out'])   \
                  + env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(prg[0], env['Out'])
   
   env.AddPostAction(prg, POST_ACTION)
   
elif ('=application' in CmdOptions or '=Application' in CmdOptions or '=App' in CmdOptions or '=APP' in CmdOptions or '=app' in CmdOptions):
   if '=delete' in CmdOptions or '=Delete' in CmdOptions:
      print('Start delete \'Build\\Application\' floder...')
      import shutil
      # delete folder "Build\\Application" and all files
      if os.path.exists('Build\\Application'):
         shutil.rmtree('Build\\Application')
      print('Complete delete \'Build\\Application\' floder.')
   print('Start build application...')
   env['BUILD']  = "application"
   # Compiler
   for name in Compiler.APP_CompileTool.keys():
      env['%s'%name] = Compiler.APP_CompileTool['%s'%name]

   # work space path
   env['WorkSpace']   = path.WorkSpace

   # project defines
   env['CPPDEFINES']  = Define.APP_CPPDEFINES

   # lib file paths
   env['LIBPATH']     = Lib.APP_LIBPATH

   # lib files
   env['LIB']         = Lib.APP_LIB

   # include file paths
   env['CPPPATH']     = Include.APP_CPPPATH

   # Export Environment
   print('env: ',env)
   Export('env')
   
   Object = GetAllObject()
   
   prg = env.Program( target = env['Out'], source = Object, )
   
   if '=ELF' in CmdOptions or '=Elf' in CmdOptions or '=elf' in CmdOptions:
      POST_ACTION = ' Tools\\ELF\\elfdump.exe %s > %s.txt'%(prg[0], prg[0])
      env.AddPostAction(prg, POST_ACTION)
   
   if '=size' in CmdOptions or '=Size' in CmdOptions or '=SIZE' in CmdOptions:
      POST_ACTION = env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(prg[0], env['Out']) + env['SIZE'] + ' %s \n'%prg[0]\
                  + env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(prg[0], env['Out'])   + env['SIZE'] + ' %s \n'%prg[0]\
                  + env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(prg[0], env['Out'])  + env['SIZE'] + ' %s \n'%prg[0]
   else:
      POST_ACTION = env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(prg[0], env['Out']) \
                  + env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(prg[0], env['Out'])   \
                  + env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(prg[0], env['Out'])
   
   env.AddPostAction(prg, POST_ACTION)
   
else:
   print('Build failed! Please let me known what do you want to build, bootloader or application?')
