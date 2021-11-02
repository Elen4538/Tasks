n = int(input())

1
data = 1 # в этой переменной будут числа от 1 до n*n

count = 0 # для заполнения спирали, при каждой итерации будем увеличивать на один для уменьшения ширины оной (от большого квадрата до малого)

rez = [[0 for i in range(n)] for j in range(n)] 

l = 1

for l in range (1, n*n):
     
    
    for i in range(count, n-count, 1): # верх квадрата заполняется, граница уменьшается на count при каждом прохождении
        rez[count][i] = data
        data += 1
        
    for i in range(count+1, n-count, 1): # правая сторона квадрата
        rez[i][n-count-1] = data
        data += 1
        
    for i in range(n-count-2, count-1, -1): # нижняя сторона квадрата
        rez[n-count-1][i] = data
        data += 1
        
    for i in range(n-2-count,count, -1): # левая сторона квадрата
        rez[i][count] = data
        data += 1
        
    count += 1
      
if n == 1: # небольшой костыль для случая n==1
    print ('1')

else:
    
    for i in range(n):
        for j in range(n):
            print(rez[i][j], end =' ')
        print('')
