# 関数

# def say_hi():
#     print("hi")

# say_hi()

def say_hi(name = "takash", age = 20): #引数に何も渡さなければ、初期値が使われる
    print("hi {0} ({1})".format(name, age))

say_hi("tom", 23)
say_hi("bob", 21)
say_hi(age = 2)

#関数2

def say_hi2():
    return "hi"
    print("hello")

msg = say_hi2()
print(msg)

def say_hi3():
    pass

msg = say_hi3
print(msg)