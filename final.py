from grobid_client.grobid_client import GrobidClient
from bs4 import BeautifulSoup
import os
from nltk.tokenize import sent_tokenize

client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", "./resources/test", output="./",
               consolidate_citations=True, tei_coordinates=True, force=True)
ans = " "
possibles = []
freq = {}


def dataset(str):
    words = str.split()
    for word in words:
        if word.isupper():
            possibles.append(word)

    for item in possibles:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1


def out(freq):
    datasets = max(freq, key=lambda x: freq[x])
    print("Datasets used is:  ------------------------")
    print(datasets)


items = ["dataset", "trained", "database", "experiments", "evaluated"]


def check(str, count):
    x = str.split(".")
    for i in range(len(x)):
        test = x[i]
        count = 0
        flag = False
        for j in range(len(items)):
            if (items[j] in test):
                count += 1
                if (count >= 1):
                    print(test)
                    dataset(test)


search = True


def extract(data):
    for info in data:
        ans = str(info.text)
        cnt = 0
        if (search):
            flag = check(ans, cnt)


path = './resources/test_out'
for file in os.listdir(path):
    possibles.clear()
    freq.clear()
    if file.endswith(".tei.xml"):
        with open(file, 'r') as f:
            temp = f.read()
        soup = BeautifulSoup(temp, 'xml')
        data = soup.find_all('p')
        extract(data)
        out(freq)
        print("\n\n\n\n")
    else:
        continue
