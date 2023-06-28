from requests_html import HTMLSession
from tqdm import trange
import yaml,json,time,random,os

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

db_type = config['database']['type']
db_star = config['database']['star']
db_andy = config['database']['andy']
db_time = config['database']['time']
db_cookie = config['database']['cookie']
db_dlpath = config['database']['dlpath']
db_outjson = config['database']['outjson']

session = HTMLSession()

with open(db_cookie, 'r') as f:
    cookies = dict(cookies_are = f.read())

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}

link = dict()

for i in trange(db_star, db_andy+1):
    try:
        time.sleep(random.uniform(1,db_time))
        r = session.get(f"https://osu.ppy.sh/beatmaps/packs/{db_type}{i}", cookies=cookies, headers=headers)
        link_raw = r.html.find('div.beatmap-pack-description', first=True).find('a') # 下载链接
        for a in link_raw:
            links = a.absolute_links
        packname = r.html.find('div.beatmap-pack__name', first=True).text # 包名
        date = r.html.find('span.beatmap-pack__date', first=True).text # 发布时间
        user = r.html.find('span.beatmap-pack__author--bold', first=True).text # 发布负责人
        data = {
            #"id":  i,
            "name": packname,
            "date": date,
            "user": user,
            "download_link": list(links)[0]
        }
        link[i] = data
    except:
        t = r.html.find('p', first=True).text
        data = {
            #"id":  i,
            "name": t
        }
        link[i] = data
    os.system(f"aria2c -d {db_dlpath} {list(links)[0]}") # with aria2
    os.system(f"wget -P {db_dlpath} {list(links)[0]}") # with wget

with open(db_outjson, "w") as f:
    json.dump(link, f, indent=4)
