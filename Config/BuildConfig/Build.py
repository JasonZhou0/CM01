import os
import sys
import time

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
   print('##',end='',flush=True)
   Data = '>>> Easy Construct <<<'
   Start = 0
   End   = 15
   fill  = ' '
   while(1):
      delay = 0.01
      DataLen = len(Data)
      Offset= Start
      print('%s%s'%(fill,Data),end='',flush=True)
      if(End<Start):
         break
      while(DataLen):
         print('\b',end='',flush=True)
         DataLen-=1
      time.sleep(delay)
      Start+=1
   print('               ##')
   print('##                                                      ##')
   print('##',end='',flush=True)
   Data = '--- Jason Zhou '
   Start = 80
   End   = 38
   fill  = ''
   DataLen = len(Data)
   while(Start):
      print(' ',end='',flush=True)
      Start-=1
   Start = 80
   while(1):
      delay = 0.01
      DataLen = len(Data)
      Offset= Start
      print('%s%s'%(fill,Data),end='',flush=True)
      if(Start<End):
         break
      while(DataLen+1):
         print('\b',end='',flush=True)
         DataLen-=1
      time.sleep(delay)
      Start-=1
   print('  ##')
   print('##########################################################\n')
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
