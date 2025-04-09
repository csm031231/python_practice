import requests
import xmltodict

query = "IU"
search_type = "artist"

API_URL = f"http://www.maniadb.com/api/search/{query}/?sr={search_type}&display=10&v=0.5"

response = requests.get(API_URL)
parsed_data = xmltodict.parse(response.text)  # XML -> JSON 변환
result = parsed_data.get("rss").get("channel").get("item")[0].get("maniadb:majorsongs").get("song")
for song in result:
    print(f"제목: {song.get('name')}")

print(f"HTTP 상태 코드: {response.status_code}")
print(f"응답 내용:\n{result}")
