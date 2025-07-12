import sys

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
    number=6
    #n=number=int(input())
    for i in range (n,0,-1):
        print("" * (n - i), end=" ")
        for j in range (i):
            print(number,end=" ")
            number-=1
        print()

def my_range(stop: float, start: float = 0.0, step: float =1.0):
    result=start
    li=[]

    while result<stop:
        li.append(result)
        result = result + step

def my_rangerator(stop: float, start: float = 0.0, step: float =1.0):
    result=start
    while (result<stop):
        yield result
        result += step


