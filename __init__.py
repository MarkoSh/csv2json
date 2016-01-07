__author__ = 'mark'

import json

with open("worldcitiespop.txt") as fp:
    dataset = {}
    for el in [line.strip().decode('iso-8859-1').split(',') for line in fp.readlines()[1:]]:
        el[0] = el[0].upper()
        el[3] = el[3].upper()
        if el[0] not in dataset:
            dataset[el[0]] = {
                el[3]: [{
                        "city": el[2],
                        "lat": el[5],
                        "lon": el[6]
                    }
                ]
            }
        else:
            if el[3] not in dataset[el[0]]:
                dataset[el[0]][el[3]] = [{
                        "city": el[2],
                        "lat": el[5],
                        "lon": el[6]
                    }
                ]
            else:
                dataset[el[0]][el[3]].append({
                        "city": el[2],
                        "lat": el[5],
                        "lon": el[6]
                    })

jsonstring = json.dumps(dataset)
with open("world_countryCode-regionCode-cities.json", "wb") as fp:
    fp.write(jsonstring)
for countryCode in dataset:
    with open("{}_regionCode-cities.json".format(countryCode), "wb") as fp:
        fp.write(json.dumps({countryCode: dataset[countryCode]}))
pass