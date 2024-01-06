'''
for i in range(0,10):
    for j in range(0,i+1):
        print(i,end=" ")
    print()      
n=5  

  
for i in range(0,n):
    for j in range(0,i+1):
        a='*'
        print(a)
    print()        

              
n = 5
for i in range(0, n):
	for j in range(0, i+1):
		print("*", end=" ")
	print()  
 
 '''
 
''' 
n=10 
for i in range(n):
    for j in range(0,i+1):
        print("*", end=" ")
    print("  ",end="\n")    '''
    
n=int(input("Enter No:"))
sum=0
for i in range(n):
    sum=sum+int(i)
print(sum)    