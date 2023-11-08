import urllib.request
import urllib.error
from bs4 import BeautifulSoup

# 設定値
requestURL = "http://xml.kishou.go.jp/jmaxml1/"
xmlPostBody = """<?xml version="1.0" encoding="utf-8" ?>
<Report xmlns="http://xml.kishou.go.jp/jmaxml1/">
<Control>
<Status>通常</Status>
<EditorialOffice>鹿児島地方気象台</EditorialOffice>
<PublishingOffice>鹿児島地方気象台</PublishingOffice>
</Control>
<Head xmlns="http://xml.kishou.go.jp/jmaxml1/informationBasis1/">
<Title>大雨に関する鹿児島県（奄美地方を除く）気象情報</Title>
...
</Head>
<Body xmlns="http://xml.kishou.go.jp/jmaxml1/body/meteorology1/">
<Notice />
<Comment><Text type="本文"> ６日２１時の気象レーダー観測によると、発達した雨雲は鹿児島・日置、出水・伊佐、川薩・姶良、大隅地方から遠ざかっています。 このため大雨のおそれはなくなりましたので、大雨・洪水注意報を解除しました。 これで「大雨に関する鹿児島県（奄美地方を除く）気象情報」は、終了します。</Text>
</Comment>
</Body>
</Report>
"""

# ヘッダーとメソッドを定義
headers = {"Content-Type": "application/xml"}
method = "POST"

# POSTリクエストを送信
bytesXMLPostBody = xmlPostBody.encode("UTF-8")
req = urllib.request.Request(url=requestURL, data=bytesXMLPostBody, headers=headers, method=method)
try:
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        soup = BeautifulSoup(response_body, 'lxml')
        print(soup)
except urllib.error.HTTPError as err:
    soup = BeautifulSoup(str(err), 'lxml')
    print(soup)