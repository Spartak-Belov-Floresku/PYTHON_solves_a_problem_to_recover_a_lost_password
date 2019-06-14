import zipfile
import zlib
import threading

class FindPassword(threading.Thread):
    def __init__(self, dic, arc, num):
        threading.Thread.__init__(self)
        self.__dic = dic
        self.__arc = arc
        self.__num = num

    def run(self):
        self.__activateProcess()

    def __activateProcess(self):
        with zipfile.ZipFile(self.__arc, "r" ) as archive:
            zipFile = archive.infolist()[self.__num]
            self.__printInfo("\nProcessing file : "+zipFile.filename)
            with open(self.__dic) as corpus:
                for line in corpus:
                    word = line.strip().encode("ASCII")
                    try:
                        with archive.open(zipFile, 'r', pwd=word) as member:
                            member.read()
                            self.__printInfo("\nPassword found '"+str(word)+"' for "+zipFile.filename)
                    except (RuntimeError, zlib.error, zipfile.BadZipFile):
                        pass
    def __printInfo(self, string):
        print(string)
        
