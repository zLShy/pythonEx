class Student():
    def __init__(self,name,city):
        self.name = name
        self.city = city
        print ("My name is %s and from %s" %(name,city))


stu = Student('xiaoming','beijing')