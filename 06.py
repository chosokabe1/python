name = "choso"
score = 52.8

print("name: %-10s, score: %10.2f" %(name, score))
#name 10の幅の左揃え、score 10の幅で少数点以下は2桁まで

print("name: {0:>10s}, score: {1:<10.2f}".format(name,score))

