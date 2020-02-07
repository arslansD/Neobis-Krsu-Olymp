listx=input("").split()
listx=list(map(int, listx))
for element in range(len(listx)):
    minx=element
    for number in range(element+1, len(listx)):
        if listx[minx] > listx[number]:
            minx=number
    listx[element], listx[minx] = listx[minx], listx[element]
print (listx[0],listx[1],listx[2])
