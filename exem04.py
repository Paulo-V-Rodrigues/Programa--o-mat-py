num = int(input('digite um número:'))
for i in range (1, num+1):


 if i % 3 == 0 and i % 5 == 0:
    print(f'FizzBuzz', end= '') 
 elif i % 3 == 0:
     print(f'Fizz', end= '')
 elif i % 5 == 0:
     print(f'Buzz', end= '')
 
else:
    print(i, end= '')
    
    
    
   