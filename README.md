# osupack download link

```python
pip install requests_html pyyaml # only main.py
pip install pandas openpyxl # only cover.py
```
## config

```yaml
database:
  type: S              #曲包类型。e.g. S/SM/ST/SC
  star: 1283           #开始编号
  andy: 1289           #截止编号
  time: 2              #最长延迟时间 (秒/s). 防止触发反爬
  cookie: ./file       #osu 登录 cookies 文件
  dlpath: .            #下载目录
  outjson: output.json #输出文件名 (.json)
  proxy: http://127.0.0.1:2080 # 支持 http 代理
```