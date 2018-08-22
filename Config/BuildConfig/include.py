try:
   import Config.BuildConfig.path as Path
except:
   try:
      import path as Path
   except:
      print('Cannot found "path" module, please check it!')
      exit(main())

Include  = {}
# Include path
Include['bootloader'] = [
   Path.Path['bootloader']['WorkSpace']+'Source\\Generic\\Driver\\Mcu\\config\\',
   Path.Path['bootloader']['WorkSpace']+'Source\\Generic\\Driver\\Mcu\\Libraries\\CMSIS\\Include\\',
   Path.Path['bootloader']['WorkSpace']+'Source\\Generic\\Driver\\Mcu\\Libraries\\CMSIS\\Device\\ST\\STM32F4xx\\Include\\',
   Path.Path['bootloader']['WorkSpace']+'Source\\Generic\\Driver\\Mcu\\Libraries\\STM32F4xx_StdPeriph_Driver\\inc\\',
   Path.Path['bootloader']['WorkSpace']+'Source\\Generic\\Driver\\Mcu\\',
   Path.Path['bootloader']['WorkSpace']+'Source\\Generic\\Support\\mcu_common\\',
   
   ]
Include['application'] = [
   Path.Path['application']['WorkSpace']+'Source\\Generic\\Driver\\Mcu\\config\\',
   Path.Path['application']['WorkSpace']+'Source\\Generic\\Driver\\Mcu\\Libraries\\CMSIS\\Include\\',
   Path.Path['application']['WorkSpace']+'Source\\Generic\\Driver\\Mcu\\Libraries\\CMSIS\\Device\\ST\\STM32F4xx\\Include\\',
   Path.Path['application']['WorkSpace']+'Source\\Generic\\Driver\\Mcu\\Libraries\\STM32F4xx_StdPeriph_Driver\\inc\\',
   Path.Path['application']['WorkSpace']+'Source\\Generic\\Driver\\Mcu\\',
   Path.Path['application']['WorkSpace']+'Source\\Generic\\Support\\mcu_common\\',
   
   ]
# End of Include path
