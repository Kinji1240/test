import requests

def get_info():
    base_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/"
    area_code = "270000"  # 大阪府のエリアコード
    url = f"{base_url}{area_code}.json"
    res = requests.get(url).json()

    # 一週間の天気情報を取得
    weather_data = res[0]['timeSeries'][0]['areas'][0]['weathers']

    # 一週間の気温情報を取得
    temperature_data = res[0]['timeSeries'][2]['areas'][0]['temps']

    # 一週間の降水確率情報を取得
    precipitation_data = res[0]['timeSeries'][1]['areas'][0]['pops']

    return weather_data, temperature_data, precipitation_data

def main():
    weather_data, temperature_data, precipitation_data = get_info()

    # 結果の出力
    print("天気情報:", weather_data)
    print("気温情報:", temperature_data)
    print("降水確率情報:", precipitation_data)

if __name__ == '__main__':
    main()