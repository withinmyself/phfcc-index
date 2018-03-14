import requests
import json



verse = requests.get('bibles.org/v2/chapters/eng-KJVA:1Cor.2/verses.js?include_marginalia=false', \
					auth=('wkVqgrZryPrFdxXIYfuUpoCyUW4LkoArNcs16Q5w', ''))
json_verse = json.loads(verse)
print(json_verse)