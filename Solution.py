a = input("Enter two comma separated no. : ")
x, y = a.split(",")
x = int(x)
y = int(y)
list2 = []
for i in range(x):
    list1 = []
    for j in range(y):
        list1.append(i*j)
    print(list1)
