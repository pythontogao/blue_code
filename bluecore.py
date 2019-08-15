import urllib.request
import json

# 获取页面
def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


# 保存页面
def saveHtml(file_name, file_content):
    with open(file_name.replace('/', ' ') + ".html", "wb") as f:
        f.write(file_content)


url = 'http://www.bluecore.com.cn/'
html = getHtml(url)
saveHtml('bulecore_Html', html)
print('下载成功')


