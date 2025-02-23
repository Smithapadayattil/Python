list=[5,9,12,48,63,6,56,32,1,68]
for i in range(0,len(list)):
       for j in range(i+1,len(list)):
        if list[i]>=list[j]:
            list[i],list[j]=list[j],list[i]
print(list)





