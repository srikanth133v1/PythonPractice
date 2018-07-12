#import urllib2
from urllib.request import urlopen
import json

stks = ["AAPL", "F"]

for stk in stks:
    url  = "https://finance.google.com/finance?q=NASDAQ:"+stk +"&output=json"
    #gf = urllib2.urlopen(url).read()
    with urlopen(url) as f:
        gf = f.read().decode('utf-8')
        #print(gf)
        gf = gf.replace("//","")
        json_data = json.loads(gf)[0]
        price = json_data["financials"][0]["f_figures"][0]["ttm"].replace('"', '\\"')
        print(price)