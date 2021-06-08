class DataLakeFacade():
    def getBasicData(self):
        Professor().getProfessorData()
        Calendar().getCalendarData()

    def getCollegeData(self):
        Class().getClassData()
        Subject().getDidaticSubject()

class TeachingPlanBasicData():
      _facade: DataLakeFacade

    def __init__(self):
        self._facade = DataLakeFacade()

    def getBasicData(self):
        self._facade.getBasicData()
        # Before:
        # DataLakeSubsystem().Professor().getProfessorData()
        # DataLakeSubsystem().Calendar().getCalendarData()
        
class TeachingCollegeData():
    
      _facade: DataLakeFacade

    def __init__(self):
        self._facade = DataLakeFacade()

    def getCollegeData(self):
        self._facade.getCollegeData()
        # Before:
        # DataLakeSubsystem().Class().getClassData()
        # DataLakeSubsystem().Subject().getDidaticSubject()
  
class TeachingPlanGenerator():

    def run(self):
        TeachingPlanBasicData().getBasicData()
        TeachingCollegeData().getCalendarData()