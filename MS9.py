import turtle, time, random


# turtle_sqloop(5,10)
def turtle_sqloop(value, size):
	for i in range(value):
		for j in range(4):
			turtle.forward(size)
			turtle.left(90)
	return (value, size)


# turtle_crloop(5,10)
def turtle_crloop(value, size):
	for k in range(value):
		turtle.circle(180, size)
	return (value, size)


# turtle_trloop(5,10)
def turtle_trloop(value, size):
	for l in range(value):
		turtle.left(45)
		turtle.forward(size)
		turtle.right(90)
		turtle.forward(size)
		turtle.right(90)
		turtle.forward(size)
	return (value, size)


# lenprint("Hello")
def lenprint(value):
	for m in value:
		print(m)


# turtle.goto() but without pen
def turtle_upgoto(value_x, value_y):
	turtle.up()
	turtle.goto(value_x, value_y)
	turtle.down()
	return (value_x, value_y)


# turtle_waterline(6)
def turtle_waterline(value):
	for n in range(value):
		for o in range(9):
			turtle.forward(5)
			turtle.left(5)
		for p in range(9):
			turtle.forward(5)
			turtle.right(5)
	return (value)


# timer(0,30)
def timer(value_x):
	while value_x == 0:
		value_x = value_x - 1
		time.sleep(1)
	return value_x


# runner(9,11)
def runner(value_x, value_y):
	while value_x < value_y:
		value_x = value_x + 1
		time.sleep(1)
	return value_x, value_y


# strvalue(9) - 9=str(9)
def strvalue(value):
	return str(value)


# chase(2,7,list)
def chase(value_x, value_y, looked):
	if looked in value_x:
		return value_x
	if looked in value_y:
		return value_y


# _random("Hello","Bye","4")
def _random(*self, value_x, value_y, value_n, value_z, value_o, value_i):
	list = [value_x, value_y, value_n, value_z, value_o, value_i]
	return random.randint(0, len(list) - 1)


# isdivision(10,2)
def isdivision(value_x, value_y):
	if value_x % value_y == 0:
		return True
	else:
		return False


# check("hello",listname)
def check(value, list):
	if value in list:
		return True
	else:
		return False


# -
def ArithmethicNum(list):
	return sum(list) / len(list)
