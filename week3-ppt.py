# 抓取PTT電腦網頁原始碼(HTML)
import bs4
import urllib.request as req
latestpage = 9499
newarr = []
for i in range(latestpage-9, latestpage+1):
    url = "https://www.ptt.cc/bbs/movie/index"+str(i)+".html"

    # 建立一個Request 物件，附加Request Headers的資訊
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # 取得電影文章標題
    root = bs4.BeautifulSoup(data, "html.parser")  # 讓 bs4解析html
    titles = root.find_all("div", class_="title")  # 尋找 class"title"的div標籤\

    for title in titles:
        # 如果包含a標籤，印出來
        if title.a != None:
            if "Re" in title.a.string:
                pass
            else:
                if "[好雷]" in title.a.string:
                    newarr.append(title.a.string)
                elif "[普雷]" in title.a.string:
                    newarr.append(title.a.string)
                elif "[負雷]" in title.a.string:
                    newarr.append(title.a.string)

newarr.sort()  # 排序好雷、普雷、負雷
with open('movie.txt', 'w',  encoding="utf-8", newline='') as file:
    for i in range(0, len(newarr)):
        file.write(newarr[i]+"\n")
