import random

print("Привет, мой друг ! \n Я сейчас загадаю чисило от 0 до 100 , А ты введи свое и посмотрим угадаешь ли ты? (у тебя 8 попыток)")
n=1
compute_chisel=random.randint(0,100)
print("Число загадано! Попытка №1:")
while n < 9:
    chislo=int(input())
    if compute_chisel==chislo:
        print("Вы победили!")
        break
    elif compute_chisel>chislo:
        print("Не правильно! Загаданное число больше!")
    elif compute_chisel<chislo:
        print("Не правильно! Загаданное число меньше")
    n=n+1
    print("Попытка №", n)
else:
    print("Вы проиграли")


