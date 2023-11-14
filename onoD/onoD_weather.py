import requests
import csv

def r_opt_csv():
    # ファイルの読み込みと書き込みはここで行います
    file_path = "test\onoD\onoD_csv_list\onoD_opt.csv"
        
    # 既存のCSVファイルを読み込む
    with open(file_path, mode='r',encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
        
    # 必要な部分を変更
    csvdata = data[2][1]

    return csvdata

def get_info(code):
    base_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/"
    url = f"{base_url}{code}.json"
    res = requests.get(url).json()

    # 一週間の天気情報を取得
    weather_data = res[0]['timeSeries'][0]['areas'][0]['weathers']

    # 一週間の気温情報を取得
    temperature_data = res[0]['timeSeries'][2]['areas'][0]['temps']

    # 一週間の気温情報を取得
    testdata = res[0]['timeSeries'][2]['areas'][0]['temps']
    print(testdata)


    # 一週間の降水確率情報を取得
    precipitation_data = res[0]['timeSeries'][1]['areas'][0]['pops']

    return weather_data, temperature_data, precipitation_data

def main():
    areaCode = r_opt_csv()

    weather_data, temperature_data, precipitation_data = get_info(code=areaCode)

    # 結果の出力
    print("天気情報:", weather_data)
    print("気温情報:", temperature_data)
    print("降水確率情報:", precipitation_data)

    # 新しいCSVファイルとして書き出す
    file_path = "test\onoD\onoD_csv_list\onoD_weather.csv"
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['天気情報', '気温情報', '降水確率情報'])
        writer.writerows(zip(weather_data, temperature_data, precipitation_data))

if __name__ == '__main__':
    main()