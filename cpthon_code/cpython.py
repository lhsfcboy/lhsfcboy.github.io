from ctypes import *
great_module = cdll.LoadLibrary('./great_module.dll')
print great_module.great_function(13)
