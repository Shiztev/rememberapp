'''
Make quick notes of anything you come accross. Whether it's 
a doctors appointment or something you heard on the radio, you
can make a note in just a few seconds.

@author Stevie Alvarez
'''

from notes import *  # create standardized note
import node_queue  # store notes 

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
        Fill the notebook with recorded notes from file filename, 
        return a dictionary version in addition
        """
        d = dict()
        with open(filename) as f:
            for line in f:
                records = line.split("\'\', ")
                # records have length of 7:
                # 0 - Subject, 1 - Time, 2 - Date, 3 - Location, 4 - People, 5 - Items, 6 - Additional

                



# Basic note functions - getopt module?

    # Create a note: UI(?) with a few text fields (Start with CLI)
        # possible text fields: subject, time, location, people, items, additional notes

    # Store a note: in a file/SQL(?)
        # could store in one file, each line being one note


# Access note functions - getopt module?

    # 'Read' stored notes: display the notes to review and remember.

    # Edit stored notes: alter the content of a note

    # Delete stored notes: remove notes from storage