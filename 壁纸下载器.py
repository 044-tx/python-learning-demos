#https://img1.baidu.com/it/u=430628254,4023808270&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=889
#https://gips2.baidu.com/it/u=2523203213,157420389&fm=3074&app=3074&f=PNG?w=1440&h=2560
#https://gips1.baidu.com/it/u=490433254,1579125907&fm=3074&app=3074&f=PNG?w=2560&h=1440
def bizhi():
    import requests


    url=input('wangzhi:')
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"}
    response=requests.get(url,headers)
    print(response)
    with open('壁纸.jpg','wb') as f:
        f.write(response.content)

bizhi()
