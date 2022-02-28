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

for i in range(10):
    str = f'    |  {episodes[i]}  '
    arr.append(epNum[i])
    epArr.append(str)
    arrNum.append(len(str))
    epGap.append(len(epArr[i]))

m = max(arrNum)
x = max([len(i) for i in epNum])
epM = [x - len(i) for i in epNum]
f = 0

for i in range(10):
    full = epArr[i] + (' ' * (m - len(episodes[i]))) + "|   " + arr[i] + (" " * epM[i]) + "   |   " + desc[i] + "    |"
    if f == 0:
        print(f'    ╭---------------╮\n    | New Episodes: |\n    ╰---------------╯\n\n    ╭{"-" * (m + x + len(desc[0]) + 12)}-------╮\n{"    |" + " " * (len(full)-6) + "|"}')
        f = 1
    print(full)
    if i < 9:
        split = "    |" + "-" * (len(full)-6) + "|"
    else:
        split = "    ╰" + "-" * (len(full)-6) + "╯"
    print("    |" + " " * (len(full)-6) + "|")
    print(split)

    if i < 9:
        print("    |" + " " * (len(full)-6) + "|")
    
print("\n     By: PFC Cruz Vazquez, Jeremy A.\n")
print()
