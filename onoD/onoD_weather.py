# -*- coding: utf-8 -*-
import requests
import json
import csv
import japanize_kivy


def cord_opt_csv():
    # onoD_Opt.csvファイルのパス
    file_path = r'C:\Users\204012\Desktop\test_git\test\onoD\onoD_Opt.csv'

    # CSVファイルを読み込む
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
        
    # 必要な部分を変更
    cord = data[2][1]  # watchを文字列に変換して代入
    prefecture = data[3][1]  
    return cord

def pref_opt_csv():
    # onoD_Opt.csvファイルのパス
    file_path = r'C:\Users\204012\Desktop\test_git\test\onoD\onoD_Opt.csv'

    # CSVファイルを読み込む
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
        
    # 必要な部分を変更
    cord = data[2][1]  
    prefecture = data[3][1]  
    return prefecture

# エリアコード
area_dic = cord_opt_csv()
# CSV出力先
output_file = "onoD_weather.csv"

# CSVヘッダー
header = ["都道府県","報告日時","予報日時","天気","気温","最高気温","最低気温"]

def main():
    make_csv()

def make_csv():
    with open(output_file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(header)

        # JSONから情報を取得
        write_lists = get_info()

        # CSV書き込み
        writer.writerows(write_lists)
      


def get_info():
    write_lists = []
    base_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/"


    url = base_url + area_dic + ".json"

    res = requests.get(url).json()

    prefecture = pref_opt_csv()

    for re in res:

        reportDatetime = re["reportDatetime"]
        timeSeries = re["timeSeries"]

        for time in timeSeries:
            for i in range(len(time["areas"])):
                    
                for j in range(len(timeSeries[0]["timeDefines"])):
                    if 'weathers' not in time["areas"][i]:
                        weather = ""
                    else:
                        weather = time["areas"][i]["weathers"][j]

                    if 'temps' not in time["areas"][i]:
                        temps = ""
                    else:
                        temps = time["areas"][i]["temps"][j]

                    if 'tempsMax' not in time["areas"][i]:
                        tempsMax = ""
                    else:
                        tempsMax = time["areas"][i]["tempsMax"][j]

                    if 'tempsMin' not in time["areas"][i]:
                        tempsMin = ""
                    else:
                        tempsMin = time["areas"][i]["tempsMin"][j]

                    timeDefine = time["timeDefines"][j]

                    pops = time["areas"][i]["pops"][j]  # 降水確率
                    temps = time["areas"][i]["temps"][j]  # 気温
                    tempsMax = time["areas"][i]["tempsMax"][j]  # 最高気温
                    tempsMin = time["areas"][i]["tempsMin"][j]  # 最低気温

                    # 各情報をリストに格納
                    write_list = []
                    write_list.append(prefecture)
                    write_list.append(reportDatetime)
                    write_list.append(timeDefine)
                    write_list.append(weather)
                    write_list.append(pops)
                    write_list.append(temps)
                    write_list.append(tempsMax)
                    write_list.append(tempsMin)

                    write_lists.append(write_list)
    return write_lists

if __name__ == '__main__':
    main()