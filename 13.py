# クラス

class User: #からのクラスを作っている
    pass

tom = User() # インスタンス
tom.name = "tom"
tom.score = 20

bob = User()
bob.name = "bob"
bob.level = 5

print(tom.name)
print(bob.level)

class User2:
    # クラス変数
    count = 0
    def __init__(self, name): 
        User2.count += 1
        # インスタンス変数
        # コンストラクタという特殊な関数
        # selfはこのクラスから作られるインスタンス
        self.name = name

print(User2.count) # 0
tom2 = User2("tom")
bob2 = User2("bob")
print(User2.count) # 2
print(tom.name)
print(bob.name)

print("\n3")

#クラスの中で定義される関数をメソッドという
class User3:
    # クラス変数
    count = 0
    def __init__(self, name): 
        User3.count += 1
        # インスタンス変数
        # コンストラクタという特殊な関数
        # selfはこのクラスから作られるインスタンス
        self.name = name

    # インスタンスメソッド
    def say_hi(self):
        print("hi {0}".format(self.name))
    
    # クラスメソッド
    @classmethod # おまじない
    def show_info(cls): # clsはクラス自身であるという意味
        print("{0} instances".format(cls.count))
          

tom3 = User3("tom3")
bob3 = User3("bob3")

tom3.say_hi()
bob3.say_hi()

User3.show_info()

print("\n4")
# クラス
# - アクセス制限
class User4:
    count = 0
    def __init__(self, name): 
        User4.count += 1
        self.__name = name
        #外からアクセスしてほしくない変数名の前に”_”をつける
        #これは慣習てきな約束なので実際には外からアクセスすることができる。

        # "__" とアンダースコアを2つにすると、外からアクセスができない。
    def say_hi(self):
        print("hi {0}".format(self.__name))

tom4 = User4("tom")
#print(tom4._name)
tom4.say_hi()

print("\n5")
# クラスの継承
class User5:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("hi {0}".format(self.name))

class AdminUser(User5):
    def __init__(self, name, age):
        super().__init__(name) 
        # name は親クラスのコンストラクトを使って設定している

        self.age = age
    def say_hello(self):
        print("hello {0} ({1})".format(self.name, self.age))
    
    #override
    def say_hi(self):
        print("[admin] hi {0}".format(self.name))


bob5 = AdminUser("bob", 23)
print(bob5.name)
bob5.say_hi()
bob5.say_hello()
