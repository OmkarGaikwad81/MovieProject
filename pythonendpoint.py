import urllib.request,json
with urllib.request.urlopen("mongodb://localhost:27017") as url:
    data = json.loads(url.read().decode())
    for i in data:
        print("name: ",i['name'])
        print("img : ",i['img'])
        print("summary: ",i['Summary'],"\n")