# リスト型とタプル
# - スライス
# 集合型
# 辞書型
# セット　順番が無くて、重複を許さないデータ構造

# リスト型
# scores = [40,50]
# print(scores[0]) # 40
# scores[0] = 45
# print(len(scores)) # 2
# scores.append(100)
# print(scores)

# for score in scores:
#     print(score)

#何番目かの要素かも取り出す
# for i, score in enumerate(scores):
#     print("{0}: {1}".format(i, score))

scores = [40,50,70,90,60]
print(scores[1:4]) # 50, 70, 90
print(scores[:2])  # 40, 50
print(scores[3:])  # 90, 60
print(scores[-3:]) # 70, 90, 60
# 60 が -1, 90 が -2, 70 が -3

s = "hello"
print(s[1:4])


# タプル
# 値の変更ができない
# 丸括弧で囲う
items = (50, "apple", 32.5)
print(items[1])
# items[1] = "pen"

# tuple <-> list の変換
print(list((1,3,5)))
print(tuple([1,3,5]))

# tupleはプログラム中で変わってほしくないデータをとり回すのによく使われる


# ------------------------
# 辞書型 キーと値でデータを管理する

sales = {"taguchi": 200, "fkoji": 400}
# print(sales["taguchi"])
# sales["taguchi"] = 300
# sales["dotinstall"] = 500
# del(sales["fkoji"])
# print(sales)

for key, value in sales.items():
    print("{0}: {1}".format(key, value))



