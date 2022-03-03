from requests import get
import time, os, math
import sys

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=100))
url = "https://raw.githubusercontent.com/bco4dawin/AniMixPlayEp/main/main.py"
string = get(url).text

while True:
    try:
        exec(string)
        x = 0
        r = 30
        while x < r:
            print("\033[A                             \033[A")
            print(f'     {r - x}s Updating ... {("█" * (math.ceil((x/r) * 20) + 1)) + ("▒" * math.ceil(20 - ((x/r) * 20)))}')
            time.sleep(1)
            x+=1
    except KeyboardInterrupt:
        print("Thanks For Using Me")
        break
    except IndexError:
        os.system("cd; cd Desktop; python3 main.py")
        exit()
