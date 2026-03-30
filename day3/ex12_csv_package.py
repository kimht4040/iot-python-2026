# csv 모듈 사용해서 csv 파일 리드


import csv # 내장라이브러리
with open('day2/부산광역시 해운대구_도서관 신착도서 현황_20251100.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)

    for row in reader: # 리더를 한줄씩 읽어서 끝까지
        print(row)