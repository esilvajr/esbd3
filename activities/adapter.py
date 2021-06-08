class Client():
    
    def processData(myJsonData: MyJsonData):
        jsonData = myJsonData.getData()
        myJsonData.cleanData(jsonData)

class JsonAdapter(MyJsonData):

    _docFormat: DocFormat

    def __init__(self, docFormat: DocFormat) -> None:
        self._docFormat = docFormat

    def getData(self) -> JsonData:
        docData = self._docFormat.getDocData()
        jsonData = convertInJson(docData)
        return jsonData

    def cleanData(self, jsonData: JsonData) -> None:
        docData = convertInDoc(jsonData)
        self._docFormat.clean(docData)
        jsonData = convertInJson(docData)
        
if __name__ == "__main__":

    docFile = DocFormat(x, y, z)
    jsonAdapter = JsonAdapter(docFile)
    client = Client()
    client.processData(jsonAdapter)
