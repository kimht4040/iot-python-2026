# 파일 입출력



print('파일입출력')

f = open('text.txt', 'w')
#with open('text.txt', 'w') as f
# with 사용시 close 생략 가능(자동으로 해줌)
f.write('텍스트를 씁니다.\n') #print와 다르게 기본적으로 \n 이 없음
f.write('텍스트를 두줄 씁니다.\n')

f.close

with open('text.txt', 'r') as f:
    content = f.read()
    print(content)





