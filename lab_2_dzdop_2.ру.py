a=int(input("a = "))

b=int(input("b = "))

c=int(input("c = "))

if a+b<c or a+c<b or b+c>a :
    print("треугольник существует")
    
elif a!=b and a!=c and b!=c :
    print("треугольник не существует")
    
elif a==b==c:
    print("равносторонний")
    
else:
    print("равнобедренный")
    
    