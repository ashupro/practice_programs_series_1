def rev_string(string):
    rev=""
    for i in string:
        rev=i+rev
    print("reverse of a string is",rev)
    if(string==rev):
        print("string is a palindrome")
    else:
        print("string is not a palindrome")


str=input("enter a string ")
rev_string(str)