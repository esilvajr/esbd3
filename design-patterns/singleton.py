class Singleton:

    _instance = None
    
    @classmethod
    def instance(cls): #cls == class
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance