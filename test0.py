# user =  "Alman"
# access = "Admin"
# def sum(r, e):
# 	return "{0} {0}".format(r, e)

# print(sum(user, access))
# print(" !_! " * 5)

## Дано: 2 числа
## Надо: возвести их в степень  (**)
## у тебя не строка.. а действие, А действите нужно по особенному отмечать? a**b

## calc

#### sum div mult pow del mod

from sys import argv as ar
## ar[0       1        2        3]
# filename + num + operation + num
print(ar)
for i in ar:
	print(i, '>> ', type(i))







def summ(a, b):
	return a + b

def power(a, b):
	return a ** b

def mult(a, b):
	return a * b

def delete(a, b):
	return a / b

def mod(a, b):
	return a % b

def div(a, b):
	return a - b




def oper(a, op, b):

	if op == "+":
		res = summ(a,b)

	elif op =="-":
		res = div(a,b)

	elif op =="*":
		res = mult(a, b)

	elif op =="/":
		res = delete(a,b)

	elif op =="**":
		res = power(a,b)

	elif op =="%":
		res = mod(a,b)

	else:
		res = "Выучи математику дебил, такого знака нет!"

	return res







if __name__=="__main__":
	res = ""
	if len(ar)  == 4 :
		a = int(ar[1])
		op = ar[2]
		b = int(ar[3])

		res = oper(a, op, b)
	else:
		res = "Это тебе калькулятор, а  не губозакаточная машина, не мечтай! вычисляй!"

	print(res)
