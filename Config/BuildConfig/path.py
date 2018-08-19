import os

WorkSpace         = os.getcwd()+'\\'
SourceBasePath    = 'Source\\'


BOOT_TargetPath   = 'Build\\Bootloader\\obj\\'
BOOT_OutPath      = 'Build\\Bootloader\\bin\\'
BOOT_OutName      = 'BOOT_TestCode'
BOOT_Out          = BOOT_OutPath+BOOT_OutName
BOOT_LD           = 'Config\\LinkerFile\\STM32F407VETx_FLASH_BOOT.ld'
BOOT_Source = {}
BOOT_Source['MCULibraryPath'] = SourceBasePath+'Generic\\Driver\\Mcu\\'
BOOT_Source['DriverPath']		= SourceBasePath+'Generic\\Driver\\'
BOOT_Source['ServicePath']	   = SourceBasePath+'Generic\\Service\\'
BOOT_Source['SupportPath']	   = SourceBasePath+'Generic\\Support\\'
BOOT_Source['PlatformPath']	= SourceBasePath+'Generic\\Platform\\'



APP_TargetPath    = 'Build\\Application\\obj\\'
APP_OutPath       = 'Build\\Application\\bin\\'
APP_OutName       = 'APP_TestCode'
APP_Out           = APP_OutPath+APP_OutName
APP_LD            = 'Config\\LinkerFile\\STM32F407VETx_FLASH_APP.ld'
APP_Source = {}
APP_Source['MCULibraryPath']  = SourceBasePath+'Generic\\Driver\\Mcu\\'
APP_Source['DriverPath']		= SourceBasePath+'Generic\\Driver\\'
APP_Source['ServicePath']	   = SourceBasePath+'Generic\\Service\\'
APP_Source['SupportPath']	   = SourceBasePath+'Generic\\Support\\'
APP_Source['PlatformPath']	   = SourceBasePath+'Generic\\Platform\\'

