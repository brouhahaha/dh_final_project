import json


def open_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

##    {'itemLabel': 'Авраам-Бер Готлобер',
##     'langLabel': 'иврит',
##     'lang': 'http://www.wikidata.org/entity/Q9288',
##     'item': 'http://www.wikidata.org/entity/Q329845',
##     'death_year': '1899-04-12T00:00:00Z',
##     'sexLabel': 'мужской пол',
##     'occupationLabel': 'журналист',
##     'occupation': 'http://www.wikidata.org/entity/Q1930187',
##     'sex': 'http://www.wikidata.org/entity/Q6581097'}
def make_unique_names(raw_data):
    data = {}
    types = {'langLabel', 'death_year', 'sexLabel', 'occupationLabel'}
    for item in raw_data:
        itemLabel = item['itemLabel']
        if itemLabel not in data:
            data[itemLabel] = {}
        for t in types:
            if t in data[itemLabel]:
                if raw_data[itemLabel][t] != data[itemLabel][t]:
                    data[itemLabel][t] = set(raw_data[itemLabel][t]) | data[itemLabel][t]
                else:
                    data[itemLabel][t] = set(raw_data[itemLabel][t])
    return data
            
            
            

def main():
##  with open('test.json', 'w', encoding='utf-8') as f:
##  f.write(json.dumps(data[:100]))
    data = open_json('test.json')


if __name__ == '__main__':
    main()
