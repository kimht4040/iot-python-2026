# csv 파일 읽기



with open('./day2/부산광역시 해운대구_도서관 신착도서 현황_20251100.csv','r', encoding='utf-8') as f:
    line = f.read()
    print(line)