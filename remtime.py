'''
Time object module

@author Stevie Alvarez
'''


import datetime


def _time_diff(time):
    """
    Determines the difference between the current time and provided time

        Parameters:
            time: Time object

        Returns:
            formated h, m list of difference between param and current time
    """
    if time.get_time() == "":
        return [-1, -1]
    current_time = datetime.datetime.now()
    h = time.get_hour() - current_time.hour
    m = time.get_min() - current_time.minute
    return [h, m]


class Time:
    '''
    Time class, ease of sorting notes
    '''
    __slots__ = ['__time', '__hour', '__minutes']
    def __init__(self, a_time):
        """
        Constructor
        """
        self.__time = a_time.strip()
        if self.__time == "":
            self.__hour = None
            self.__minutes = None
        else:
            m = self.__time[-2:len(a_time)]  # am/pm
            if m == "am":
                m = 0
            else:
                m = 12
            a_time = self.__time.split(":")
            self.__hour = int(a_time[0]) + m
            self.__minutes = int(a_time[1][:2])

    
    def get_time(self):
        return self.__time

    
    def get_hour(self):
        return self.__hour


    def get_min(self):
        return self.__minutes


    def __lt__(self, other):
        """
        """
        if type(self) == type(other):
            s = _time_diff(self)
            o = _time_diff(other)

            if s[0] < 0 or s[1] < 0:
                return True
            if o[0] < 0 or o[1] < 0:
                return False

            if s[0] == o[0]:
                return s[1] < o[1]
            else:
                return s[0] < o[0]

        return False


    def __gt__(self, other):
        """
        """
        if type(self) == type(other):
            s = _time_diff(self)
            o = _time_diff(other)

            if s[0] < 0 or s[1] < 0:
                return False
            if o[0] < 0 or o[1] < 0:
                return True
            
            if s[0] == o[0]:
                return s[1] > o[1]
            else:
                return s[0] > o[0] 

        return False