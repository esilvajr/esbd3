class Office():
    def open(self):
        raise NotImplemetedError

class Word(Office):
    def open(self):
        print("Opening word")

class NewWord(Word):
    def open(self):
        print("Opening new release from word")

class Excel(Office):
    def open(self):
        print("Opening excel")

class NewExcel(Excel):
    def open(self):
        print("Opening new release from excel")

class Powerpoint(Office):
    def open(self):
        print("Opening powerpoint")

class Project(Office):
    def open(self):
        print("Opening project")

class OfficeFactory():
    def create(self):
        raise NotImplemetedError

class WordFactory(OfficeFactory):
    def create(self, version: int) -> Word:
        if (version != 'docx'):
            return Word()
        else: 
            return NewWord()

class ExcelFactory(OfficeFactory):
    def create(self, version: int) -> Excel:
        if (version != "xlsx"):
            return Excel()
        else: 
            return NewExcel()

class PowerpointFactory(OfficeFactory):
    def create(self) -> Powerpoint:
        return Powerpoint()

class ProjectFactory(OfficeFactory):
    def create(self) -> Project:
        return Project()


if __name__ == '__main__':
    word = WordFactory().create('doc')
    word.open()
    ...
    newword = WordFactory().create('docx')
    newword.open()
    ...
    excel = ExcelFactory().create('xls')
    excel.open()
    ...
    newexcel = ExcelFactory().create('xlsx')
    newexcel.open()
    ...
    powerpoint = PowerpointFactory().create()
    powerpoint.open()
    ...
    project = ProjectFactory().create()
    project.open()
    ...