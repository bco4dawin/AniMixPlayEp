from requests import get
import time, os
url = "https://raw.githubusercontent.com/bco4dawin/AniMixPlayEp/main/main.py"
string = get(url).text

while True:
    try:
        exec(string)
        x = 0
        while x < 300:
            print("\033[A                             \033[A")
            print(f'     {300 - x} Seconds Until Next Update.')
            time.sleep(1)
            x+=1
    except KeyboardInterrupt:
        print("Thanks For Using Me")
        break
    except IndexError:
        os.system("cd; cd Desktop; python3 main.py")
        exit()
