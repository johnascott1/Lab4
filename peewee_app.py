from peewee import *


db = SqliteDatabase('archery.sqlite')




class Archer(Model):
    name = CharField()
    nation = CharField()
    score = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'Name: {self.name}  Country: {self.nation}  Score: {self.score}'
#cur.execute('create table phones (brand text, version integer)')

#cur.execute('insert into phones values ("Android", 5)')
#cur.execute('insert into phones values ("iPhone", 6)')

#db.commit()
db.connect()
db.create_tables([Archer])

def main():

    while True:

        print("1) Add Contestant")
        print("2) Delete Contestant")
        print("3) Update Score")
        print("4) Search Contestant")
        print("5) Display All Contestants")
        print("6) Exit")

        selection = input("Please Select:")
        if selection == '1':
            add_contestantPW()
        elif selection == '2':
            delete_contestantPW()
        elif selection == '3':
            modify_scorePW()
        elif selection == '4':
            search_contestantPW()
        elif selection == '5':
            search_allPW()
        elif selection == '6':
            #db.commit()
            break
        else:
            print("Unknown Option Selected!")



def add_contestantPW():

    enterName = input("Enter the name")
    enterNation = input("Enter Nation:")
    enterScore = input("Enter score:")
    archer = Archer(name=enterName, nation=enterNation, score=enterScore)
    archer.save()
    #cur.execute('insert into archery_scores values (?, ?, ?)', (enterName, enterNation, enterScore))

def delete_contestantPW():
    deleteName = input("Enter the name of the contestant you wish to delete")
    rows_deleted = Archer.delete().where(Archer.name == deleteName).execute()
        #cur.execute('DELETE FROM archery_scores WHERE contestant_name = ?', (deleteName,))

def modify_scorePW():
    #modifyID = int(input("Enter the id of the contestant you wish to modify"))
    modifyName = input("Enter the id of the contestant you wish to modify")
    newScore = int(input("Enter the new score"))
    rows_changed = Archer.update(score=newScore).where(Archer.name == modifyName).execute()

def search_contestantPW():
    searchName = input("Enter the id of the contestant you wish to display: ")
    oneContestant = Archer.select().where(Archer.name == searchName)
    for contestant in oneContestant:
        print(contestant)

def search_allPW():
    allCOntestants = Archer.select()
    for contestant in allCOntestants:
        print(contestant)



main()
