from requests_html import HTMLSession
from tqdm import trange
import json,time,random,argparse,os

parser = argparse.ArgumentParser(description='help')
parser.add_argument('-y', dest='types', type=str, help='曲包类型. e.g. S/SM/ST/SC')
parser.add_argument('-f', dest='frst', type=int, help='开始编号')
parser.add_argument('-e', dest='end', type=int, help='截止编号')
parser.add_argument('-o', dest='out', type=str, help='输出文件名(.json)')
parser.add_argument('-t', dest='time', type=int, help='最长延迟时间(秒/s). 防止触发反爬')
parser.add_argument('-c', dest='cookies', type=str, help='osu登录cookies文件')
parser.add_argument('-p', dest='output', type=str, help='下载目录')
args = parser.parse_args()

session = HTMLSession()

with open(args.cookies, 'r') as f:
    cookies = dict(cookies_are = f.read())

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}

link = dict()

for i in trange(args.frst, args.end+1):
    try:
        time.sleep(random.uniform(1,args.time))
        r = session.get(f"https://osu.ppy.sh/beatmaps/packs/{args.types}{i}", cookies=cookies, headers=headers)
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
    # os.system(f"mega-get {list(links)[0]} {args.output}") on Windows
    # os.system(f"mega-exec get {list(links)[0]} {args.output}") on Linux

with open(args.out, "w") as f:
    json.dump(link, f, indent=4)
