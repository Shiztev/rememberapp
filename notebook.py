'''
Notebook object module

@author Stevie Alvarez
'''


from notes import *  # create standardized note
import node_queue  # store notes 
import inquirer  # CLI navigation


FILENAME = "notememory.txt"  # standardized storage filename 
ATTRIBUTES = ["Subject", "Time", "Date", "Location", "People", "Items", "Additional Information"]
METHOD_QS = ["Which note would you like to edit?", "Which note would you like to delete?", "Current notes in notebook...."]


class Notebook(node_queue.Queue):
    '''
    A subclass of node_queue, handels notes
    '''

    def __init__(self):
        """
        Constructor
        """
        super().__init__()  # Parent class init


    def __str__(self):
        """
        String version of notebook
        """
        s = ""
        for i in range(self.size()):
            _ = self.dequeue()
            s += str(_) + "\n"
            self.enqueue(_)
        
        return s


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


    def __new_note(self):
        """
        Make a new note and enqueue it
        """
        n = Note()
        n.create_note()
        self.enqueue(n)


    def __search(self, action, q):
        """
        Search for a note and pass it to the specified method

            Parameters:
                action: method to use with selected note
                q: question prompt with respect to action method
        """
        front = self.peek()
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

        # reorder notebook
        while not top.same(self.peek()):
            _ = self.dequeue()
            self.enqueue(_)


    def __shift(self, a_note):
        """
        Shift queue until a_note is at the front
        """
        while not a_note.same(self.peek()):
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


    def add(self):
        """
        Create and add a note

            Option:
                -a
        """
        self.__new_note()

    
    def update(self): 
        """
        Save an updated version of a note, utilizes inquirer for note selection

            Option:
                -u
        """
        # dequeue and enqueue front note, display new front
        # user determines if note should be updated
        self.__search(self.__edit, METHOD_QS[0])
            

    def delete(self):
        """
        Delete a note

            Option:
                -d
        """
        self.__search(self.__remove, METHOD_QS[1])


    def __make_list(self):
        """
        Dequeues and turns notebook into unordered list
        """
        l = []
        while not self.is_empty():
            l.append(self.dequeue())

        return l


    def __convert_list(self, l):
        """
        Enqueues all items in a list in order
        """
        for _ in l:
            self.enqueue(_)


    def __order(self):
            """
            Order queue with respect to note comparators  
            # NEED TO IMPLIMENT NOTE COMPARATORS FIRST, BASED OFF TIME/DATE(?)
            """
            l = self.__make_list()
            l = sorted(l)  # Doesn't properly sort....
            self.__convert_list(l)


    def __read_note(self, a_note):
        """
        Display a note
        """
        print(str(a_note))


    def read(self):
        """
        Display notes

            Option:
                -r
        """
        # change so that notebook is ordered before reading
        self.__order() # move to top of __save, once implimented 
        self.__search(self.__read_note, METHOD_QS[2])


    def __append(self):  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        Save notes to end of file
        """
        # single update implimentation
        with open(FILENAME, "a") as f:  # append to storage file
            f.write(repr(self.dequeue()))
        

    def __save(self):  # APPEND WORKS, NEED OTHERS
        """
        Save the current queue of notes to the standard storage file

        UPDATE TO CALL METHODS TO UPDATE NOTES AND APPEND NOTES

            Option(?):
                -s  # maybe don't have an option to save and just do automatically?
        """
        pass
        # have __order at top(?)
        

            



    


# Access note functions - getopt module?

    # 'Read' stored notes: display the notes to review and remember.

        # Order notes by time and date - the sooner, the higher 'ranked' (1/1/01 > 1/2/01)
