import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # res.text를 lxml 파서를 통해서 BS객체를 만든 것
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # 처음으로 발견된 a 엘레먼트
# print()
# print(soup.a.attrs)
# print(soup.a["href"])

print(soup.find("a", attrs={"class": "Nbtn_upload"})) # class가 Nbtn_upload인 a 태그를 찾아라
print(soup.find(attrs={"class": "Nbtn_upload"})) # 아무 엘레먼트나 찾아

rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())
rank2 = rank1.nextSibling.next_sibling  # 다음 형제가 \n 등의 공백일수도 있어서 next를 2번해야할 때도 있음
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

# print(rank1.parent)
print("-----")
rank2 = rank1.find_next_sibling("li") # 패턴이 일치하는 형제만 찾음
print(rank2.a.get_text())
print("-----")
siblings = rank1.find_next_siblings("li")
for sibling in siblings:
    print(sibling.a.get_text())


webtoon = soup.find("a", text="여신강림-외전-9화[수진ep]") # 텍스트가 일치하는 a태그 찾아라
print(webtoon)
