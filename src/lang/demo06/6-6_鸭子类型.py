class Animal(object):
    def eat(self):
        print("动物吃东西")

class Cat(Animal):
    def eat(self):
        print("猫吃鱼")

class Dog(Animal):
    def eat(self):
        print("狗吃骨头")

class Person(object):
    def eat(self):
        print("人吃五谷杂粮")


def eatFun(obj):
    obj.eat()

eatFun(Cat())
eatFun(Dog())
eatFun(Animal())

# 动态语言 鸭子类型
eatFun(Person())
