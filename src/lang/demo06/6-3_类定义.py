class Test:
    pass

print(id(Test))
print(type(Test))
print(Test)

class ClassDefine:
    # 类属性 所有实例共享 __开头的外部类不能访问
    __privite_var = '私有属性'
    public_var = '外部可访问'

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        return obj

    def __init__(self, instance_var):
        print("构造方法", instance_var)
        # 实例属性
        self.instance_var = instance_var

    def instance_method(self):
        print("实例方法")

    @staticmethod
    def static_method():
        print("静态方法")

    @classmethod
    def class_method(cls):
        print("类方法")

cd1 = ClassDefine('1')
cd2 = ClassDefine('2')
print(ClassDefine.public_var, cd1.public_var, cd2.public_var)
# 通过实例修改类属性会创建同名实例属性，遮蔽类属性
cd1.public_var = '修改了类属性'
print(ClassDefine.public_var)
print(ClassDefine.public_var, cd1.public_var, cd2.public_var)

cd1.dynamic_var = '动态绑定属性'
print(cd1.dynamic_var)

def m():
    print("动态绑定方法")
cd1.dynamic_method = m
cd1.dynamic_method()


print(dir(cd1))
print(cd1._ClassDefine__privite_var)
