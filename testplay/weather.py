import urllib.request
import urllib.error

from bs4 import BeautifulSoup

# 設定値
requestURL = "http://xml.kishou.go.jp/jmaxml1/"
headers = {"Content-Type": "application/xml; charset=utf-8"}
method = "POST"

# 正しいXMLデータを設定
xmlPostBody = """
<?xml version="1.0" encoding="UTF-8"?>
<Report xmlns="http://xml.kishou.go.jp/jmaxml1/" xmlns:jmx="http://xml.kishou.go.jp/jmaxml1/" xmlns:jmx_add="http://xml.kishou.go.jp/jmaxml1/addition1/">
    <!-- ここにXMLデータを追加 -->
</Report>
"""

# POSTリクエスト送信
bytesXMLPostBody = xmlPostBody.encode("UTF-8")
req = urllib.request.Request(url=requestURL, data=bytesXMLPostBody, headers=headers, method=method)
try:
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        soup = BeautifulSoup(response_body, "lxml")
        print(soup)
except urllib.error.HTTPError as err:
    soup = BeautifulSoup(err, "lxml")
    print(soup)