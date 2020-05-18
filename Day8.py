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
