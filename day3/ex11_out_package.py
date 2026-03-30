# 외부 라이브러리 사용
import requests


response = requests.get("https://www.google.com")


print(response.status_code)