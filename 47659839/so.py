import os
import urllib.request as request
#import libxml2
from lxml import html

totalurl = "https://www.icc-ccs.org/index.php/piracy-reporting-centre/live-piracy-report"
htmlfile = request.urlopen(totalurl)
htmltext = htmlfile.read()
source = html.fromstring(htmltext.decode())
num = source.xpath('//div[@class="fabrikDataContainer"]')
new_content = str.encode(num[0].text_content(), 'utf8')
# print(new_content.decode('utf8'))
if os.path.exists('lastresult.txt'):
    with open('lastresult.txt', 'rb+') as f:
        last_content = f.read()
        if new_content != last_content:
            print("updated")
        f.seek(0)
        f.write(new_content)
        f.truncate()
else:
    with open('lastresult.txt', 'wb') as f:
        f.write(new_content)
