import urllib.request
import urllib.error

import lxml
from bs4 import BeautifulSoup

# 設定値
requestURL = "http://xml.kishou.go.jp/jmaxml1/"
xmlPostBody = "xml.kishou.go.jp/jmaxml1/"


# POSTリクエスト送信
bytesXMLPostBody = xmlPostBody.encode("UTF-8")
req = urllib.request.Request(url=requestURL, data=bytesXMLPostBody, headers="headers", method="method")
try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode("utf-8")
            soup = BeautifulSoup(response_body, lxml)
            print(soup)
except urllib.error.HTTPError as err:
        soup = BeautifulSoup(err, lxml)
        print(soup)