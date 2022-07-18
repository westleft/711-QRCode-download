import json

class JsonReader():
    def __init__(self) -> None:
        pass

    def readJson(self, filePath):
        with open(filePath, "r" ,encoding="utf-8") as f:
            self.data = json.load(f)

    def getReceiverName(self):
        arr = []
        for item in self.data['receiver']:
            arr.append(item['Name'])

        return arr

    def filterData(self, name):
        filtered = filter(lambda item: item['Name'] == name, self.data['receiver'])
        return list(filtered)[0]

jsonReader = JsonReader()


if __name__ == '__main__':
    jsonReader

jsonReader.readJson("data.json")
jsonReader.getReceiverName()