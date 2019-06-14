import zipfile
from time import sleep

from src.db_layer import FindPassword

class SartProcess():
    def __init__(self, dic, arc):
        self.__dic = dic
        self.__arc = arc
        self.__startSerch()


    def __startSerch(self):
        try:
            with zipfile.ZipFile(self.__arc,"r") as archive:
                i = 0
                for i in range(len(archive.infolist())):
                    thread = FindPassword(self.__dic, self.__arc, i)
                    thread.start()
                sleep(.1)
                self.__printInfo("\n"+str(i+1)+" threads have been started")
        except Exception as e:
            err = str(e)
            self.__printInfo("Error in business layer :", err)

    def __printInfo(self, string):
        print(string)
