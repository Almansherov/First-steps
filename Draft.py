#1 - Пользователь вводит два числа. Одно присваивается одной переменной, а второе - другой. Необходимо поменять значения переменных так,
# чтобы значение первой оказалось во второй, а второй - в первой.
#2 - Вводятся три целых числа. Определить какое из них наибольшее.
#3 - Найти сумму и произведение цифр, введенного натурального числа. Например, если введено число 325, то сумма его цифр равна 10 (3+2+5), а произведение 30 (3*2*5).
#4 - Перевести число, введенное пользователем, в байты или килобайты в зависимости от его выбора.
#это задачки разные, для понятия вообще уровня, что и как есть


#1
def task_one():
    a = input()
    b = input()
    print("So, now we are gonna change their positions. ")

    print("look, right now your first input is a: " + str(a))
    print("and the second one is b: " + str(b))

    c = a

    a = b
    print("wait..")
    print("little bit more..")
    print("Done!")
    print("I need to apologize, but right now, 'a' means your second number: " + str(a))

    b = c

    print ("and 'b' means that it is your first number: " + str(b))



#2 - Вводятся три целых числа. Определить какое из них наибольшее.

a = input("so, there should be three numbers. Please, enter the first one: ")
b = input("Go ahead and give me the second one: ")
c = input("Hell yeah! The last one: ")

if a >= b and a >= c:
   print (a)
if b >= a and b >= c:
   print (b)
if c >= a and c >= b:
   print (c)
