'''
Note object module

@author Stevie Alvarez
'''


FIELDS = ["Subject", "Time", "Date", "Location", "People", "Items", "Additional Information"]


class NoteIterator:
    '''
    Allows Note objects to be iterated through
    '''
    __slots__ = ['__note', '__index', '__max']

    def __init__(self, note):
        """
        Constructor
        """
        # index order: sub -> time -> date -> loc -> people -> items -> addit
        self.__note = note
        self.__index = 0
        self.__max = len(self.__note.get_sub()) + len(self.__note.get_time()) + len(self.__note.get_date()) + len(self.__note.get_location()) + len(self.__note.get_people()) + len(self.__note.get_items()) + len(self.__note.get_additional())


    def __next__(self):
        """
        Retrieves next 'item' in Note
        """
        if self.__index < self.__max:
            self.__index += 1
            if self.__index < len(self.__note.get_sub()):
                return self.__note.get_sub()[self.__index - 1]
            elif self.__index < len(self.__note.get_sub()) + len(self.__note.get_time()):
                return self.__note.get_time()[self.__index - 1 - len(self.__note.get_sub())]
            elif self.__index < len(self.__note.get_sub()) + len(self.__note.get_time()) + len(self.__note.get_date()):
                return self.__note.get_date()[self.__index - 1 - (len(self.__note.get_sub()) + len(self.__note.get_time()))]
            elif self.__index < len(self.__note.get_sub()) + len(self.__note.get_time()) + len(self.__note.get_date()) + len(self.__note.get_location()):
                return self.__note.get_location()[self.__index - 1 - (len(self.__note.get_sub()) + len(self.__note.get_time()) + len(self.__note.get_date()))]
            elif self.__index < len(self.__note.get_sub()) + len(self.__note.get_time()) + len(self.__note.get_date()) + len(self.__note.get_location()) + len(self.__note.get_people()):
                return self.__note.get_people()[self.__index - 1 - (len(self.__note.get_sub()) + len(self.__note.get_time()) + len(self.__note.get_date()) + len(self.__note.get_location()))]
            elif self.__index < len(self.__note.get_sub()) + len(self.__note.get_time()) + len(self.__note.get_date()) + len(self.__note.get_location()) + len(self.__note.get_people()) + len(self.__note.get_items()):
                return self.__note.get_items()[self.__index - 1 - (len(self.__note.get_sub()) + len(self.__note.get_time()) + len(self.__note.get_date()) + len(self.__note.get_location()) + len(self.__note.get_people()))]
            else:
                return self.__note.get_additional()[self.__index - 1 - (len(self.__note.get_sub()) + len(self.__note.get_time()) + len(self.__note.get_date()) + len(self.__note.get_location()) + len(self.__note.get_people()) + len(self.__note.get_items()))]

        raise StopIteration


class Note:
    '''
    A note with key features of a subject

        Slots:
            sub: Subject
            time: time
            date: date
            location: location
            people: people
            items: items
            additional: anything else that aught to be remembered
    '''
    __slots__ = [
        '__sub', '__time', '__date', '__location', '__people', 
        '__items', '__additional'
        ]

    def __init__(self):
        """
        Constructor
        """
        self.__sub = ""  # None
        self.__time = ""  # None
        self.__date = ""  # None
        self.__location = ""  # None
        self.__people = ""  # None
        self.__items = ""  # None
        self.__additional = ""  # None


    def get_sub(self):
        return self.__sub


    def get_time(self):
        return self.__time


    def get_date(self):
        return self.__date


    def get_location(self):
        return self.__location


    def get_people(self):
        return self.__people


    def get_items(self):
        return self.__items

    def get_additional(self):
        return self.__additional


    def set_sub(self, a_sub=None):
        """
        Set subject
        """
        if a_sub == None:
            a_sub = input("Enter new subject: ")

        if type(a_sub) != str:
            raise ValueError("Subject must be described in text!")
        elif len(a_sub) > 15:
            raise Warning("Subject text is long, this may affect legibility note.")
        else:
            self.__sub = a_sub

    
    def set_time(self, a_time=None):
        """
        Set time
        """
        if a_time == None:
            a_time = input("Enter new time: ")

        if type(a_time) != str:
            raise ValueError("Time must be text!")
        else:
            self.__time = a_time


    def set_date(self, a_date=None):
        """
        Set date
        """
        if a_date == None:
            a_date = input("Enter new date: ")
            
        if type(a_dates) != str:
            raise ValueError("Date must be text!")
        else:
            self.__date = a_date


    def set_location(self, a_loc=None):
        """
        Set location
        """
        if a_loc == None:
            a_loc = input("Enter new location: ")
            
        if type(a_loc) != str:
            raise ValueError("Location must be text!")
        else:
            self.__location = a_loc


    def set_people(self, peoples=None):
        """
        Set people
        """
        if peoples == None:
            peoples = input("Enter new people: ")
            
        if type(peoples) != str:
            raise ValueError("Peoples names must be text!")
        else:
            self.__people = peoples

    
    def set_items(self, an_item=None):
        """
        Set items
        """
        if an_item == None:
            an_item = input("Enter new items: ")
            
        if type(an_item) != str:
            raise ValueError("Items must be text!")
        else:
            self.__items = an_item


    def set_additional(self, addit=None):
        """
        Set additional
        """
        if addit == None:
            addit = input("Enter new additional information: ")
            
        if type(addit) != str:
            raise ValueError("Additional information must be text!")
        else:
            self.__additional = addit


    def __repr__(self):
        """
        Representation - primarily used for file storage
        """
        # 0 - Subject, 1 - Time, 2 - Date, 3 - Location, 4 - People, 5 - Items, 6 - Additional
        return (self.__sub + "'', " + self.__time + "'', " + self.__date + "'', " + self.__location + "'', " + self.__people + "'', " + self.__items + "'', " + self.__additional + "'', " + "\n")


    def __str__(self):
        """
        String
        """
        return "Subject: " + self.__sub + "\n\tTime: " + self.__time + "\n\tDate: " + self.__date + "\n\tLocation: " + self.__location + "\n\tPeople: " + self.__people + "\n\tItems: " + self.__items + "\n\tAdditional: " + self.__additional


    def __fill(self, sub, time, date, loc, people, items, addit):
        # 0 - Subject, 1 - Time, 2 - Date, 3 - Location, 4 - People, 5 - Items, 6 - Additional
        """
        Fill note with respect to arguments
        """
        self.__sub = sub
        self.__time = time
        self.__date = date
        self.__location = loc
        self.__people = people
        self.__items = items
        self.__additional = addit

    
    def read_in_note(self, sub, time, date, loc, people, items, addit):
        """
        Create note with respect to arguments, called when filling in from file
        """
        self.__fill(sub, time, date, loc, people, items, addit)


    def create_note(self):
        """
        Create note from user input/options
        """
        print("Fill out each field of the note, press enter when done.\nIf field should be blank, simply press enter.")
        a = []
        for f in FIELDS:
            user_input = input("Enter " + f + ": ")
            a.append(user_input)
        
        self.__fill(a[0], a[1], a[2], a[3], a[4], a[5], a[6])


    def __hash__(self):
        """
        Hash
        """
        return ((ord(self.__sub[0]) * 31) + len(self.__sub))


    def __contain__(self, item):
        """
        Contain - in, not in
        """
        if item in self.__sub:
            return True

        if item in self.__time:
            return True

        if item in self.__date:
            return True

        if item in self.__people:
            return True

        if item in self.__location:
            return True

        if item in self.__items:
            return True

        if item in self.__additional:
            return True

        return False


    def __iter__(self):
        """
        Returns iterator
        """
        return NoteIterator(self)


    def __eq__(self, other):
        """
        Returns comparison bool
        """
        if type(self) == type(other):
            return self == other

        return False


    def edit(self, field):
        """
        Edit specified field
        """
        if field == "Subject":
            self.set_sub()
        elif field == "Time":
            self.set_time()
        elif field == "Date":
            self.set_date()
        elif field == "Location":
            self.set_location()
        elif field == "People":
            self.set_people()
        elif field == "Items":
            self.set_items()
        else:
            self.set_additional()


    def make_list(self):
        """
        Return formated list version of note
        """
        return ["Subject: " + self.__sub, "Time: " + self.__time, "Date: " + self.__date, "Location: " + self.__location, "People: " + self.__people, "Items: " + self.__items, "Additional Information: " + self.__additional]