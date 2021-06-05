# set
# 順番が無くて重複を許さないデータ構造
# なみ括弧で囲う

a = {5, 3, 8, 5}
b = {3, 5, 8, 9}
print(a)
print(5 in a) # True
a.add(2)
a.remove(3)
print(a)
print(len(a))

# 和集合
print(a | b)
# 積集合
print(a & b)
# 差集合
print(a - b)
