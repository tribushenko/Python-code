# artsy.net: password = edcrfv123321Artem
# Name	artsy_app

import requests
import json

client_id = 'de25c063656ba5a2f0b1'
client_secret = 'f48c6dde95c6fa9f484f4670c36b1e1e'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
dict_artist = {}
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
codes = open("codes.txt").read().split("\n")[:-1]
for i in codes:
    r = requests.get(f"https://api.artsy.net/api/artists/{i}", headers=headers)
    # разбираем ответ сервера
    j = json.loads(r.text)
    dict_artist[j["sortable_name"]] = j["birthday"]

sorted_tuple = sorted(dict_artist.items(), key=lambda x: (x[1], x[0]))
for k, v in sorted_tuple:
    print(k)
