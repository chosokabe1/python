# モジュール

# import user
# user.pyが実行される

# from user import AdminUser
# モジュールから指定した関数やクラスだけを読み込む
# (from モジュール名 import クラス/関数名)

from user import AdminUser, User
# 複数のクラスを読みこむ

# import user の場合
# bob = user.AdminUser("bob", 23) 
#関数はモジュール名を前につけて使う。

# from user import Adminuserの場合
bob = AdminUser("bob", 23)

tom = User("tom")

print(bob.name)
bob.say_hi()
bob.say_hello()