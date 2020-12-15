'''
Note object module

@author Stevie Alvarez
'''


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


    def set_sub(self, a_sub):
        """
        Set subject
        """
        if type(a_sub) != str:
            raise ValueError("Subject must be described in text!")
        elif len(a_sub) > 75:
            raise Warning("Subject text is long, this may affect legibility note.")
        else:
            self.__sub = a_sub

    
    def set_time(self, a_time):
        """
        Set time
        """
        if type(a_time) != str:
            raise ValueError("Time must be text!")
        else:
            self.__time = a_time


    def set_date(self, a_date):
        """
        Set date
        """
        if type(a_dates) != str:
            raise ValueError("Date must be text!")
        else:
            self.__date = a_date


    def set_location(self, a_loc):
        """
        Set location
        """
        if type(a_loc) != str:
            raise ValueError("Location must be text!")
        else:
            self.__location = a_loc


    def set_people(self, peoples):
        """
        Set people
        """
        if type(peoples) != str:
            raise ValueError("Peoples names must be text!")
        else:
            self.__people = peoples

    
    def set_items(self, an_item):
        """
        Set items
        """
        if type(an_item) != str:
            raise ValueError("Items must be text!")
        else:
            self.__items = an_item


    def set_additional(self, addit):
        """
        Set additional
        """
        if type(addit) != str:
            raise ValueError("Additional information must be text!")
        else:
            self.__additional = addit


    def __repr__(self):
        """
        Representation
        """
        pass


    def __str__(self):
        """
        String
        """
        pass


    def read_in_note(self):
        """
        Create note from previously stored note
        """
        pass


    def create_note(self):
        """
        Create note from user input/options
        """
        pass


    def __hash__(self):
        """
        Hash
        """
        ((ord(self.__sub[0]) * 31) + len(self.__sub))


    def __contain__(self, item):
        """
        Contain - in, not in
        """
        if item in self.__sub:
            return True

        if item in self.__time:
            return True

        if item in self.__people:
            return True

        if item in self.__location:
            return True

        if item in self.__items:
            return True

        if item in self.__additional:
            return True

        """
        for _ in self.__sub:
            if _ == item:
                return True

        for _ in self.__time:
            if _ == item:
                return True

        for _ in self.__people:
            if _ == item:
                return True

        for _ in self.__location:
            if _ == item:
                return True

        for _ in self.__people:
            if _ == item:
                return True

        for _ in self.__items:
            if _ == item:
                return True

        for _ in self.__additional:
            if _ == item:
                return True
        """

        return False


    def __iter__(self):
        """
        Returns iterator
        """
        return NoteIterator(self)