class Set:
    def __init__(self, set):
        self.__set = set

    def average(self):
        if len(self.__set) == 1:
            return (self.__set[0])
        elif len(self.__set) == 2:
            return (self.__set[0] + self.__set[1]) / 2
        else:
            return None
