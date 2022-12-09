from zipfile import ZipFile


def main():

    with ZipFile('./archive.zip', 'r') as zipObj:
        listOfFileNames = zipObj.namelist()
        for fileName in listOfFileNames:
            if fileName.endswith('.csv'):
                zipObj.extract(fileName, 'temp_csv')
if __name__ == '__main__':
    main()
