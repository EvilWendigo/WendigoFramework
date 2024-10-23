import os
if not 'SUDO_UID' in os.environ.keys():
    print("Try running this program with sudo.")
    exit()
os.system("figlet Wendigo")
os.system("figlet FrameWork")
print("1|bettercap")
print("2|sqlmap")
print("3|spiderfoot")
print("4|wifite")
print("5|recon-ng")
print("6|WendigoCracker")
print("7|WendigoScrape")
print("8|WendigoDeauth")

while True:
    console = input("Wendigo>>> ")
    if console == "1":
        print("enable monitor mode: Y/N")
        mon = input("Wendigo> ")
        if mon == "Y":
            os.system("sudo airmon-ng start wlan0")
            os.system("sudo bettercap -iface wlan0mon")
            os.system("sudo airmon-ng stop wlan0mon")
            print("exited monitor mode")
        if mon == "N":
            print("started bettercap without ")
            os.system("sudo bettercap -iface wlan0")
    if console == "2":
        os.system("sqlmap --wizard")
    if console == "3":
        os.system("spiderfoot -l 127.0.0.1:5001")
    if console == "4":
        os.system("sudo wifite")
    if console == "5":
        os.system("recon-ng")
    if console == "6":
        os.system("python3 WendigoTools/WendigoCracker.py")
    if console == "7":
        os.system("python3 WendigoTools/WendigoScrape.py")
    if console == "clear":
        os.system("clear")
        
    if console == "8":
        os.system("python3 WendigoTools/WendigoDeauth.py")
        os.system("sudo airmon-ng stop wlan0mon")