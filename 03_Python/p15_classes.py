#define a new class
class Point():
    #Função __init__ inicializa uma instância da classe Point() sempre que ela for chamada
        #Argumento self é utilizado em funções que operam nos próprios objetos e são utilizados pra referenciarem a si
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

#Create a new point
p1 = Point(2,8)
#Access a value inside the point created
print(p1.x)
print(p1.y)

p2 = Point(4,3)

print(p2.x)
print(p2.y)