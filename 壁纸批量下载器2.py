from lxml import etree
import requests
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"}
url='https://www.bizhihui.com/'
response = requests.get(url,headers)
response.encoding='utf-8'
#print(response.status_code)

tree = etree.HTML(response.text)
pics=tree.xpath('//div[@class="container p-top"]//img/@src')
print(pics)
n=0
print(pics)
for pic in pics:
    n=n+1
    pic_url = pic.replace('-pcthumbs', '')
    print(pic_url)
    # 下载图片时带上 headers
    with open(f"bizhi{n}.jpg", "wb") as f:
        f.write(requests.get(pic_url, headers=headers).content)