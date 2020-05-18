n = int(input())
phoneBook = dict()

for i in range(n):
    name, number = input().split()
    phoneBook[name] = number
 
for i in range(n):
    try:
        name = input()
        if name in phoneBook:
            print(name + "=" +phoneBook[name])
        else:
            print("Not found")
    except:
        break
#The first line contains an integer,denoting the number of entries in the phone book.
#Each of the  subsequent lines describes an entry in the form of 2 space-separated values on a single line.
#The first value is a friend's name, and the second value is an 8-digit phone number.
#After the  lines of phone book entries, there are an unknown number of lines of queries. 
#Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.
#On a new line for each query, print Not found if the name has no corresponding entry in the phone book; 
#otherwise, print the full name and phonenumber in the format name=phoneNumber.

#I am using exception handling here in this python program
#Exceptions indicate conditions that an application should try to catch
#Exception handling makes your program robust (handling unexpected termination and unexpected actions) helps to prevent potential failure

