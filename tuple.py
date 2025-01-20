a = ("ram","rohit",1,"mohit",20.3,True,"ram")  #0,1,2
print(a)
# print(a[0])
# a[0]="r"  #value not change
# print(a)
# print(type(a))
b= ('ram')
# b=(1,) #int
print(type(b))


#cannot update the values of a tuple
a[0]="pninfosys"
print(a)

tuple1 = (5,10,15,20,25)
tuple1 = tuple1 +(8,9,"h")
print(tuple1)
print(tuple1[5])