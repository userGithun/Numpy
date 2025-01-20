a = (1,3,4,6,7,1,1,3,3,3,4,5,2,1,1)
# print(a.count(1))
print(a.index(3))
# a[0] =12
# print(a)

#Tuple update

x = ("apple","banana","cherry")
y = list(x)
print(y) #list

y[1] ="kiwi"
x = tuple(y)
print(x)

#jion two tuple

tuple1 =('a','b','c')
tuple2 =(1,2,3)

tuple3 = tuple1 + tuple2
print(tuple3)

#multiply Tuple

fruits = ('apple','banana','cherry')
fruits = (2,3,4)
fruits =('a','b')

mytuple = fruits * 3
print(mytuple)