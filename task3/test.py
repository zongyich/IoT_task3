import json

if __name__ == '__main__':
    f = open('data.json')
    data = json.load(f)
    print(data)
    f.close();
