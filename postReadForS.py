import random
import csv
from xml.dom import minidom

# from Module.Student import Student
from Module.Student import Student
a = random.randint(1,100)
# print a
print a

n = input("input(1,100)")

# print n
while a!=n:
    if a>n:
        n = input("input(1,100)")
    elif a<n:
        n = input("input(1,100)")

print "win"

sum = 0
for i in range(11):
    sum += i
print sum
# print 1+2+3+4+5+6+7+8+9+10

stu = Student('xiaoHong',"shanghai")

lines = open("personinfo.txt","r").readlines()
print lines

for line in lines:
     print line.split(",")[0]


fo = open("personinfo.txt","a")
fo.write("xiaoZhang,20,chengdu\n")
fo.close()



