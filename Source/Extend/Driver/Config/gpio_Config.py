# -*- coding: utf-8 -*-

import string

tempTemplate = string.Template("Hello $name,yourwebsiteismessage $message")

print(tempTemplate.substitute(name='gcc',message='http://blog.me115.com'))


str = '{0:*>9}'
str = str.format('')
print(str)

import xlrd

from datetime import date,datetime

def read_excel():

   #文件位置

   ExcelFile=xlrd.open_workbook(r'D:\MyProject\MyProject\CM01\Source\Extend\Driver\Config\gpio_Config.xlsx')

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
   sheet.cell(1,0) = "DWA"
   print(sheet.cell(1,0).value.encode('utf-8'))

   print(sheet.cell_value(1,0).encode('utf-8'))

   print(sheet.row(1)[0].value.encode('utf-8'))

   #打印单元格内容格式

   print(sheet.cell(1,0).ctype)

if __name__ == '__main__':
   read_excel()