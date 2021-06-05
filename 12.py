# 関数
# 変数のスコープ

msg = "hello" # グローバル変数
msg2 = "hello"

def say_hi():
    msg = "hi" # ローカル変数
    print(msg)

    global msg2 # globalをつけると、グローバル変数を書き換えることができる。
    msg2 = "hello global"
    print(msg2)

say_hi()
print(msg)
print(msg2)