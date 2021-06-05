# 例外処理

class MyException(Exception):
    # python 用意している Exception クラスを継承して独自の例外を作る。
    pass

def div(a,b):
    try:
        if(b < 0):
            raise MyException("not minus")
        print(a / b)
    except ZeroDivisionError:
        print("not by zero!")
    except MyException as e:
        print(e)
    else:
        print("no exception!")
    finally:
        print("-- end --")
div(10, 3)
div(10, 0)
div(10, -3)