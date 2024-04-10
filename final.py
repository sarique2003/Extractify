import os
import spacy
from bs4 import BeautifulSoup

nlp = spacy.load("en_core_web_sm")  # Load spaCy's English language model

def dataset(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "ORG":  # Check if entity is an organization
            possibles.append(ent.text)

    for item in possibles:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

def out(freq):
    datasets = max(freq, key=lambda x: freq[x])
    print("Datasets used is: ------------------------")
    print(datasets)

items = ["dataset", "trained", "database", "experiments", "evaluated"]

def check(text, count):
    x = text.split(".")
    for i in range(len(x)):
        test = x[i]
        count = 0
        flag = False
        for j in range(len(items)):
            if items[j] in test:
                count += 1
                if count >= 1:
                    print(test)
                    dataset(test)

search = True

def extract(data):
    for info in data:
        ans = str(info.text)
        cnt = 0
        if search:
            flag = check(ans, cnt)

path = './resources/test_out'
for file in os.listdir(path):
    possibles = []  # Clear possibles list for each file
    freq = {}  # Clear freq dictionary for each file
    if file.endswith(".tei.xml"):
        with open(os.path.join(path, file), 'r') as f:
            temp = f.read()
        soup = BeautifulSoup(temp, 'xml')
        data = soup.find_all('p')
        extract(data)
        out(freq)
        print("\n\n\n\n")
    else:
        continue
