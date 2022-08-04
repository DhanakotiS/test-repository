import json

store="muthumani stores"
def main():
    with open('data.json', 'r') as f:
        data = json.load(f)
        groceries = data.get(store)["grocery"]
        for item in groceries:
            print(item.capitalize())



if __name__ == "__main__":
    main()