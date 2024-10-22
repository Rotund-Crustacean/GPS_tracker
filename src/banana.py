class Banana:

    def __init__(self,thing):
        self.thing = thing #instance variable

    def five_characters(self,input):
        return self.thing + input[0:5]

    @staticmethod
    def more_five_characters(input):
        return input[0:5]