import pickle
class Person:
    def __init__(self,name,age,address) -> None:
        self.name=name
        self.age=age
        self.address=address
    def __repr__(self) -> str:
        return f'name:{self.name},age:{self.age},address:{self.address}'
people = [
    Person("niko", 20, "hmd st ostadan"),
    Person("elnaz", 25, "Tehran st ashrafi"),
    Person("sara", 21, "Tehran st Azadi")
]
listPeople=[]
while(True):
    name=input('get name:')
    age=input('get age:')
    address=input('get address:')
    newPerson=Person(name, age, address)
    f=open("file.dat","ab")
    newPerson=pickle.dump(newPerson,f)
    listPeople.append(newPerson)
    goAhead=input("do you want countinu?[Y,N] ")
    if goAhead=='N':
        f.close()
        break