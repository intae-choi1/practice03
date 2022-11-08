import requests
res = requests.get("http://naver.com")
res.raise_for_status() # 200이 아니면 에러를 발생시킴
# if res.status_code == requests.codes.ok: # codes.ok는 200임
#     print("wjdtkd")
# else:
#     print(res.status_code)

print(len(res.text))
with open("my.html", "w", encoding="utf-8") as f:
    f.write(res.text)
