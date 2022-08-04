import json
from update import update_json

store="muthumani stores"
def main():
    update_json()
    with open('data.json', 'r') as f:
        data = json.load(f)
        groceries = data.get(store)["grocery"]
        print("Grocery Items:\n")
        for item in groceries:
            print(item.capitalize())
        oils = data.get(store)["oils"]
        print("\nOils:\n")
        for oil in oils:
            print(oil.capitalize())
        address = data.get(store)["address"]
        storetimimg ="From {}- to {}".format( data.get(store)["opens"], data.get(store)["closes"])
        print("Address of the Store:", address)
        print("Store Open and Closing Timimg:", storetimimg)
        print("Danke for visiting us")



if __name__ == "__main__":
    main()