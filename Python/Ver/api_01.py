import requests , json

reasponse = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&tagged=python&site=stackoverflow')
#print(reasponse.json()['items'])

for data in reasponse.json()['items']:
    print(data['title'])
    print(data['link'] + '\n')