import cloudscraper
import re
from os import system

system("clear")

scraper = cloudscraper.create_scraper()

html = scraper.get("https://animixplay.to/").text
#print(html)

episodes = re.findall('<p class="name">(.*?)</p>',html)
epNum = re.findall("<p class=\"infotext\">(.*?)</p>", html)
desc = re.findall("<div class=\"timetext\">(.*?)</div>", html)
arr = []
epArr = []
arrNum = []
epGap = []

print("\n    | New Episodes: \n    ---------------\n")
for i in range(len(episodes)):
    str = f'    | {episodes[i]}  '
    arr.append(epNum[i])
    epArr.append(str)
    arrNum.append(len(str))
    epGap.append(len(epArr[i]))

m = max(arrNum)
x = max([len(i) for i in epNum])
epM = [x - len(i) for i in epNum]

for i in range(len(episodes)):
    full = epArr[i] + (' ' * (m - len(episodes[i]))) + "| " + arr[i] + (" " * epM[i]) + "   |   " + desc[i]
    print(full)
    print("    " + "-" * (len(full)-4))
print()
