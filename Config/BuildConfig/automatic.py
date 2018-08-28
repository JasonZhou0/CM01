# try:
   # import Config.BuildConfig.path as Path
# except:
   # try:
      # import path as Path
   # except:
      # print('Cannot found "path" module, please check it!')


def AutomaticScript(arg):
   
   if(arg == 'bootloader'):
      print('%s call automatic script gpio_config start!'%arg)
      try:
         import Source.Extend.Driver.gpio.Template.gpio_config as gpio_config
      except:
         try:
            import gpio_config as gpio_config
         except:
            print('Cannot found "gpio_config" module, please check it!')
            exit()
      
            
            
            
      print('%s call automatic script gpio_config completed!'%arg)

   elif(arg == 'application'):
      print('%s call automatic script gpio_config start!'%arg)
      try:
         import Source.Extend.Driver.gpio.Template.gpio_config as gpio_config
      except:
         try:
            import gpio_config as gpio_config
         except:
            print('Cannot found "gpio_config" module, please check it!')
            exit()
      
            
            
            
            
      print('%s call automatic script gpio_config completed!'%arg)
      
   else:
      print('Error: %s is out of range!'%arg)

if __name__ == '__main__':
   AutomaticScript('bootloader')
   AutomaticScript('application')