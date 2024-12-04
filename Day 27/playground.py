def add(*args):
    sum=0
    for i in args:
        sum+=i
    return  sum

#print(add(1,5))

def calculate(n,**kwargs):
    print(kwargs)
    #for key,value in kwargs.items()
    # print(key)
    # print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2,add=3,multiply=5)

class car:
    def __init__(self,**kw):
        self.model=kw.get("model")
        self.make=kw["make"]

my_car=car(model="Gtr",make="Nissan")

print(my_car.make)
