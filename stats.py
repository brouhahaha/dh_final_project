import json


def open_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

def write_json(js, f):
    with open(f, 'w', encoding='utf-8') as f:
        f.write(json.dumps(js, ensure_ascii=False))
    print('File successfully written.')


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
            if t in item:
                if t == 'sexLabel':
                    data[itemLabel][t] = item[t]
                elif t == 'death_year':
                    data[itemLabel][t] = item[t][:4]
                elif t in data[itemLabel]:
                    if data[itemLabel][t] and item[t] not in data[itemLabel][t]:
                        data[itemLabel][t].append(item[t])
                else:
                    data[itemLabel][t] = [item[t]]
            else:
                data[itemLabel][t] = None  
    return data
            
            
            

def main():
##    data = open_json('net.json')
##    with open('test.json', 'w', encoding='utf-8') as f:
##        f.write(json.dumps(data[:100]))
    data = open_json('net.json')
    write_json(make_unique_names(data), 'results.json')
    


if __name__ == '__main__':
    main()
