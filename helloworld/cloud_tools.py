from tkinter.constants import FALSE
import cloudconvert
import sys
import os

class CloudInstance:
    testName = 'New Cloud Item'

    def __init__(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, '../Data/key.txt')
        with open(filename, 'r') as key:
            cloudconvert.configure(api_key = key.read, sandbox = FALSE)

    def convert(self):
        print("Enter filename then extension. Press enter when finished")
        response = "y"
        tuples = list()
        while response != 'n':
            filedir = input('File Location: ')
            filetype = input('Extension: ')
            tuples.append((filedir, filetype))
            response = input('Add Another? ')
        for a in tuples:
            print(a)



            


def toolTester():
    cvt = CloudInstance()
    ans = input("Convert a File? Y/N ")
    if ans.lower() == 'n':
        quit()
    else:
        if ans.lower() == 'y':
            cvt.convert()
        else:
            toolTester()


        




if __name__ == '__main__':
    print('Cloud Converter V.1')
    toolTester()