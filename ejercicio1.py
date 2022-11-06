def mover_tower(height,from_pole,to_pole,with_pole):
    if height>=1:
        mover_tower(height-1,from_pole,with_pole,to_pole)
        move_disk(from_pole,to_pole)
        mover_tower(height-1,with_pole,to_pole,from_pole)

def move_disk(fp,tp):
    print("moviendo disco de ",fp,"a",tp)

def main():
    discos=3
    mover_tower(discos,"A","B","C")

if __name__=="__main__":
    main()

#Con 74 discos habría que hacer el problema pero tardaría mucho en ejecutarse      
