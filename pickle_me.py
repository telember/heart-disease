import pickle

def storeData():
     Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak', 'age':21, 'pay': 40000}
     Jag = {'key': 'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay':50000}

     db = {}
     db['Omkar']= Omkar
     db['Jagdish']= Jag

     dbfile= open('examplePickle','ab')

     pickle.dump(db, dbfile)
     dbfile.close()

def loadData():
    dbfile = open('examplePiclke','rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()

if __name__ == '__main__':
    storeData()
    loadData()