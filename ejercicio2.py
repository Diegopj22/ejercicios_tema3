matriz=[[0,0,0],[0,0,0],[0,0,0]]

def rellenar(n):
    for x in range(n):
        for y in range(n):
            matriz[x][y]=float(input('valor de ['+str(x)+'['+ str(y)+')='))