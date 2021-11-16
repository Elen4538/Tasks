from functools import wraps

def memoized(maxsize=None):
    
    memory = {}
    def memory_func(func):
        @wraps(func)        
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))         
            
            if isinstance(maxsize, int): #словарь ограничен
                            
                if len(memory) < maxsize:#не превышает память
                    
                    if key not in memory:  
                        memory[key] = func(*args, **kwargs)
                        
                    return memory[key]                   
                   
                else: #превышает память
                    
                    if key in memory:
                     
                        return memory[key]
                    else:
                        memory.popitem()
                        memory[key] = func(*args, **kwargs)
                        return memory[key]

            else:                        #словарь не ограничен 
               
                if key not in memory:
                    memory[key] = func(*args, **kwargs)
                return memory[key]
            

        return wrapper

    return memory_func
