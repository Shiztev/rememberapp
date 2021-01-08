'''
Make quick notes of anything you come accross. Whether it's 
a doctors appointment or something you heard on the radio, you
can make a note in just a few seconds.

@author Stevie Alvarez
'''

from notes import *  # create standardized note
import node_queue  # store notes 
import sys  # sys.argv to gather arguments/options from command line
import inquirer  # CLI navigation

FILENAME = "notebook"  # standardized storage filename 
ATTRIBUTES = ["Subject", "Time", "Date", "Location", "People", "Items", "Additional Information"]
METHOD_QS = ["Which note would you like to edit?", "Which note would you like to delete?"]

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


    def fill(self, filename=FILENAME):
        """
        Fill the notebook with recorded notes from file filename
        """
        with open(filename) as f:
            for line in f:
                r = line.split("\'\', ")  # records
                r.pop(-1)
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


    def __shift(self, a_note):
        """
        Shift queue until a_note is at the front
        """
        while self.peek() != a_note:
            _ = self.dequeue()
            self.enqueue(_)


    def __edit(self, a_note):
        """
        Edit provided note, utilizes inquirer for attribute selection
        """
        if type(a_note) != Note:
            raise TypeError("Attempting to edit something other than a note!\nYou really shouldn't be seeing this message....")
       
        while True:  # allow user to edit as many attributes on the note as they want
            
            attribs = a_note.make_list()
            attribs.append("EXIT")
            questions = [
                inquirer.List(
                    'attrib',
                    message="Which field would you like to edit?",
                    choices=attribs)
            ]

            answers = inquirer.prompt(questions)
            
            if answers['attrib'] == "EXIT":
                break
            else:
                i = attribs.index(answers['attrib'])
                a_note.edit(ATTRIBUTES[i])


    def __remove(self, a_note):
        """
        Remove specified note from queue

            Returns:
                note specified to be removed from queue
        """
        self.__shift(a_note)
        _ = self.dequeue()
        return _


    def __append(self):
        """
        Save notes to end of file, 

            Option:
                -a
        """
        # single update implimentation
        with open(FILENAME, "a") as f:  # append to storage file
            f.write(repr(self.dequeue()))


    def __search(self, action, q):
        """
        Search for a note and pass it to the specified method

            Parameters:
                action: method to use with selected note
                q: question prompt with respect to action method
        """
        pass
        # use content from update method

        moderator = self.size()
        factor = 5
        next_prompt = "Next 5..."

        while True:  # repeat untill note/quit is selected

            if moderator <= 5:
                factor = moderator
                next_prompt = "Return to top"
            else:
                moderator -= 5

            options = []
            for _ in range(factor):
                i = self.dequeue()
                options.append(i)
                self.enqueue(i)
            
            subjects = [n.get_sub() for n in options]
            subjects.append("EXIT"); subjects.append(next_prompt);
                
            questions = [
                inquirer.List(
                    'note',
                    message=q,  # CHANGE BASED ON METHOD BEING CALLED
                    choices=subjects)
            ]

            answers = inquirer.prompt(questions)

            if answers['note'] == "EXIT":
                return

            elif answers['note'] == "Next 5...":
                continue

            elif answers['note'] == "Return to top":
                factor = 5
                moderator = self.size()

            else:
                break
        
        i = subjects.index(answers['note'])
        action(options[i])


    
    def update(self):  # IMPLIMENT and privitize<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        Save an updated version of a note, utilizes inquirer for note selection

            Option:
                -u
        """
        # dequeue and enqueue front note, display new front
        # user determines if note should be updated
        self.__search(self.__edit, METHOD_QS[0])
        # USE __search TO DETERMINE, NEED TO PASS METHOD 
            

    def delete(self):
        """
        Delete a note

            Option:
                -d
        """
        self.__search(self.__remove, METHOD_QS[1])
        


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

    
    n = Notebook()
    n.fill()
    n.update()
    n.delete()

    



if __name__ == "__main__":
    main()
