''''' 
Showoff features of Pydoc module 
This is easy module to demonstrate docstrings 
'''  
__authors__  = 'Alice & Fred'  
__version__  = 'version 1.10'  
__license__  = 'Copyright...'  
  
class MyClass:  
    ''''' 
    Demonstrate Class Docstrings 
     
    '''  
    def __init__(self, spam=1, eggs=2):  
        ''''' 
        Set the default attributevalues only 
        Keyword arguments: 
        spam - a processed meat product 
        eggs - a fine breakfast for lumberjacks 
        '''  
        self.spam = spam  
        self.eggs = eggs  
  
def square(x):  
    ''''' 
    Square of the param <x> 
    '''  
    return x * x  
