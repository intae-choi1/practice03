import requests
import re
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
}
url = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"thumb_img"})
print(len(images))
for idx, image in enumerate(images):
    if idx >= 30:
        break
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https:"+image_url
    print(image_url)
    
    image_res = requests.get(image_url)
    image_res.raise_for_status()
    with open(f"movie_images/movie{idx+1}.jpg", "wb") as f:
        f.write(image_res.content)