#导入模块
import time
import requests
import random
from bs4 import BeautifulSoup
#开始信号
print("正在开始必应爬虫")
#获取url
url="https://cn.bing.com/search"
#目标以及页数
name=input("请输入要查询的内容：")
page1=int(input("请输入起始页："))
page2=int(input("请输入终止页："))#建议小于5页
#请求头
Ualist=["Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1 Edg/145.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36 Edg/145.0.0.0"]
cookie_str="MUID=3A184E04940467EF1A3C5807954E66D4; MUIDB=3A184E04940467EF1A3C5807954E66D4; SRCHD=AF=ANSPA1; SRCHUID=V=2&GUID=DFF8267CB8434FC5883D4F28DC059902&dmnchg=1; MMCASM=ID=E77A56B6800543AAA73DE71B78ADEE22; _tarLang=default=zh-Hans; _TTSS_IN=hist=WyJlbiIsImF1dG8tZGV0ZWN0Il0=&isADRU=0; _TTSS_OUT=hist=WyJ6aC1IYW5zIl0=; _clck=11q7012%5E2%5Efyu%5E0%5E2062; _UR=QS=0&TQS=0&Pn=0; BFBUSR=BFBHP=0; _Rwho=u=d&ts=2026-03-09; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNi0wMy0wOVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjo4LCJUb2JuIjowfQ==; ipv6=hit=1773069259616&t=4; BFPRResults=FirstPageUrls=FFBB94D1D827BF6D1C2DBF5222764318%2C8C1205BDA016FAEF571889B521F89C90%2C9A443E053C4F1480435A20C27C0FA5BF%2C5DE0C280CEB4B58DE35548E02D73CD88%2CBF3E48D6EDBDFBE8C6BC4B5DE4158083%2C2941C55247D1ED569A32A8F79AE40592%2C179A72D903FA7BAB24C0FDE9020C6537%2CA6D01819A0E5E573DB21555757889F52%2C562FBF7A6BAD87DF8CBDA5E36C9431D0%2C71E2C1C20855BBBBCB11F81101E1188F&FPIG=4071C7132EA64329A03D6C44002127DE; SRCHUSR=DOB=20250606&DS=1&POEX=W; .MSA.Auth=CfDJ8HAK7eZCYw5BifHFeUHnkJEp9RrvvdhKxs5sFhO5FE_N9v76t9lNHT5Bugs2liZIJJVtd260V2XlXW_2NnKEG34pqoBXQtlQxxDTdnz0uab-q1SlMk-YE_vIvOrByKohO3Nk7FC4TBt6uV_DWj_okkkwIty8zc4F_hX66GZrE25Uyqa6XH_CG491FOeUNIKaIeIhHfKjG-3dDW2L05dy8C0Fb4ac5gBoDzgtKorwYuvssKDrLPu014QnL8b4ZuAZ9MfkD-ksnUihFgSyHtbHdb_tFWRAmN1JId1m5DvP1C1GMVz3Ofi7RDT-fA5e74H4AkEozuv5H9KfK3D4593p0_92_CGaoTYvTTW2751CEUEb06ePKg0aOTBNDMGxmij5JP95strnj1MvcIwDg01R_5aq4ue-YYpxueCYAXJxIjoF3lxGXzn7i_nPt_h74zt-y8lxkmb4W5_Aw97blkDZ9NoPfDGXfisCtrs3Tlbh-kC6eHU79Ln5-KwNeTNW7d8NUF__g-4e-oD1qCJaB1pWwpRmLuMEGj6xbAMxR_-eXmTtJ-P9eHTSXdUSYzcl7xnofAlbLiTf8cFYpJAcBp6Wb4GWoGebECtwlhYG4wneTK_us4XoKFhLNb-FKj9DxcnqBK4pnzsDdAMYrR37ev1EvCReaTlnnrTm4vwE7yuB8_kSx-lzNpLBLKd9lSmHA3d1Grm9AacbOgrDo14jtWGztaHIlZRzAmGBAe4-K_qV3NtcFYpryWUcZfFfn7x4E9xp073f4OfXOYWuka2MTloFNV4WrfHDGx9d1ylmzvBDF3hHHMUdRJ6eDsu5gkkdsEtRTGllBR3JD2Mn2_B4HcH-NhdTBafmOJrdZwaNpAtxvEC45OZNo0llKZp2Wd45zu5MymiUm7l_Ra5kBiRJHptrYeii83UjVvJxv9J2MRK4zVnymexYUOCl0A1tTqgvpFlEjg; _U=1sOYD9N_2gZ-iybM2Rmju5rZHgH4zHN_VuD65pvtF-3h6I6O6PyfjcIaEkY6VMjd_331YjoQlZIDSN2goN-iH_YVkHa5pMn1N7qEgJ9lrgsq8P2X75zMZB6_YPSSs2ijHOiaFWAdk8zDiuj1cPA1aImUbbZGYJGh9y0dIh9SsIVPJdv61q8fofBwnhS2boIVlhqlu-Xn8yuk2fmTnZjT8rA; ANON=A=2263C6A68915716ED6DA71E4FFFFFFFF; _MsaRef=RT=1773069866310; _EDGE_S=SID=3D80677CBEC863BF1B26706BBFE662CD; WLS=C=81edc30dc8c4c040&N=sdwad; USRLOC=HS=1&ELOC=LAT=36.85231399536133|LON=117.93025207519531|N=%E5%91%A8%E6%9D%91%E5%8C%BA%EF%BC%8C%E5%B1%B1%E4%B8%9C%E7%9C%81|ELT=2|&CLOC=LAT=36.85231497395023|LON=117.93025033193426|A=733.4464586120832|TS=260309142242|SRC=W&BID=MjYwMzA5MjIyMjQwXzRmMzYyY2YzM2Q1NzMwYWY2MjJiOTgzMzIxM2Y4YWIwZTg1YmE0MDk0Mzk5MGNkNWZjMDBiOTJkZWRkOTJmZjQ=; GC=bnWT1hrZmHto3AYjsVSu7PpWiWr4PMjRKM-F15AULrX0z7_3GV_RhmJxXJvRSLaEoLYhoJc0wDU-dZOaKDT4xg; _RwBf=r=0&ilt=164&ihpd=3&ispd=12&rc=51&rb=51&rg=0&pc=200&mtu=0&rbb=0.0&clo=0&v=16&l=2026-03-09T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=-62135539200&rwflt=1747518986&rwaul2=0&g=newLevel1&o=0&p=MSAAUTOENROLL&c=MR000T&t=3249&s=2025-04-10T15:10:57.4639645+00:00&ts=2026-03-09T14:24:30.8081192+00:00&rwred=0&wls=0&wlb=0&wle=1&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&cid=0&gb=2025w17_u&W=1&mta=0&e=w7CSqi3LgI8lNMyGWeuOrnAihsN2fpAW3TOkKwOuzMdCBJTGy3CDW6TBnNwSaMYOWN0R2cQqrxS6RRzwwNFLhg; _SS=PC=U531&SID=327E7A492F07690813D56D5E2E616874&R=51&RB=51&GB=0&RG=0&RP=200; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=19.0.0&BZA=0&DM=0&BRW=M&BRH=M&CW=1280&CH=800&SCW=1280&SCH=2776&DPR=1.3&UTC=480&PRVCW=1528&PRVCH=779&EXLTT=31&HV=1773066292&HVE=CfDJ8HAK7eZCYw5BifHFeUHnkJGmR5foa8FzyNDG3e3_zpDqqlxARHKoSUXnxcKv-IE5RV8wgJw2tGK9Xe1Sj_fL8G6ThgXyEQ4z7CupayrGcKw8be9ZjblaOhCKB_XRnyzGpIfw71_2J04PUYOMCa2rnHdYepNoqB3Ru0V7zl6geNDFjlegYsRSqocoQDd-F1iKtA&WTS=63885748531&AV=14&ADV=14&RB=0&MB=0&PREFCOL=0&B=0&P=CfDJ8BJecyNyfxpMtsfDoM3OqQs2XIy2Eji2Zd68NfWycphKB40Ht8l4ewTG69DC-WYOUr_-qavIOvTRyMgLh2dI5Oz85fZjqD_SDRxeL09m1N2IBzYEMiCGjRv339Q-XGbyZSLCPz9phXp92IT1zftgV1vzVN2JKaEjCQG9Br2dlH-BE_QXCS9Is7-l-I7iZq33MQ1&PR=2.0000000298023224&OR=0"
#获取响应
for i in range(page1,page2+1):
    params={"q":name,
            "first":(i-1)*10,
            "count":10,
            "form":"PERE"
            }#规定相应内容与页数
    headers={"User-Agent":random.choice(Ualist),"cookie":cookie_str,"Referer":"https://cn.bing.com/", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",  # 必应校验的关键头
        "Connection": "keep-alive"}#随机选取请求头
    res=requests.get(url,params=params,headers=headers,timeout=10)#获取响应内容
    time.sleep(random.randint(3,6))#间隔时间随机3到6秒
    soup=BeautifulSoup(res.text,"html.parser")
    # 拿到 soup 之后：
    results = soup.find_all("li", class_="b_algo")  # 匹配所有结果项
    for item in results:
        # 先找 h2，再找里面的 a
        h2_tag = item.find("h2")
        if h2_tag:
            a_tag = h2_tag.find("a", target="_blank")
            if a_tag:
                title = a_tag.text.strip()
                print(title)
                print("-" * 30)
