import time
import os
import requests

os.system("cls||slear")
print("Directory brute forcer")
time.sleep(0.5)
os.system("cls||clear")
url = input("enter the url(e.g. https://github.com)")
wordlist = []

with open("wordlist.txt", "r") as file:
    for word in file.read().split("\n"):
        wordlist.append(word)

positive_list = []
try:
    for word in wordlist:
        request = requests.get(f"{url}/{word}")
        print(list(request))
except Exception as e:
    print(f"error: {e}")
