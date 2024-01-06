
x=0
print(id(x))

y=6
print(id(y))


a=1+2j
#print(a,"a is complex")
print(isinstance(a,complex))

a=10

#if isinstance(a,int):
if type(a)==int :
    print("yes")
else:
    print("no")    