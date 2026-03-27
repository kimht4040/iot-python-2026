## 구구단 프로그램


# 2중 for 문



dan = int(input("몇단까지 출력할까요"))


for i in range(2,dan+1):
    print(f"{i}단")
    for j in range(1,10):
        print(f"{i} X {j} = {i * j}")

