# behavioral/singleton.py

class Singleton:
    """
    An example of Singleton OOPs design pattern.
    """
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception("Singleton class doesn't initiate more than an instance.")


    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
