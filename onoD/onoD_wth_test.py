import requests

base_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/"
area_code = "270000"  # 大阪府のエリアコード
url = f"{base_url}{area_code}.json"
res = requests.get(url).json()

print(res)
