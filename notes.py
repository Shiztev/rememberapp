'''
Note object module

@author Stevie Alvarez
'''


import warnings
import datetime


FIELDS = ["Subject", "Time", "Date", "Location", "People", "Items", "Additional Information"]
MONTHS = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def equal(a, b):
    if type(a) == type(b):
        return a == b
    else:
        raise TypeError


def greater_than(a, b):
    if type(a) == type(b):
        return a > b
    else:
        raise TypeError


def less_than(a, b):
    if type(a) == type(b):
        return a < b
    else:
        raise TypeError


def lt_equal(a, b):
    if type(a) == type(b):
        return a <= b
    else:
        raise TypeError


def gt_equal(a, b):
    if type(a) == type(b):
        return a >= b
    else:
        raise TypeError


def _time_total(time):
    """
    Get total minutes of time list
    """
    total = 0
    total += time[0] * 60  # hours to minutes
    total += time[1]  # minutes

    return total


def _date_total(date):
    """
    Get total minuts of date list
    """
    total = 0
    total += (date[0] - 1950) * 525960  # years to minutes, since 1950, for size reduction
    total += date[1] * 43830  # months to minutes
    total += date[2] * 1440  # days to minutes
    return total


def _standard_time(time_list):
    """
    Convert time_list into minutes

        Parameters:
            time_list: list in [y, m, d, h, min] format
    """
    return _time_total(time_list[3:]) + _date_total(time_list[:3])
    

def _date_parser(date):
    """
    Parses date and ensures numerical values are used for proportional measuring

        Parameters:
            date: a date in m/d/y or m, d, y format
    """
    # date
    date = date.strip()
    if date == "":
        return [None, None, None]
    elif "/" in date:
        date = date.split("/")
    elif ", " in date:
        date.split(", ")
    else:
        raise ValueError("Improper date format!")

    # day and year should already be numeric
    try:
        d = int(date[1])
    except:
        raise ValueError("Date day is not numeric!")

    try:
        y = int(date[2])
    except:
        raise ValueError("Date year is not numeric!")

    # check if month needs to be converted
    try:
        m = int(date[0])
    except:
        for i in range(len(MONTHS)):
            if date[0] in MONTHS[i]:
                m = i + 1

    return [int(y), int(m), int(d)]


def _time_parser(time):
    """
    Parses time into list

        Parameters:
            time: a time in h:mm format
    """
    time = time.strip()
    hours = 0
    minutes = 0
    if time == "":
        return [None, None]

    if time[-2:] == "am":
        time = time[:-2].split(":")

    else:
        hours += 12
        if time[-2:] != "pm":
            time = time.split(":")
        else:
            time = time[:-2].split(":")

    try:
        hours += int(time[0])
        minutes += int(time[1])
    except ValueError:
        raise ValueError("Time not numeric! Hours: " + time[0] + " Minutes: " + time[1])
    except IndexError:
        raise ValueError("Time could not be properly split!")

    return [hours, minutes]


def _time_merge(date, time):
    """
    Merge date and time lists, used as a safeguard
    """
    if type(date) == list and type(time) == list:
        return date + time

    else:
        raise ValueError("Date or time not converted to a list!")


def _time_diff(date, time):
    """
    Determines the difference between the current date and provided time total
    """
    ct = datetime.datetime.now()
    c = [ct.year, ct.month, ct.day, ct.hour, ct.minute]  # get current time

    if None in date:
        if None in time:  # if provided time is None, return None
            return None
        else:
            return _time_total(time) # add up time, ignore date, ranks higher

    time = _standard_time(_time_merge(date, time))  # convert to minutes
    curr_time = _standard_time(c)  # convert current time to minutes

    return time - curr_time


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
            print("\033[1m\nFutureWarning: Subject text is long, this may affect legibility note.\n\033[0m")
        
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
            
        if type(a_date) != str:
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
        return "Subject: " + self.__sub + "\n\tTime: " + self.__time + "\n\tDate: " + self.__date + "\n\tLocation: " + self.__location + "\n\tPeople: " + self.__people + "\n\tItems: " + self.__items + "\n\tAdditional: " + self.__additional + "\n"


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


    """
    Bool comparisons done with respect to time and date. Notes ranked 
    based on time of occurance
    """

    def same(self, other):
        """
        Full __eq__ method, determines if items are completely identical
        """
        if type(self) == type(other):
            return self.__sub == other.get_sub() and self.__date == other.get_date() and self.__location == other.get_location() and self.__people == other.get_people() and self.__items == other.get_items() and self.__additional == other.get_additional()
                
        return False


# 'Rank' notes based on how long until time is reached - longer time < shorter time, with respect to current time

    def __eq__(self, other):
        """
        Returns equal comparison bool, with respect to time
        """
        if type(self) == type(other):
            sd = _time_diff(_date_parser(self.__date), _time_parser(self.__time))
            od = _time_diff(_date_parser(other.get_date()), _time_parser(other.get_time()))
            return sd == od

        return False


    def __le__(self, other):
        """
        Returns less than/equal comparison bool, with respect to current time and date
        """
        if type(self) == type(other):
            sd = _time_diff(_date_parser(self.__date), _time_parser(self.__time))
            od = _time_diff(_date_parser(other.get_date()), _time_parser(other.get_time()))

            # check to see if date is present
            if sd == None:
                return False
            
            elif od == None:
                return True

            # check to see if date has passed
            elif sd < 0:
                return True
            elif od < 0:
                return False
            
            return sd >= od  # if date is farther away, ranks lower

        return False


    def __ge__(self, other):
        """
        Returns greater than/equal comparison bool, with respect to current time and date
        """
        if type(self) == type(other):
            sd = _time_diff(_date_parser(self.__date), _time_parser(self.__time))
            od = _time_diff(_date_parser(other.get_date()), _time_parser(other.get_time()))

            # check to see if date is present
            if sd == None:
                return False
            
            elif od == None:
                return True

            # check to see if date has passed
            elif sd < 0:
                return False
            elif od < 0:
                return True
            
            return sd <= od  # if date is farther away, ranks lower

        return False


    def __gt__(self, other):
        """
        Returns greater than comparison bool, with respect to current time and date
        """
        if type(self) == type(other):
            sd = _time_diff(_date_parser(self.__date), _time_parser(self.__time))
            od = _time_diff(_date_parser(other.get_date()), _time_parser(other.get_time()))

            # check to see if date is present
            if sd == None:
                return False
            
            elif od == None:
                return True

            # check to see if date has passed
            elif sd < 0:
                return False
            elif od < 0:
                return True
            
            return sd < od  # if date is farther away, ranks lower

        return False


    def __lt__(self, other):
        """
        Returns less than comparison bool, with respect to current time and date
        If primary note's date is closer than other note's date, other > primary
        """
        if type(self) == type(other):
            sd = _time_diff(_date_parser(self.__date), _time_parser(self.__time))
            od = _time_diff(_date_parser(other.get_date()), _time_parser(other.get_time()))

            # check to see if date is present
            if sd == None:
                return False
            
            elif od == None:
                return True

            # check to see if date has passed
            elif sd < 0:
                return True
            elif od < 0:
                return False
            
            return sd > od  # if date is farther away, ranks lower

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