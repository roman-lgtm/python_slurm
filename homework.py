def matrix(self,rows,numbers):
    number=1
    for i in range(rows):
        for j in range(numbers):
            print(number,end=" ")
            number+=1
            print()

def treugolnik():
    number=1
    n=int(input())
    for i in range (1,n+1):
        for j in range (i):
            print (number,end=" ")
            number+=1
        print()

def obt_treugolnik(n):
    number=n
    #n=number=int(input())
    for i in range (n-1):
        for j in range (i):
            print(number,end=" ")
            number-=1
        print()
obt_treugolnik(5)