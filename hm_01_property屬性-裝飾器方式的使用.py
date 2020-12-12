class Student(object):
    def __init__(self):
        # 私有屬性
        self.__age = 0

    @property #當對象調用age屬性的時候會執行下面的方法
    def age(self):
        print("獲取屬性！！")
        return self.__age

    @age.setter #當對象調用age屬性設置值的時候會調用下面的方法
    def age(self, new_age):
        print("獲取屬性！！")
        if new_age >= 0 and new_age <= 130:
            self.__age = new_age
        else:
            print("太老了")

#  使用裝飾器方式的 property屬性那麼方法名要保持一致

student = Student()
age = student.age
print(age)

student.age = 201
age = student.age
print(age)



