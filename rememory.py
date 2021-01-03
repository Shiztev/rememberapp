'''
Make quick notes of anything you come accross. Whether it's 
a doctors appointment or something you heard on the radio, you
can make a note in just a few seconds.

@author Stevie Alvarez
'''

from notes import *  # create standardized note
import node_queue  # store notes 
import sys  # sys.argv to gather arguments/options from command line

FILENAME = "notebook"  # standardized storage filename 

class Notebook(node_queue.Queue):
    '''
    A subclass of node_queue, handels notes
    '''

    def __init__(self):
        """
        Constructor
        """
        super().__init__()  # Parent class init


    def __order(self):
        """
        Order queue with respect to note comparators  
        # NEED TO IMPLIMENT NOTE COMPARATORS FIRST, BASED OFF TIME/DATE(?)
        """
        pass # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


    def fill(self, filename):
        """
        Fill the notebook with recorded notes from file filename
        """
        with open(filename) as f:
            for line in f:
                r = line.split("\'\', ")  # records
                # records have length of 7:
                # 0 - Subject, 1 - Time, 2 - Date, 3 - Location, 4 - People, 5 - Items, 6 - Additional
                n = Note()
                n.read_in_note(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
                self.enqueue(n)


    def new_note(self):
        """
        Make a new note and enqueue it
        """
        n = Note()
        n.create_note()
        self.enqueue(n)

    
    def __read(self):  # UNTESTED <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # >>>>>>>>>>>>>>>>>>>>>>DO YOU NEED THIS, WHAT IS IT FOR...?<<<<<<<<<<<<<<<<
        """
        Read the current save file
        """
        with open(FILENAME, "r") as f:
            for line in f:
                print(line)
                if f.tell() % 10 == 0:
                    _ = input("Enter integer index, or (y/n) to continue.")
                    if "n" in _:
                        break
                    elif "y" in _:
                        continue
                    else:
                        try:
                            _ = int(_)
                            break
                        except:
                            print("Improper input, specify yes or no to continue or not, or enter note index.")

        return _


    def __edit(self, a_note):
        """
        Edit provided note
        """
        if type(a_note) != Note:
            raise TypeError("Attempting to edit something other than a note!\nYou really shouldn't be seeing this message....")
        print("Which field would you like to edit?")


    def __append(self):
        """
        Save notes to end of file

            Option:
                -a
        """
        # single update implimentation
        with open(FILENAME, "a") as f:  # append to storage file
            f.write(repr(self.dequeue()))

    
    def __update(self):  # IMPLIMENT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        Save an updated version of a note

            Option:
                -u
        """
        # dequeue and enqueue front note, display new front
        # user determines if note should be updated
        print("Enter any character(s) when you reach the note you want to edit.")
        print("Otherwise, leave your input empty.")
        print("TO EXIT, enter in all caps: EXIT")

        curr = self.dequeue()
        u = input(str(curr))
        while u.strip() == "":
            
            self.enqueue(curr)
            curr = self.dequeue()
            u = input(str(curr))

        if u == "EXIT":
            return 0  # user exit

        edited = self.__edit(curr)
            

        
        


    def __save(self):  # APPEND WORKS, NEED OTHERS
        """
        Save the current queue of notes to the standard storage file

        UPDATE TO CALL METHODS TO UPDATE NOTES AND APPEND NOTES

            Option(?):
                -s  # maybe don't have an option to save and just do automatically?
        """
        pass


# Basic note functions - getopt module?

    # Create a note: UI(?) with a few text fields (Start with CLI)
        # possible text fields: subject, time, location, people, items, additional notes

    # Store a note: in a file/SQL(?)
        # could store in one file, each line being one note


# Access note functions - getopt module?

    # 'Read' stored notes: display the notes to review and remember.

        # Order notes by time and date - the sooner, the higher 'ranked' (1/1/01 > 1/2/01)

    # Edit stored notes: alter the content of a note

    # Delete stored notes: remove notes from storage



# Main function, utilize sys to gather and process args/opts
def main():
    """
    Currently using for manual tests
    """

    # try
        # verify sys.argv[1] is an option
        # get the argument for the option: sys.argv[2]
        # execuite the function/method with respect to the option
    # except, handel errors - raise errors when possible

    '''
    n = Notebook()
    n.new_note()
    n.new_note()
    n.new_note()
    n.save()
    '''


if __name__ == "__main__":
    main()
