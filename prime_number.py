print("enter the num ")
num=int(input())
if num>1:
    for i in range(2,num):
        if(num%i==0):
            print("the num is not prime")
            break
    else:
            print("the num is prime")
else:
    print("the num is not prime")