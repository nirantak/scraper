import requests
from bs4 import BeautifulSoup

url = "https://docs.python.org/3/library/functions.html"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

# for link in soup.find_all("a"):
# 	if "http" in link.get("href"):
# 		print(link.text, link.get("href"))

data = soup.find_all("dl", {"class": "function"})
# print(data)

for item in data:
	print("{}:\n{}\n".format(item.find("code").text, item.find("p").text))
