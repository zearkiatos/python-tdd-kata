class Set:
    def __init__(self, set):
        self.__set = set

    def average(self):
        if len(self.__set) > 0:
            return sum(self.__set) / len(self.__set)
        else:
            return None
