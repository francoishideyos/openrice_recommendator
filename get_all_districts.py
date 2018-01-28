import requests, json, pandas as pd

# fake to become a browser
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

alias      = []
count      = []
typeof     = [] 
identifier = []
name       = []
searchkey  = []

r = requests.get("https://www.openrice.com/api/pois?uiLang=en&uiCity=hongkong&page=2&&sortBy=Default", headers = headers)
result = json.loads(r.text)
for i in result['searchResult']['refineSearchFilter']['locations']:
    alias.append(i['aliasUI'])
    count.append(i['count'])
    typeof.append(i['filter'])
    identifier.append(i['id'])
    name.append(i['name'])
    searchkey.append(i['searchKey'])

df = pd.DataFrame([alias,count,typeof,identifier,name,searchkey]).transpose()
col = ['aliasUI','Count','Type','ID','Name','Search Key']
df.columns = col 

df.to_csv('assets/data/all_districts.csv',encoding='utf-8',index=False)