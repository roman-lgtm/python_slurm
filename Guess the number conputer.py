from random import randint

print("Введи свое число жалкий смертный")
human_chislo=int(input())
low=0
high=100
n=0

while n < 8:
    n+=1
    computer_chislo=randint(low,high)
    print("Попытка №",n,"Твое число - это",computer_chislo)
    help=str(input())
    if help=="=":
        print("Ура, я победил!!")
        break
    elif help=="-":
        high=computer_chislo-1
    elif help=="+":
        low=computer_chislo+1
else:
    print("Я проиграл, вонючий человек")


