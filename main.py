import requests
import json
print("select the news of your choice\ntype *exit* to exit from the app")
query = ""
while(query != "exit"):
    query = input("\nselect the news you want to read\n1 : politics\n2 : technology\n3 : current affairs\n4 : sports\n5 : movies\nexit : exit\n")
    if query =="exit":
        break
    else:
        url = f"https://newsapi.org/v2/everything?q={query}&from=2023-02-19&sortBy=publishedAt&apiKey=b0346f4e627042459a0dfd2f016de152"
        r = requests.get(url)
        news = json.loads(r.text)
        for article in news["articles"]:
            print(article["title"])
            print(article["description"])



