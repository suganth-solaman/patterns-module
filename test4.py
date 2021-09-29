def inverse_pyrmid():
    s=int(input("enter"))
    s1=s*2
    for i1 in range(s+1,-1,-1):
        for j2 in range(0,s1):
            print(" ",end="")
        s1+=1
        for j1 in range(i1+1,0,-1):
            print("* ",end="")
        print()


def pyramid():
    s=int(input("enter"))
    s1=s*2
    for i1 in range(0,s+1):
        for j2 in range(0, s1):
            print(" ", end="")
        s1-= 1
        for j1 in range(0,i1+1):
            print("- ", end="")
        print()


def diamond():
    s=int(input("enter"))
    s1=s*2
    for i1 in range(0,s+1):
        for j2 in range(0, s1):
            print(" ", end="")
        s1-= 1
        for j1 in range(0,i1+1):
            print("@ ", end="")
        print()
    for i1 in range(s+1,-1,-1):
        for j2 in range(0,s1):
            print(" ",end="")
        s1+=1
        for j1 in range(i1+1,0,-1):
            print("! ",end="")
        print()


def sand_clock():

    s=int(input("enter"))
    s1=s*2

    for i1 in range(s+1,-1,-1):
        for j2 in range(0,s1):
            print(" ",end="")
        s1+=1
        for j1 in range(i1+1,0,-1):
            print("/\ ",end="")
        print()

    for i1 in range(0,s+1):
        for j2 in range(0, s1-2):
            print(" ", end="")
        s1-= 1
        for j1 in range(0,i1+1):
            print("/\ ", end="")
        print()
