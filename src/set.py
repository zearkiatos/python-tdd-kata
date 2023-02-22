class Set:
    def __init__(self, set):
        self.__set = set

    def average(self):
        if len(self.__set) == 1:
            return (self.__set[0])
        else:
            return None