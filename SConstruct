import os
import sys
import Config.BuildConfig.compiler  as Compiler
import Config.BuildConfig.include   as Include
import Config.BuildConfig.define    as Define
import Config.BuildConfig.library   as Lib
import Config.BuildConfig.path   	as Path
# import shutil
# # delete folder "Build" and all files
# if os.path.exists('Build'):
	# shutil.rmtree('Build')

base_env  = Environment(ENV = os.environ)
   
<<<<<<< HEAD
class ConstructTarget(object):
   def __init__(self,name,env,arg):
      self.name = name
      self.env  = env
      self.arg  = arg
   def GetConfig(self):
      env = self.env
      env['CCCOMSTR']   = "Compiling $TARGET"
      env['LINKCOMSTR'] = "Linking $TARGET"
      # tool chain
      for name in Compiler.Compiler[self.name].keys():
         env[name] = Compiler.Compiler[self.name][name]
      # files path
      for name in Path.Path[self.name].keys():
         env[name] = Path.Path[self.name][name]
      # define
      env['CPPDEFINES'] = Define.Define[self.name]
      # include
      env['CPPPATH']    = Include.Include[self.name]
      # lib files
      env['LIB']         = Lib.Library[self.name]
      # lib file paths
      env['LIBPATH']     = Lib.LibraryPath[self.name]

      if '=delete' in self.arg or '=Delete' in self.arg:
         print('Start delete %s floder...'%env['BuildRelativePath'])
         import shutil
         # delete folder "Build\\%s"%self.name and all files
         if os.path.exists('%s'%env['BuildRelativePath']):
            shutil.rmtree('%s'%env['BuildRelativePath'])
         print('Complete delete %s floder.'%env['BuildRelativePath'])
      print('Start build %s...'%env['TargetName'])

      Export('env')
      
   def PrintAll(self):
      for item in self.env.Dictionary().items():
         print(item)
      print('Construct target name  : %s'%self.name)
      print('Construct target arg   : %s'%self.arg)
      for object in self.object:
         print('Construct target object: %s'%object)
   def GetObject(self):
      self.object    = []
      AllSConscript  = []
      for source_path in self.env['SourcePath'].values():
         for dirpath, dirnames, filenames in os.walk(source_path):
            if ("SConscript" in filenames):
               SConscript_path_file = os.path.join(dirpath,"SConscript")
               if SConscript_path_file not in AllSConscript:
                  AllSConscript.append(SConscript_path_file)
                  O = SConscript([SConscript_path_file])
                  if O not in self.object:
                     self.object+=O
   def Program(self):
      self.prg = self.env.Program( target = self.env['Target'], source = self.object, )
   def OutPut(self):
      if '=ELF' in self.arg or '=Elf' in self.arg or '=elf' in self.arg:
         POST_ACTION = ' Tools\\ELF\\elfdump.exe %s > %s.txt'%(self.prg[0], self.prg[0])
         self.env.AddPostAction(self.prg, POST_ACTION)
      
      if '=size' in self.arg or '=Size' in self.arg or '=SIZE' in self.arg:
         POST_ACTION = self.env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(self.prg[0], self.env['Target']) + self.env['SIZE'] + ' %s \n'%self.prg[0]\
                     + self.env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(self.prg[0], self.env['Target'])   + self.env['SIZE'] + ' %s \n'%self.prg[0]\
                     + self.env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(self.prg[0], self.env['Target'])  + self.env['SIZE'] + ' %s \n'%self.prg[0]
      else:
         POST_ACTION = self.env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(self.prg[0], self.env['Target']) \
                     + self.env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(self.prg[0], self.env['Target'])   \
                     + self.env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(self.prg[0], self.env['Target'])
      
      self.env.AddPostAction(self.prg, POST_ACTION)

if ('=bootloader' in sys.argv or '=Bootloader' in sys.argv or '=Boot' in sys.argv or '=BOOT' in sys.argv or '=boot' in sys.argv):
   Project = ConstructTarget('bootloader', base_env, sys.argv)
elif ('=application' in sys.argv or '=Application' in sys.argv or '=App' in sys.argv or '=APP' in sys.argv or '=app' in sys.argv):
   Project = ConstructTarget('application', base_env, sys.argv)
Project.GetConfig()
Project.GetObject()
Project.Program()
Project.OutPut()
# Project.PrintAll()








# env  = Environment(ENV = os.environ)
# env['CCCOMSTR']    = "Compiling $TARGET"
# env['LINKCOMSTR']  = "Linking $TARGET"

# CmdOptions = sys.argv

# def GetAllObject():
   # AllObject = []
   # AllSConscript = []
   # for source_path in path.BOOT_Source.values():
      # for dirpath, dirnames, filenames in os.walk(source_path):
         # if ("SConscript" in filenames):
            # SConscript_path_file = os.path.join(dirpath,"SConscript")
            # if SConscript_path_file not in AllSConscript:
               # AllSConscript.append(SConscript_path_file)
               # O = SConscript([SConscript_path_file])
               # if O not in AllObject:
                  # AllObject+=O
   # return AllObject
=======
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
   Export('env')
>>>>>>> ef53921522b7ccaef5c7c48620f2060d83224a82
   
# # build all
# if ('=bootloader' in CmdOptions or '=Bootloader' in CmdOptions or '=Boot' in CmdOptions or '=BOOT' in CmdOptions or '=boot' in CmdOptions):
   # if '=delete' in CmdOptions or '=Delete' in CmdOptions:
      # print('Start delete \'Build\\Bootloader\' floder...')
      # import shutil
      # # delete folder "Build\\Bootloader" and all files
      # if os.path.exists('Build\\Bootloader'):
         # shutil.rmtree('Build\\Bootloader')
      # print('Complete delete \'Build\\Bootloader\' floder.')
   # print('Start build bootloader...')
   # env['BUILD']  = "bootloader"
   # # Compiler
   # for name in Compiler.BOOT_CompileTool.keys():
      # env['%s'%name] = Compiler.BOOT_CompileTool['%s'%name]

   # # work space path
   # env['WorkSpace']   = path.WorkSpace

   # # project defines
   # env['CPPDEFINES']  = Define.Define['bootloader']

   # # lib file paths
   # env['LIBPATH']     = Lib.BOOT_LIBPATH

   # # lib files
   # env['LIB']         = Lib.BOOT_LIB

   # # include file paths
   # env['CPPPATH']     = Include.BOOT_CPPPATH

   # # Export Environment

   # # Export('env')
   
   # Object = GetAllObject()
   
   # prg = env.Program( target = env['Out'], source = Object, )
   
   # if '=ELF' in CmdOptions or '=Elf' in CmdOptions or '=elf' in CmdOptions:
      # POST_ACTION = ' Tools\\ELF\\elfdump.exe %s > %s.txt'%(prg[0], prg[0])
      # env.AddPostAction(prg, POST_ACTION)
   
   # if '=size' in CmdOptions or '=Size' in CmdOptions or '=SIZE' in CmdOptions:
      # POST_ACTION = env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(prg[0], env['Out']) + env['SIZE'] + ' %s \n'%prg[0]\
                  # + env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(prg[0], env['Out'])   + env['SIZE'] + ' %s \n'%prg[0]\
                  # + env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(prg[0], env['Out'])  + env['SIZE'] + ' %s \n'%prg[0]
   # else:
      # POST_ACTION = env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(prg[0], env['Out']) \
                  # + env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(prg[0], env['Out'])   \
                  # + env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(prg[0], env['Out'])
   
<<<<<<< HEAD
   # env.AddPostAction(prg, POST_ACTION)
=======
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
   Export('env')
>>>>>>> ef53921522b7ccaef5c7c48620f2060d83224a82
   
# elif ('=application' in CmdOptions or '=Application' in CmdOptions or '=App' in CmdOptions or '=APP' in CmdOptions or '=app' in CmdOptions):
   # if '=delete' in CmdOptions or '=Delete' in CmdOptions:
      # print('Start delete \'Build\\Application\' floder...')
      # import shutil
      # # delete folder "Build\\Application" and all files
      # if os.path.exists('Build\\Application'):
         # shutil.rmtree('Build\\Application')
      # print('Complete delete \'Build\\Application\' floder.')
   # print('Start build application...')
   # env['BUILD']  = "application"
   # # Compiler
   # for name in Compiler.APP_CompileTool.keys():
      # env['%s'%name] = Compiler.APP_CompileTool['%s'%name]

   # # work space path
   # env['WorkSpace']   = path.WorkSpace

   # # project defines
   # env['CPPDEFINES']  = Define.APP_CPPDEFINES

   # # lib file paths
   # env['LIBPATH']     = Lib.APP_LIBPATH

   # # lib files
   # env['LIB']         = Lib.APP_LIB

   # # include file paths
   # env['CPPPATH']     = Include.APP_CPPPATH

   # # Export Environment

   # Export('env')
   
   # Object = GetAllObject()
   
   # prg = env.Program( target = env['Out'], source = Object, )
   
   # if '=ELF' in CmdOptions or '=Elf' in CmdOptions or '=elf' in CmdOptions:
      # POST_ACTION = ' Tools\\ELF\\elfdump.exe %s > %s.txt'%(prg[0], prg[0])
      # env.AddPostAction(prg, POST_ACTION)
   
   # if '=size' in CmdOptions or '=Size' in CmdOptions or '=SIZE' in CmdOptions:
      # POST_ACTION = env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(prg[0], env['Out']) + env['SIZE'] + ' %s \n'%prg[0]\
                  # + env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(prg[0], env['Out'])   + env['SIZE'] + ' %s \n'%prg[0]\
                  # + env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(prg[0], env['Out'])  + env['SIZE'] + ' %s \n'%prg[0]
   # else:
      # POST_ACTION = env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(prg[0], env['Out']) \
                  # + env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(prg[0], env['Out'])   \
                  # + env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(prg[0], env['Out'])
   
   # env.AddPostAction(prg, POST_ACTION)
   
# else:
   # print('Build failed! Please let me known what do you want to build, bootloader or application?')
