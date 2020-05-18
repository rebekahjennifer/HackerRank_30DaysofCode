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
"The first line contains an integer, , denoting the number of entries in the phone book.Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line.
