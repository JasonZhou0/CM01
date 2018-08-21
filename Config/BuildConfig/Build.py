import os
import sys

type = sys.version_info.major

MainMenu = {}
MainMenu[0] = {
   'Build bootloader'   :['call build -Q =boot '],
   'Build application'  :['call build -Q =app '],
   'Rebuild bootloader' :['call build -Q =boot =delete '],
   'Rebuild application':['call build -Q =app =delete '],
   'Rebuild all'        :['call build -Q =boot =delete ', 'call build -Q =app =delete '],
   'Clean bootloader'   :['call build -c -Q =boot =delete '],
   'Clean application'  :['call build -c -Q =app =delete '],
   'Clean all'          :['call build -c -Q =boot =delete ', 'call build -c -Q =app =delete '],
   'ELF -> TXT'         :['call build -Q =boot =elf ', 'call build -Q =app =elf ']
   }

while(1):
   print('')
   print('##########################################################')
   print('##                                                      ##')
   print('##                                                      ##')
   print('##               *   Start Construct   *                ##')
   print('##                                                      ##')
   print('##                                                      ##')
   print('##########################################################')
   MenuDepth  = 0
   MenuNumMax = {
      '0':0,
      '1':0,
      }
   CallMenu = {}
   for menu_user in MainMenu[MenuDepth].keys():
      CallMenu[MenuNumMax['%d'%MenuDepth]] = MainMenu[MenuDepth][menu_user]
      if type == 2:
         print [MenuNumMax['%d'%MenuDepth]], menu_user
      elif type == 3:
         print('[%d]'%MenuNumMax['%d'%MenuDepth], '%s'%menu_user)
      MenuNumMax['%d'%MenuDepth] += 1

   InputKey = input('Please enter your option number: ')
   if(InputKey is 'exit'):
      break
   else:
      InputKey = int(InputKey)

   if InputKey < MenuNumMax['%d'%MenuDepth]:
      for cmd in CallMenu[InputKey]:
         os.system(cmd)
   else:
      print('Your input number put of range!')
