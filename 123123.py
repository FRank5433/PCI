import urllib.request, urllib.parse, http.cookiejar
from bs4 import BeautifulSoup

def getHtml(url):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')]

    urllib.request.install_opener(opener)

    html_bytes = urllib.request.urlopen(url).read()
    html_string = html_bytes.decode('utf-8')
    return html_string

html = getHtml('http://zst.aicai.com/ssq/openInfo/')

soup = BeautifulSoup(html,'html.parser')

tr1 = soup.find_all('tr',attrs={"onmouseout": "this.style.background=''"})
tr2 = soup.find_all('tr',attrs={"onmouseout": "this.style.background='#eff3f7'"})
tr1.extend(tr2)
results = []
for ix in tr1:
    tds = ix.find_all('td')
    result = []
    for ixx in tds:
        result.append(ixx.get_text())
    results.append(result)

for ix in range(len(results)):
    for ixx in range(1,len(results)):
        if results[ixx][0] >= results[ixx-1][0]:
            pass
        else:
            temp = results[ixx]
            results[ixx] = results[ixx-1]
            results[ixx-1] = temp
for ix in results:
    print(ix)




#
#
# soup = BeautifulSoup(html,'html.parser')
#
# tr = soup.find('tr',attrs={"onmouseout": "this.style.background=''"})
# tds = tr.find_all('td')
# opennum = tds[0].get_text()
# reds = []
# for i in range(2,8):
#     reds.append(tds[i].get_text())
# blue = tds[8].get_text()
# print(opennum+'期开奖号码：'+ (',').join(reds)+", 蓝球："+blue)
#
# print(132)
# print(132)


