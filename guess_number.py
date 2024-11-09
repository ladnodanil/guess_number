from random import randint as r

number = r(1,100)
print('Угадайте число от 1 до 100')

while True:
    guess = int(input("Введите число: "))

    if(guess < number):
        print('Ваше число меньше того, что загадано.')
    if guess > number:
        # ...выводим сообщение.
        print('Ваше число больше того, что загадано.')
    if guess == number:
        # ...прерываем выполнение программы и...
        break
# ...выводим сообщение.
print('Отличная интуиция! Вы угадали число :')