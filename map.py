# map(関数, イテレータ)

def triple(n):
    return n * 3

print(list(map(triple, [1, 2, 3])))

# lambda 引数: 処理
print(list(map(lambda n: n * 3, [1, 2, 3])))

# filter(関数, イテレータ)

def is_even(n):
    return n % 2 == 0
# 偶数ならTrue, 奇数ならFalseを返す

#print(list(filter(is_even, range(10))))

print(list(filter(lambda n: n % 2 == 0, range(10))))