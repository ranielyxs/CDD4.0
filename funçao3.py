"""for x in range(1, 6):
   for y in range(1,x+1):
        print(str(x)*x)
        """
"""def exercicio_1(n):
    for i in range(1,n+1):
        print(str(i)*i)

exercicio_1(5)
exercicio_1(10)
"""

"""def exercicio_1(n):
    for i in range(1,n+1):
        print(str(i)*i)
        
print(exercicio_1(5))"""

def exercio_2(n):
    for y in range(1,n+1):
        for i in range(1,y):
            print(i,end=" ")
exercio_2(5)
