import string

tempTemplate = string.Template("Hello $name,yourwebsiteismessage $message")

print(tempTemplate.substitute(name='gcc',message='http://blog.me115.com'))


str = '{0:*>9}'
str = str.format('')
print(str)
