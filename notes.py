'''
Note object module

@author Stevie Alvarez
'''

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
        self.__sub = None
        self.__time = None
        self.__date = None
        self.__location = None
        self.__people = None
        self.__items = None
        self.__additional = None


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


    def readin_note(self):
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
        ord(self.__sub[0])



