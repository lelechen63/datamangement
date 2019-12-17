import json
import os
import re
import pickle

def read_folder():
    datapath = './metadata'
    all_file = []
    for (root,dirs,files) in os.walk(datapath): 
            # print (root) 

            # print (dirs) 
            if len(files) != 0:
                all_file.append(os.path.join(root, files[0]))
            # print ('--------------------------------')
    with open('./pickle/all_file.pkl', 'wb') as handle:
                pickle.dump(all_file, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return all_file

def splitnonalpha(s):
    pos = 1
    while pos < len(s) and s[pos].isalpha():
        pos+=1
    return (s[:pos], s[pos:])

def read_txt(all_file):
    for js_file in all_file:
        data_reprensent = []
        with open(js_file) as fp:
            line = fp.readline()

            data_reprensent =  re.sub('[^A-Za-z0-9]+', ',', line).lower()

        data_reprensent = data_reprensent[1:-1].split(',')
        data_reprensent = set(data_reprensent)
        with open(js_file.replace('json','pkl'), 'wb') as handle:
            pickle.dump(list(data_reprensent), handle, protocol=pickle.HIGHEST_PROTOCOL)


def read_json(all_file):
    for js_file in all_file:
        with open( js_file ) as json_file:
            data = json.load(json_file)
            print (data)
            # print (data['resource']['columns_name'])
            # print (data['resource']['columns_description'])
            # print (data['resource']['description'])
            # print (data['classification']['domain_tags'])
            # print (data['classification']['domain_metadata'])
            # print (data['classification']['domain_category'])
            
            for key in data.keys():
                pass
                
        # break

all_file = read_folder()
read_txt(all_file)