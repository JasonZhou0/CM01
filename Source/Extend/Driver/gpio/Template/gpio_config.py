# -*- coding: utf-8 -*-

# import string

# tempTemplate = string.Template("Hello $name,yourwebsiteismessage $message")

# print(tempTemplate.substitute(name='gcc',message='http://blog.me115.com'))
import re

str = '{0:*>9}'
str = str.format('ADWA')
print(str)

import xlrd

from datetime import date,datetime

def read_excel():

   #文件位置

   ExcelFile=xlrd.open_workbook(r'D:\MyProject\MyProject\CM01\Source\Extend\Driver\gpio\Template\gpio_config.xlsx')

   #获取目标EXCEL文件sheet名

   print(ExcelFile.sheet_names())

   #------------------------------------

   #若有多个sheet，则需要指定读取目标sheet例如读取sheet2

   # sheet2_name=ExcelFile.sheet_names()[1]

   #------------------------------------

   #获取sheet内容【1.根据sheet索引2.根据sheet名称】

   #sheet=ExcelFile.sheet_by_index(1)

   sheet=ExcelFile.sheet_by_name('GPIO')

   #打印sheet的名称，行数，列数

   print(sheet.name,sheet.nrows,sheet.ncols) 

   #获取整行或者整列的值

   rows1=sheet.row_values(0)#第一行内容
   rows2=sheet.row_values(1)#第二行内容
   cols=sheet.col_values(1)#第二列内容

   print(rows1,rows2,cols)

   #获取单元格内容
   # sheet.cell(1,0) = "DWA"
   print(sheet.cell(1,0).value.encode('utf-8'))

   print(sheet.cell_value(1,0).encode('utf-8'))

   print(sheet.row(1)[0].value.encode('utf-8'))

   #打印单元格内容格式

   print(sheet.cell(1,0).ctype)

# records is a list
def LoadTemplate(path,records,encoding):
   try:
     file = open(path, "r", encoding=encoding)  # open file in read mode
   except IOError as message:                   # file open failed
     print("read file error({0}:{1})".format(message, path))
     exit()
   lines = file.readlines()
   for line in lines:
     records.append(line)
   file.close()

# def GreatSourceFile(path,records,encoding):
   # try:
      # file = open(path, "w", encoding=encoding)  # open file in read mode
   # except IOError as message:                   # file open failed
      # print("read file error({0}:{1})".format(message, path))
      # exit()
   # import string
   # for line in records:
      # print(line)
      # tempLine = string.Template(line)
      # print(tempLine)
      # writeLine = tempLine.substitute(GPIOx='GPIOA',PINx='PIN1')
      # print(writeLine)
      # if '%' == writeLine[0]:
         # writeLine = writeLine[1:-1]
         # exec(writeLine)
         # pass
      # else:
         # file.writelines(writeLine)
   # file.close()
   

class GetExcelConfig(object):
   def __init__(self,source):
      import xlrd
      self.ExcelFile       = xlrd.open_workbook(source)
      self.functionSheet   = self.ExcelFile.sheet_by_name('function')
      # self.rowsNum   = 
      # self.colsNum   = 
   def PrintAll(self):
      print('self.ExcelFile = ',self.ExcelFile)
      print('self.ExcelFile.sheet_names() = ',self.ExcelFile.sheet_names())
      print('self.functionSheet.name = ',self.functionSheet.name)
      print('self.functionSheet.nrows = ',self.functionSheet.nrows)
      print('self.functionSheet.ncols = ',self.functionSheet.ncols)
      # print('self.rowsNum = ',self.rowsNum)
      
Project_gpio_config = GetExcelConfig('D:\MyProject\MyProject\CM01\Source\Extend\Driver\gpio\Template\gpio_config.xlsx')

print('test',Project_gpio_config.functionSheet.nrows)
Project_gpio_config.PrintAll()
gpio_template = []
LoadTemplate('D:\MyProject\MyProject\CM01\Source\Extend\Driver\gpio\Template\gpio_template.c',gpio_template,'utf-8')
for line in gpio_template:
   if '%' == line[0]:
      print(line)

def GreatSourceFile(path,records,encoding):
   try:
      file = open(path, "w", encoding=encoding)  # open file in read mode
   except IOError as message:                   # file open failed
      print("read file error({0}:{1})".format(message, path))
      exit()
   import string
   process     = 'normal' # normal/script
   dict        = {}
   CodeBlock   = ''
   for line in records:
      if process == 'normal':
         if '% ' == line[:2]:# when line start is '% ', it is mean: this is a script.
            if ' if ' in line[:5]:
               dict[dict_count] = 'if'
            elif ' for ' in line[:6]:
               dict[dict_count] = 'for'
            elif ' while ' in line[:8]:
               dict[dict_count] = 'while'
            else:
               replaceLists = re.findall(r"\$\{(.+?)\}",line)
               if(len(replaceLists)):
                  pass
               exec(line[2:])
         else:
            writeLine = line
            replaceLists = re.findall(r"\$\{(.+?)\}",line)
            if(len(replaceLists) > 0):
               for list in replaceLists:
                  temp = string.Template(writeLine)
                  run = 'temp.safe_substitute(%s=\'GPIOA\')'%(list)
                  writeLine = eval(run)
            file.writelines(writeLine)
      elif process == 'script':
         
         pass
      else:
         print('process\'s value is fault')
      # print(line)
      # tempLine = string.Template(line)
      # print(tempLine)
      # writeLine = tempLine.substitute(GPIOx='GPIOA',PINx='PIN1')
      # print(writeLine)
      # if '% ' == writeLine[0]:
         # writeLine = writeLine[1:-1]
         # if ('for' in writeLine[:5]) or ('if' in writeLine[:5]) or ('while' in writeLine[:5]):
            # exec(writeLine)
               # pass
         # else:
         # exec(writeLine)
         # pass
      # else:
         # file.writelines(writeLine)
   file.close()
      
      
GreatSourceFile('D:\MyProject\MyProject\CM01\Source\Extend\Driver\gpio\gpio.c',gpio_template,'utf-8')



# if __name__ == '__main__':
   # read_excel()