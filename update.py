import json

def update_json():
    with open('data.json','r') as f:
        data=json.load(f)
        store = "muthumani stores"
        groc_list=data.get(store)["groc_list"]
        data.get(store)["grocery"].append(groc_list[-1])
        groc_list.pop()

    with open('data.json','w') as f:
        json.dump(data,f)