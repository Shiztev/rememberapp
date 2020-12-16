'''
Make quick notes of anything you come accross. Whether it's 
a doctors appointment or something you heard on the radio, you
can make a note in just a few seconds.

@author Stevie Alvarez
'''

from notes import *  # create standardized note
import node_queue  # store notes 
import sys  # sys.argv to gather arguments/options from command line

class Notebook(node_queue.Queue):
    '''
    A subclass of node_queue, handels notes
    '''

    def __init__(self):
        """
        Constructor
        """
        super().__init__()  # Parent class init


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


    def __save(self):
        """
        Save the current queue of notes
        """
        # open the file with writing perms (APPEND), not standard reading
        pass


# Basic note functions - getopt module?

    # Create a note: UI(?) with a few text fields (Start with CLI)
        # possible text fields: subject, time, location, people, items, additional notes

    # Store a note: in a file/SQL(?)
        # could store in one file, each line being one note


# Access note functions - getopt module?

    # 'Read' stored notes: display the notes to review and remember.

    # Edit stored notes: alter the content of a note

    # Delete stored notes: remove notes from storage



# Main function, utilize sys to gather and process args/opts
    # try
        # verify sys.argv[1] is an option
        # get the argument for the option: sys.argv[2]
        # execuite the function/method with respect to the option
    # except, handel errors - raise errors when possible