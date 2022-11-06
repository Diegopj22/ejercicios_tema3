matriz=[[0,0,0],[0,0,0],[0,0,0]]

def rellenar(n):
    for x in range(n):
        for y in range(n):
            matriz[x][y]=float(input('valor de ['+str(x)+'['+ str(y)+')='))

def sarrus (n):
    for z in range (n-1):
        for x in range (1,n-z):
            if (matriz[z][z]!=0):
                p = matriz[x+z][z]/matriz[z][z]
                for y in range(n):
                    matriz[x+z][y]= matriz[x+z][y]-(matriz[z][y]*p)

def determinante(n):
    deter=1
    for x in range (n):
      deter = matriz[x][x]*deter
    print('\n El determinante de la matriz es =',deter)

n=3
rellenar(n)
sarrus(n)
determinante(n)