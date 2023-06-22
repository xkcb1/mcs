#reader <- CommonHelper
class StyleReader:
    @staticmethod
    def readQSS(style):
        with open(style,'r',encoding='utf-8') as f:
            return f.read()