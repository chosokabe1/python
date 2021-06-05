# イテレータ 次の要素を返してくれるデータの集合
scores = [40, 50, 70, 90, 60]
it = iter(scores)
print(next(it))
print(next(it))
print("hello")
print(next(it))

for score in scores:
    print(score)

def get_infinite(): # じぇねれーた
    i = 0
    while True:
        yield i * 2 
        # yield つぎの要素を引っ張ってくる
        i+= 1

g = get_infinite()
print(next(g))
print(next(g))
print(next(g))
