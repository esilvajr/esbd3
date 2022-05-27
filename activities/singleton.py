class DatabaseConnection:

    _instance = None
    _data = None

    @classmethod
    def instance(cls): 
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def setAssignmentGrade(cls, student: str, course: str, assignment: str):
        cls._data = "Aluno:" + student + " , Curso: " + course + " , Grade: " + assignment 

    def getAssignmentGrade(cls):
        return cls._data


if __name__ == "__main__":
    
    databaseObjectA = DatabaseConnection.instance()
    databaseObjectB = DatabaseConnection.instance()

    databaseObjectA.setAssignmentGrade("John", "MBA", "Grade A")

    if (databaseObjectA.getAssignmentGrade().__eq__(databaseObjectB.getAssignmentGrade())):
        print("true")