a = 0
with open("practice.txt","r") as n:
    data = n.read()
    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            a += 1

print(a)

