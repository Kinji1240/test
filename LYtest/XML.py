import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import japanize_kivy

class WeatherApp(App):
    def build(self):
        self.api_url = "https://api.open-meteo.com/v1/forecast?latitude=34.7&longitude=135.5&daily=temperature_2m_max,temperature_2m_min,weather_code&timezone=Asia%2FTokyo"
        self.data = None
        self.weather_layout = create_weather_layout()
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.weather_layout)
        # 最初のデータ取得と更新関数の呼び出しをスケジュール
        self.update_weather_data()
        Clock.schedule_interval(self.update_weather_data, 3600)  # 1時間ごとに更新
        return layout

    def update_weather_data(self, dt=None):
        response = requests.get(self.api_url)
        data = response.json()
        self.data = data
        self.update_display()

    def update_display(self):
        if self.data:
            daily_data = self.data.get("daily", {})
            time = daily_data.get("time", [])
            max_temperature = daily_data.get("temperature_2m_max", [])
            min_temperature = daily_data.get("temperature_2m_min", [])
            weather_code = daily_data.get("weather_code", [])

            if time and max_temperature and min_temperature and weather_code:
                weekly_data = []  # 一週間分のデータを格納するリスト
                for i in range(len(time)):
                    day_data = {
                        'day': time[i],
                        'max_temp': max_temperature[i],
                        'min_temp': min_temperature[i],
                        'weather': get_weather_meaning(weather_code[i])
                    }
                    weekly_data.append(day_data)

                # 一週間分のデータを更新
                self.update_weekly_data(weekly_data)

    def update_weekly_data(self, weekly_data):
        # 一週間分のデータをレイアウトに反映
        self.weather_layout.clear_widgets()
        for day_data in weekly_data:
            day_layout = BoxLayout(orientation='vertical')
            day_label = Label(text=day_data['day'])
            max_temp_label = Label(text=f"Max Temp: {day_data['max_temp']}°C")
            min_temp_label = Label(text=f"Min Temp: {day_data['min_temp']}°C")
            weather_label = Label(text=f"Weather: {day_data['weather']}")
            day_layout.add_widget(day_label)
            day_layout.add_widget(max_temp_label)
            day_layout.add_widget(min_temp_label)
            day_layout.add_widget(weather_label)
            self.weather_layout.add_widget(day_layout)

def get_weather_meaning(weather_code):
    # 新しい天気コードと意味の対応表
    weather_codes = {
        0: "雲の発達が見られないか、観測できない",
        1: "雲は一般的に消散または発達が減少している",
        2: "天空の状態は全体的に変わっていない",
        3: "雲は一般的に形成または発達している",
        4: "視程が煙で低下",
        5: "もや",
        6: "空中に広範な塵が漂っている",
        7: "風によって塵や砂が巻き上げられている",
        8: "発達した塵旋風または砂旋風が見られる",
        9: "視界内の砂嵐または砂嵐",
        10: "もや",
        11: "浅い霧や氷霧のパッチ",
        12: "より連続的な浅い霧や氷霧",
        13: "稲妻が見え、雷は聞こえない",
        14: "視界内の降水、地面または海面に届かない",
        15: "視界内の降水、地面または海面に届いており、遠い",
        16: "視界内の降水、地面または海面に届いており、近いが観測地点ではない",
        17: "雷雨、ただし観測時点での降水はない",
        18: "観測地点またはその近くでスコール",
        19: "ファネルクラウド（漏斗雲）",
        20: "霧や雪粒がシャワーとして降らない霧や雪粒",
        21: "雨（凍結していない）はシャワーとして降っていない",
        22: "雪はシャワーとして降っていない",
        23: "雨と雪または氷の粒、タイプ（a）、シャワーとして降らない",
        24: "凍結した霧や凍結した雨はシャワーとして降らない",
        25: "雨のシャワー",
        26: "雪または雨と雪のシャワー",
        27: "ひょうのシャワー",
        28: "霧または氷霧",
        29: "雷雨（降水または降水なし）",
        30: "わずかまたは中程度の塵嵐または砂嵐",
        31: "わずかまたは中程度の塵嵐または砂嵐 - ほとんど変化なし",
        32: "わずかまたは中程度の塵嵐または砂嵐 - 開始または増加",
        33: "激しい塵嵐または砂嵐 - 減少",
        34: "激しい塵嵐または砂嵐 - ほとんど変化なし",
        35: "激しい塵嵐または砂嵐 - 開始または増加",
        36: "わずかまたは中程度の吹雪、一般的に低い",
        37: "一般的に低い場所での大雪",
        38: "わずかまたは中程度の吹雪、一般的に高い",
        39: "一般的に高い場所での大雪",
        40: "観測時には霧または氷霧が見えるが、直前の1時間内には観測地点で観測されていない",
        41: "霧または氷霧のパッチ",
        42: "霧または氷霧、空が見える部分が薄くなった",
        43: "霧または氷霧、空が見えない部分が薄くなった",
        44: "霧または氷霧、空が見える部分はほとんど変化なし",
        45: "霧または氷霧、空が見えない部分はほとんど変化なし",
        46: "霧または氷霧、空が見える部分が始まったか、厚くなった",
        47: "霧または氷霧、空が見えない部分が始まったか、厚くなった",
        48: "霧、リームを堆積、空が見える",
        49: "霧、リームを堆積、空が見えない",
        50: "霜、凍結しない霧、断続的にわずか",
        51: "霜、凍結しない霧、継続的にわずか",
        52: "霜、凍結しない霧、断続的に中程度",
        53: "霜、凍結しない霧、継続的に中程度",
        54: "霜、凍結しない霧、断続的に激しい",
        55: "霜、凍結しない霧、継続的に激しい",
        56: "霜、凍結する、わずか",
        57: "霜、凍結する、中程度または激しい",
        58: "霜と雨、わずか",
        59: "霜と雨、中程度または激しい",
        60: "雨、凍結しない、断続的にわずか",
        61: "雨、凍結しない、継続的にわずか",
        62: "雨、凍結しない、断続的に中程度",
        63: "雨、凍結しない、継続的に中程度",
        64: "雨、凍結しない、断続的に激しい",
        65: "雨、凍結しない、継続的に激しい",
        66: "雨、凍結する、わずか",
        67: "雨、凍結する、中程度または激しい",
        68: "雨、または霧雨と雪、わずか",
        69: "雨、または霧雨と雪、中程度または激しい",
        70: "雪片の降り方、わずか",
        71: "雪片の降り方、継続的にわずか",
        72: "雪片の降り方、断続的に中程度",
        73: "雪片の降り方、継続的に中程度",
        74: "雪片の降り方、断続的に激しい",
        75: "雪片の降り方、継続的に激しい",
        76: "氷の柱",
        77: "雪粒",
        78: "星型の雪結晶が散在",
        79: "氷の粒、タイプ（a）",
        80: "雨のシャワー、わずか",
        81: "雨のシャワー、中程度または激しい",
        82: "雨のシャワー、激しい",
        83: "雨と雪のシャワー、わずか",
        84: "雨と雪のシャワー、中程度または激しい",
        85: "雪のシャワー、わずか",
        86: "雪のシャワー、中程度または激しい",
        87: "雪の粒または氷の粒のシャワー",
        88: "雪の粒または氷の粒のシャワー、中程度または激しい",
        89: "雨の降り方、雨の降り方なしであるかどうかにかかわらず、中程度または激しい",
        90: "雨の降り方、雨の降り方なしであるかどうかにかかわらず、中程度または激しい",
        91: "観測時には軽い雨 - 観測時に雷雨があるが観測時にはない",
        92: "観測時には中程度または激しい雨 - 観測時に雷雨があるが観測時にはない",
        93: "観測時には軽い雪、または雨と雪の混合またはひょう - 観測時に雷雨があるが観測時にはない",
        94: "観測時には中程度または激しい雪、または雨と雪の混合またはひょう - 観測時に雷雨があるが観測時にはない",
        95: "観測時には軽いまたは中程度の雷雨、ひょうなし、雨と/または雪あり",
        96: "観測時にはひょうありの軽いまたは中程度の雷雨",
        97: "観測時にはひょうなしの重い雷雨、雨および/または雪あり",
        98: "観測時にはひょうなしの重い雷雨、塵嵐または砂嵐と組み合わせ",
        99: "観測時にはひょうありの重い雷雨"
    }

    return weather_codes.get(weather_code, "不明")

def create_weather_layout():
    layout = BoxLayout(orientation='vertical')
    return layout

if __name__ == '__main__':
    WeatherApp().run()
