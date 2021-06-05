# クラスの多重継承
# A, B -> C

class A:
    def say_a(self):
        print("A!")
    def say_hi(self):
        print("hi a")
class B:
    def say_b(self):
        print("B!")
    def say_hi(self):
        print("hi b")
    
class C(A, B):
    pass

c = C()
c.say_a()
c.say_b()
c.say_hi() 
# 同じメソッドがあった場合は先に指定したほうのメソッドが優先される。
#class C(A,B) をC(B,A)に変えたら、"hi b"　が表示される。