# try:
   # import Config.BuildConfig.path as Path
# except:
   # try:
      # import path as Path
   # except:
      # print('Cannot found "path" module, please check it!')

def fn():
   print('hello world')
def AutomaticScript(arg):
   
   if(arg == 'bootloader'):
      print('%s call automatic script gpio_config start!'%arg)
      # try:
         # import Source.Extend.Driver.gpio.Template.gpio_config as gpio_config
      # except:
         # try:
            # import gpio_config as gpio_config
         # except:
            # print('Cannot found "gpio_config" module, please check it!')
            # exit()
      import sys
      
      
      func_name = fn.__name__
      fn_obj = getattr(sys.modules[__name__], func_name)
            # 根据函数名（func_name），获得函数对象
      fn_obj()
                  # hello world
       

       

      print(sys.modules[__name__])
          # <module ‘__main__‘ from ‘**/test.py‘>
            
            
            
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