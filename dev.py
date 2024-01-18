from requests_html import HTMLSession

session = HTMLSession()

proxy = "http://127.0.0.1:2080"

with open('../cook', 'r') as f:
    cookies = dict(cookies_are = f.read())

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'referer': 'https://osu.ppy.sh/beatmaps/packs', 'host': 'osu.ppy.sh'}

link = dict()
r = session.get(f"https://osu.ppy.sh/beatmaps/packs/S1283", cookies=cookies, headers=headers, proxies={'http': proxy, 'https': proxy})
link_raw = r.html.find('div.beatmap-pack-description', first=True).find('a') # 下载链接
for a in link_raw:
    links = a.absolute_links
print(links)
