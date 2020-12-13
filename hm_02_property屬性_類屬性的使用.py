class Student(object):
    def __init__(self):
        # 私有屬性
        self.__age = 0
    
    def get_age(self):
        print("獲取屬性！！")
        return self.__age

    
    def set_age(self, new_age):
        print("獲取屬性！！")
        if new_age >= 0 and new_age <= 130:
            self.__age = new_age
        else:
            print("太老了")
    # 1.get_age表示獲取屬性的時候執行的方法
    # 2.set_age表示設置屬性的時候執行的方法
    age = property(get_age, set_age)

#  使用裝飾器方式的 property屬性那麼方法名要保持一致

student = Student()
age = student.age
print(age)

student.age = 201
age = student.age
print(age)



