import os

Path={}

if __name__ == '__main__':
   WorkSpace = os.path.abspath('..\\..')+'\\'
else:
   WorkSpace = os.getcwd()+'\\'
   
Path['bootloader'] = {
   'WorkSpace'       :WorkSpace,
   'BuildRelativePath':'Build\\bootloader\\',
   'BuildPath'       :WorkSpace+'Build\\bootloader\\',
   'BinPath'         :WorkSpace+'Build\\bootloader\\bin\\',
   'Target'          :WorkSpace+'Build\\bootloader\\bin\\bootloader',
   'TargetName'      :'bootloader',
   'LinkerFile'      :WorkSpace+'Config\\LinkerFile\\STM32F407VETx_FLASH_BOOT.ld',
   'ObjPath'         :WorkSpace+'Build\\bootloader\\obj\\',
   'SourcePath'      :{
      'MCULibraryPath'  :WorkSpace+'Source\\Generic\\Driver\\Mcu\\',
      'DriverPath'      :WorkSpace+'Source\\Generic\\Driver\\',
      'ServicePath'     :WorkSpace+'Source\\Generic\\Service\\',
      'SupportPath'     :WorkSpace+'Source\\Generic\\Support\\',
      'PlatformPath'    :WorkSpace+'Source\\Generic\\Platform\\',
      }
   }

Path['application'] = {
   'WorkSpace'       :WorkSpace,
   'BuildRelativePath':'Build\\application\\',
   'BuildPath'       :WorkSpace+'Build\\application\\',
   'BinPath'         :WorkSpace+'Build\\application\\bin\\',
   'Target'          :WorkSpace+'Build\\application\\bin\\application',
   'TargetName'      :'application',
   'LinkerFile'      :WorkSpace+'Config\\LinkerFile\\STM32F407VETx_FLASH_APP.ld',
   'ObjPath'         :WorkSpace+'Build\\application\\obj\\',
   'SourcePath'      :{
      'MCULibraryPath'  :WorkSpace+'Source\\Generic\\Driver\\Mcu\\',
      'DriverPath'      :WorkSpace+'Source\\Generic\\Driver\\',
      'ServicePath'     :WorkSpace+'Source\\Generic\\Service\\',
      'SupportPath'     :WorkSpace+'Source\\Generic\\Support\\',
      'PlatformPath'    :WorkSpace+'Source\\Generic\\Platform\\',
      }
   }

if __name__ == '__main__':
   import os
   print(Path)
   os.system('pause')



# WorkSpace         = os.getcwd()+'\\'
# SourceBasePath    = 'Source\\'


# BOOT_TargetPath   = 'Build\\Bootloader\\obj\\'
# BOOT_OutPath      = 'Build\\Bootloader\\bin\\'
# BOOT_OutName      = 'BOOT_TestCode'
# BOOT_Out          = BOOT_OutPath+BOOT_OutName
# BOOT_LD           = 'Config\\LinkerFile\\STM32F407VETx_FLASH_BOOT.ld'
# BOOT_Source = {}
# BOOT_Source['MCULibraryPath'] = SourceBasePath+'Generic\\Driver\\Mcu\\'
# BOOT_Source['DriverPath']		= SourceBasePath+'Generic\\Driver\\'
# BOOT_Source['ServicePath']	   = SourceBasePath+'Generic\\Service\\'
# BOOT_Source['SupportPath']	   = SourceBasePath+'Generic\\Support\\'
# BOOT_Source['PlatformPath']	= SourceBasePath+'Generic\\Platform\\'



# APP_TargetPath    = 'Build\\Application\\obj\\'
# APP_OutPath       = 'Build\\Application\\bin\\'
# APP_OutName       = 'APP_TestCode'
# APP_Out           = APP_OutPath+APP_OutName
# APP_LD            = 'Config\\LinkerFile\\STM32F407VETx_FLASH_APP.ld'
# APP_Source = {}
# APP_Source['MCULibraryPath']  = SourceBasePath+'Generic\\Driver\\Mcu\\'
# APP_Source['DriverPath']		= SourceBasePath+'Generic\\Driver\\'
# APP_Source['ServicePath']	   = SourceBasePath+'Generic\\Service\\'
# APP_Source['SupportPath']	   = SourceBasePath+'Generic\\Support\\'
# APP_Source['PlatformPath']	   = SourceBasePath+'Generic\\Platform\\'

