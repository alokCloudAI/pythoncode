try:
    a = int(input('enetr the first number'))
    b = int(input('enetr the second number'))
    
    c = a/b
    
    print(c)
    
except Exception as e:
    print(e)
    
else:
    print(c)
    
finally:
    print('i will be exce anyways')