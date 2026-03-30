# 메인함수개념
def main():
    print("이곳이 실제 메인 로직입니다.")
    print("main")
print("여기는 전역 범위(Global Scope)라 바로 실행됩니다.")
# __main__ 파이썬의 특별 변수
# __import__ 와 같은 특별함수

if __name__ == '__main__':
    main()