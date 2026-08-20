import requests as pavan


# t = pavan.get("https://www.skpythonclasses.com")

# print(t.txt)


# t = pavan.get("https://www.google.com")

# print(t.text)


# x = requests.get('http://www.skpythonclasses.com')

# print(x.text)



data = {'name': 'sachin' , 'age': 18}

a = pavan.post('http://www.skpythonclasses.com', json=data)



import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
  