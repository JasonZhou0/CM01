import os

def GetAllObject(Source):
	Object = []
	for dirpath, dirnames, filenames in os.walk(Source):
		#for filename in filenames:
			if ("SConscript" in filenames):
				SConscript_path_file = os.path.join(dirpath,"SConscript")
				Object += SConscript([SConscript_path_file])
	return Object
   
def GetAllObjectPath(Object):
	ObjectPath = ''
	for path in Object:
		ObjectPath = os.path.join(ObjectPath+' ',str(path))
	return ObjectPath