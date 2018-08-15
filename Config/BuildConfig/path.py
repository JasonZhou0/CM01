BOOT_TargetPath   = 'Build\\Bootloader\\obj\\'
BOOT_OutPath      = 'Build\\Bootloader\\bin\\'
BOOT_OutName      = 'BOOT_TestCode'
BOOT_Out          = BOOT_OutPath+BOOT_OutName
BOOT_LD           = 'Config\\LinkerFile\\STM32F407VETx_FLASH_BOOT.ld'

APP_TargetPath    = 'Build\\Application\\obj\\'
APP_OutPath       = 'Build\\Application\\bin\\'
APP_OutName       = 'APP_TestCode'
APP_Out           = APP_OutPath+APP_OutName
APP_LD            = 'Config\\LinkerFile\\STM32F407VETx_FLASH_APP.ld'

SourceBasePath    = 'Source\\'
MCULibraryPath	   = SourceBasePath+'Generic\\Driver\\Mcu\\'
DriverPath		   = SourceBasePath+'Generic\\Driver\\'
ServicePath	      = SourceBasePath+'Generic\\Service\\'
SupportPath	      = SourceBasePath+'Generic\\Support\\'
PlatformPath	   = SourceBasePath+'Generic\\Platform\\'