import json
import urllib.request as req
import csv

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
# 建立一個Request 物件，附加Request Headers的資訊
request = req.Request(url, headers={

    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")  # 取得json格式
#data= data.replace()
data = json.loads(data)
# print(data)
# 取得json格式資料
newlist = []
posts = data["result"]["results"]
for i in range(len(posts)):
    postsyear = posts[i]["xpostDate"]
    posts_year = postsyear.split("/")
    if int(posts_year[0]) >= 2015:
        stitle = posts[i]["stitle"]
        newlist.append(stitle)

        alladdress = posts[i]["address"].split()[1]
        address = alladdress[0:3]
        newlist.append(address)

        longitude = posts[i]["longitude"]
        newlist.append(longitude)

        latitude = posts[i]["latitude"]
        newlist.append(latitude)

        piccount = posts[i]["file"].count('https')
        allpath = posts[i]["file"].split("https:", piccount)[1]
        path = "https:"+allpath
        newlist.append(path)

        #list = stitle+','+address+','+longitude+',' + latitude+','+path
        # print(list)


with open('data.csv', 'w',  encoding="utf-8", newline='') as file:  # newline避免空行
    writer = csv.writer(file)
    cnt1 = 0
    cnt2 = 5
    for i in range(len(newlist)):
        if i % 5 == 0:
            writer.writerow(newlist[cnt1:cnt2])
            cnt1 += 5
            cnt2 += 5
        else:
            pass
