#if
# input 標準入力を読み込む。文字列が帰ってくる。
score = int(input("score ? "))

if score > 80:
    print("Great!")
elif score > 60:
    print("Good!")
else:
    print("so so ...")

print("Great!" if score > 80 else "so so...")

# while
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
else:
    print("end")

#for
# for 変数 in データの集合：
# 処理
# range(0, 10) 0 ~ 9の数字
# range(10)    0~9,0から始まる場合に0は省略することができる。
for i in range(10):
    if i == 2:
        # break
        continue
    print(i)
else:
    print("end")
