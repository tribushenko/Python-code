import requests

res = requests.get("https://docs.python.org/3.5/")
res = requests.get("https://google.com/",
                    params={"text":"Stepik",
                            "test": "test1",
                            "name": "Name With Spaces",
                            "list": ["test1", "test2"]
                            })
print(res.status_code) # status_code = 200 - success, 404 - page not found
                       # 500 - server error 
print(res.headers["Content-Type"]) # тип содержимого. В нашем случае html

print(res.content) # бинарные данные - содержимое запроса
print(res.text)
print(res.url)