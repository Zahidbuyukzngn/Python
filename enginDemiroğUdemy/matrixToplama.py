matrix1=[[4,9,11],
         [0,1,1],
         [2,2,5]]

matrix2=[[1,2,3],
         [4,5,6],
         [7,8,9]]

toplam=[[0,0,0],
        [0,0,0],
        [0,0,0],]

#matrix toplama
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        toplam[i][j]=matrix1[i][j]+matrix2[i][j]

print(f"{toplam[0]}\n"+f"{toplam[1]}\n"+f"{toplam[2]}")
      