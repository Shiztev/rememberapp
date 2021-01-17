'''
Test module for notes

@author Stevie Alvarez
'''


import notes
import notebook
import io

def test_contain():
    """
    """
    # setup
    n = notes.Note()
    n.set_sub("Testing")
    n.set_location("More tests")
    n.set_additional("\"Some major tests going down\"")

    # invoke
    actual_1 = False
    if "fail" in n:
        actual_1 = True

    actual_2 = False
    if "\"" in n:
        actual_2 = True

    # analyze
    assert actual_1 == False
    assert actual_2 == True


# OBSOLETE TEST - privitized new_note method
'''
def test_create(monkeypatch):
    """
    """
    # setup
    book = notebook.Notebook()
    monkeypatch.setattr('sys.stdin', io.StringIO("This\nIs\nA\nTest\nThe last field\nWill be blank\n \n"))
    expected = "Subject: " + "This" + "\n\tTime: " + "Is" + "\n\tDate: " + "A" + "\n\tLocation: " + "Test" + "\n\tPeople: " + "The last field" + "\n\tItems: " + "Will be blank" + "\n\tAdditional:  "

    # invoke
    book.new_note()
    actual = str(book.peek())

    # analyze
    assert expected == actual
'''


def test_type():
    """
    """
    # setup
    n = notes.Note()
    n.set_sub("sub")

    # invoke

    # analyze
    assert notes.Note == type(n)


def test_eq(monkeypatch):
    """
    """
    # setup
    n1 = notes.Note()
    n2 = notes.Note()
    n3 = notes.Note()
    monkeypatch.setattr('sys.stdin', io.StringIO("Test Pass\n2:00pm\n1/1/2005\n\n\n\n\nTest Pass\n2:00pm\n1/1/2005\n\n\nSome Stuff\n\nTest Fail\n2:00pm\n\nSomewhere\n\nSome Stuff\n\n"))
    # invoke
    n1.create_note()
    n2.create_note()
    n3.create_note()

    # analyze
    assert n1 == n2
    assert n1 != n3


def test_lt(monkeypatch):
    """
    """
    # setup
    n1 = notes.Note()
    n2 = notes.Note()
    n3 = notes.Note()
    monkeypatch.setattr('sys.stdin', io.StringIO("Test 1\n2:00pm\n7/8/2030\n\n\nSome Stuff\n\nTest 2\n2:00pm\n1/1/2022\n\n\nSome Stuff\n\nTest 3\n3:00pm\n\nSomewhere\n\nSome Stuff\n\n"))
    # invoke
    n1.create_note()
    n2.create_note()
    n3.create_note()

    # analyze
    assert n1 < n2  # 2pm @ 7/8/2030 < 2pm @ 1/1/2022
    assert n2 < n3  # 2pm @ 1/1/2022 < 3pm


def test_gt(monkeypatch):
    """
    """
    # setup
    n1 = notes.Note()
    n2 = notes.Note()
    n3 = notes.Note()
    monkeypatch.setattr('sys.stdin', io.StringIO("Test 1\n2:00pm\n1/2/2022\n\n\nSome Stuff\n\nTest 2\n2:00pm\n1/1/2023\n\n\nSome Stuff\n\nTest 3\n3:00pm\n\nSomewhere\n\nSome Stuff\n\n"))
    # invoke
    n1.create_note()
    n2.create_note()
    n3.create_note()

    # analyze
    assert n1 > n2  # 2pm @ 1/2/2022 > 2pm @ 1/1/2023
    assert n3 > n2  # 3pm > 2pm @ 1/1/2023


def test_ge(monkeypatch):
    """
    """
    # setup
    n1 = notes.Note()
    n2 = notes.Note()
    n3 = notes.Note()
    monkeypatch.setattr('sys.stdin', io.StringIO("Test 1\n2:00pm\n1/1/2023\n\n\nSome Stuff\n\nTest 2\n2:00pm\n1/1/2023\n\n\nSome Stuff\n\nTest 3\n1:00pm\n1/1/2023\nSomewhere\n\nSome Stuff\n\n"))
    # invoke
    n1.create_note()
    n2.create_note()
    n3.create_note()

    # analyze
    assert n1 >= n2  
    assert n3 >= n2  


def test_le():
    """
    """
    # setup
    n1 = notes.Note()
    n2 = notes.Note()
    n3 = notes.Note()
    #monkeypatch.setattr('sys.stdin', io.StringIO("Test 1\n3:00pm\n1/1/2022\n\n\nSome Stuff\n\nTest 2\n2:00pm\n1/1/2022\n\n\nSome Stuff\n\nTest 3\n2:00pm\n1/1/2022\nSomewhere\n\nSome Stuff\n\n"))
    # invoke
    n1.set_sub("test 1")
    n1.set_time("3:00pm")
    n1.set_date("1/1/2022")
    n2.set_sub("test 2")
    n2.set_time("2:00pm")
    n2.set_date("1/1/2022")
    n3.set_sub("test 3")
    n3.set_time("2:00pm")
    n3.set_date("1/1/2022")

    # analyze
    assert n2 <= n3 
    assert n1 <= n2 

#test_le()
# 0 - Subject, 1 - Time, 2 - Date, 3 - Location, 4 - People, 5 - Items, 6 - Additional