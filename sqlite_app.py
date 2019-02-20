import sqlite3
import collections


db = sqlite3.connect('archery.sqlite')

cur = db.cursor()



#cur.execute('create table phones (brand text, version integer)')

#cur.execute('insert into phones values ("Android", 5)')
#cur.execute('insert into phones values ("iPhone", 6)')

#db.commit()
cur.execute('create table if not exists archery_scores (contestant_name text, nation text,score integer )')
def main():

    while True:

        print("1) Add Contestant")
        print("2) Delete Contestant")
        print("3) Update Catches")
        print("4) Search Contestant")
        print("5) Display All Contestants")
        print("6) Exit")

        selection = input("Please Select:")
        if selection == '1':
            add_contestant()
        elif selection == '2':
            delete_contestant()
        elif selection == '3':
            modify_score()
        elif selection == '4':
            search_contestant()
        elif selection == '5':
            search_all()
        elif selection == '6':
            db.commit()
            break
        else:
            print("Unknown Option Selected!")



def add_contestant():
    enterName = input("Enter the name")
    enterNation = input("Enter Nation:")
    enterScore = input("Enter score:")
    cur.execute('insert into archery_scores values (?, ?, ?)', (enterName, enterNation, enterScore))

def delete_contestant():
    try:
        deleteName = input("Enter the name of the contestant you wish to delete")
        cur.execute('DELETE FROM archery_scores WHERE contestant_name = ?', (deleteName,))

    except sqlite3.Error:
        print('Error deleting contestant')


def modify_score():
    try:
        #modifyID = int(input("Enter the id of the contestant you wish to modify"))
        modifyName = input("Enter the id of the contestant you wish to modify")
        modifyScore = int(input("Enter the new score"))
        cur.execute('UPDATE archery_scores SET score = ? WHERE contestant_name = ?', (modifyScore, modifyName,))

    except sqlite3.Error:
        #raise ArcherError('Error updating score') from e
        print('Error updating score')

def search_contestant():
    try:
        searchName = input("Enter the id of the contestant you wish to display: ")
        oneContestant = cur.execute('SELECT rowid, * FROM archery_scores WHERE contestant_name = ?', (searchName,)).fetchone();
        print(oneContestant)

    except sqlite3.Error:
        #raise ArcherError('Error finding archer')
        print('Archer not found')

def search_all():
    allCOntestants = cur.execute('SELECT * FROM archery_scores').fetchall();
    print(allCOntestants)
main()
class ArcherError(Exception):
#for archery_scores eroors.
    pass