# -*- coding: utf-8 -*-
# str = '{0:*>9}'
# str = str.format('ADWA')
# print(str)

import re
import xlrd
import string

NowSheetName = ''
NowSubscript = 0


def SetNowSubscript(Subscript):
   global NowSubscript
   NowSubscript = Subscript
def GetNowSubscript():
   return NowSubscript
   
def SetNowSheetName(name):
   global NowSheetName
   NowSheetName = name
def GetNowSheetName():
   return NowSheetName

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

   sheet=ExcelFile.sheet_by_name('function')

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

class GetExcelConfig(object):
   def __init__(self,path):
      ExcelFile = xlrd.open_workbook(path)
      self.SheetNames= ExcelFile.sheet_names()
      self.ExcelDict = {}
      for sheet_name in self.SheetNames:
         self.ExcelDict[sheet_name] = {}
         sheet = ExcelFile.sheet_by_name(sheet_name)
         if(sheet.ncols > 0):
            parameter_list = sheet.row_values(0)
            for i, parameter in enumerate(parameter_list):
               self.ExcelDict[sheet_name][parameter] = sheet.col_values(i)[1:]
      ExcelFile.release_resources()
      del ExcelFile
   def PrintAll(self):
      print('self.ExcelDict = ',self.ExcelDict)


def GreatSourceFile(path,records,excel,encoding):
   try:
      file = open(path, "w", encoding=encoding)  # open file in read mode
   except IOError as message:                   # file open failed
      print("read file error({0}:{1})".format(message, path))
      exit()

   process     = 'normal' # normal/script
   dict        = {}
   CodeBlock   = ''
   for line in records:
      if process == 'normal':
         if '% ' == line[:2]:# when line start is '% ', it is mean: this is a script.
            if ' if ' in line[:5]:
               dict[dict_count] = 'if'
               CodeBlock = line[2:]
            elif ' for ' in line[:6]:
               dict[dict_count] = 'for'
               CodeBlock = line[2:]
            elif ' while ' in line[:8]:
               dict[dict_count] = 'while'
               CodeBlock = line[2:]
            else:
               writeLine    = line
               replaceLists = re.findall(r"\$\{(.+?)\}",writeLine)
               if(len(replaceLists) > 0):
                  for list in replaceLists:
                     temp = string.Template(writeLine)
                     run  = "temp.safe_substitute(%s='%s')"%(list, excel.ExcelDict[GetNowSheetName()][list][GetNowSubscript()])
                     writeLine = eval(run)
               exec(writeLine[2:-1])
         else:
            writeLine    = line
            replaceLists = re.findall(r"\$\{(.+?)\}",writeLine)
            if(len(replaceLists) > 0):
               for list in replaceLists:
                  temp = string.Template(writeLine)
                  run  = "temp.safe_substitute(%s='%s')"%(list, excel.ExcelDict[GetNowSheetName()][list][GetNowSubscript()])
                  writeLine = eval(run)
            file.writelines(writeLine)
      elif process == 'script':

         pass
      else:
         print('process\'s value is fault')
   file.close()

def AutomaticCode():
   import os
   import sys
   print('Start: automatic programming code for [gpio]')
   sys.path.append(r'%s\\Source\\Extend\\Driver\\gpio\\Template\\'%os.getcwd()) # add config file path to system path
   import gpio_config
   TemplateFile = []
   Project_gpio_config = GetExcelConfig(gpio_config.Config['config'])
   LoadTemplate(gpio_config.Config['template'],TemplateFile,'utf-8')
   GreatSourceFile(gpio_config.Config['target'],TemplateFile,Project_gpio_config,'utf-8')
   print('Completed: automatic programming code for [gpio]')
   
if __name__ == '__main__':
   AutomaticCode()
