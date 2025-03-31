#if you want to make a full scan, replace wordlist_test.txt with wordlist.txt at line 14.
import time
import os
import requests

os.system("cls||slear")
print("DIRECTORY BRUTE FORCER")
time.sleep(3)
os.system("cls||clear")
url = input("enter the url(e.g. https://github.com)")
time_start = time.time()
wordlist = []

with open("wordlist_test.txt", "r") as file:
    for word in file.read().split("\n"):
        wordlist.append(word)

positive_list = []
try:
    for word in wordlist:
        response = requests.get(f"{url}/{word}")
        if response.status_code == 200:
            positive_list.append(f"{url}/{word}")
except Exception as e:
    print(f"error: {e}")

os.system("cls||clear")
print(10*"-","URL's in Positive_responses.txt",10*("-"))
with open("Positive_Responses.txt", "w") as positive_file:
    for url in positive_list:
        positive_file.write(f"{url}\n")

time_finish = time.time() - time_start
print(f"\nit took {round(time_finish, 2)}")