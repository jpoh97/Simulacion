

b1 = [1,2,3,5,5]
b2 = [6,7,5,4,5]
#b3 = [val for val in b1 if val in b2]
cont = 0
i =0
print(b1.__len__())
while(i < b1.__len__()):
    if(b1[i] == b2[i]):
        cont = cont+1
    i = i+1

print(cont)