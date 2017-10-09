def fibo(n):
    x = 0
    y = 0
    z = 1
    while x < n:
        yield z
        
        y, z = z, z + y
    
        x += 1
    return 'done'
            
                  
            
