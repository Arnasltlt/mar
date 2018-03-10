# -*- coding: utf-8 -*-
import json
import yaml

with open('/Users/Arnoldas/Documents/GitHub/mar/_data/mariusvalaitis.json', encoding='utf8') as f:
    data = json.load(f)

web_data = []
n = 0

# print(data['posts'][24]['slug'])
# print(data['posts'][24]['photos'][0]['photo-url-250'])
# print(data['posts'][24]["photo-caption"])




for post in data['posts']:
        try:
                name = data['posts'][n]['slug']
                product = data['posts'][n]['slug']
                thumbnail = data['posts'][n]['photos'][0]['photo-url-250']
                description = data['posts'][n]["photo-caption"]
                picture1 = data['posts'][n]['photos'][0]["photo-url-1280"]
                picture2 = data['posts'][n]['photos'][1]["photo-url-1280"]
                fotkes = []
                for picture in data['posts'][n]['photos']:
                    fotkes.extend(('image: ' + picture["photo-url-1280"], 'image-small: ' + picture['photo-url-250'], 'caption: ' + picture['caption']))

                zodynas = {}
                nuotraukos = {}
                # print('Name:' + " " + name)
                # print('Product:' + " " + product)
                # print('Thumbnail:' + " " + thumbnail)
                # print('Description:' + " " + description)
                # print('Nuotraukos:')
                zodynas['name'] = name
                zodynas['product'] = product
                zodynas['thumbnail'] = thumbnail
                zodynas['description'] = description
                nuotraukos['nuotrauka'] = fotkes
                zodynas['Nuotraukos'] = nuotraukos
                web_data.append(zodynas)
                n = n+1
        except (ValueError, KeyError, TypeError):
                print("JsON format error")

# print(web_data[0])

#
# for post in data['posts']:
#     try:
#         item = {}
#         item['name'] = post['slug']
#         item['product'] = post['slug']
#         item['thumbnail'] = post['photos'][0]['photo-url-250']
#         item['description'] = post["photo-caption"]
#         item['nuotraukos'] = " "
#         web_data.append(item)
#         n = n + 1
#     except (ValueError, KeyError, TypeError):
#         print("JsON format error")

# print(web_data)
with open('/Users/Arnoldas/Desktop/test.json', 'w') as out:
    json.dump(web_data, out, indent = 2)
# with open('/Users/Arnoldas/Desktop/test.yaml', 'w') as out:
#     yaml.dump(web_data, out, indent = 2)
