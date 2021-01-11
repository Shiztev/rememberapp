'''
Test module for notes

@author Stevie Alvarez
'''


import notes
import rememory
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


def test_create(monkeypatch):
    """
    """
    # setup
    book = rememory.Notebook()
    monkeypatch.setattr('sys.stdin', io.StringIO("This\nIs\nA\nTest\nThe last field\nWill be blank\n \n"))
    expected = "Subject: " + "This" + "\n\tTime: " + "Is" + "\n\tDate: " + "A" + "\n\tLocation: " + "Test" + "\n\tPeople: " + "The last field" + "\n\tItems: " + "Will be blank" + "\n\tAdditional:  "

    # invoke
    book.new_note()
    actual = str(book.peek())

    # analyze
    assert expected == actual


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
    monkeypatch.setattr('sys.stdin', io.StringIO("Test Pass\n2:00pm\n1/1/2005\n\n\nSome Stuff\n\nTest Pass\n2:00pm\n1/1/2005\n\n\nSome Stuff\n\nTest Fail\n3:00pm\n\nSomewhere\n\nSome Stuff\n\n"))
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
    monkeypatch.setattr('sys.stdin', io.StringIO("Test Pass\n2:00pm\n1/1/2005\n\n\nSome Stuff\n\nTest Pass\n2:00pm\n1/1/2005\n\n\nSome Stuff\n\nTest Fail\n3:00pm\n\nSomewhere\n\nSome Stuff\n\n"))
    # invoke
    n1.create_note()
    n2.create_note()
    n3.create_note()

    # analyze
    assert n1 == n2
    assert n1 != n3


def test_gt(monkeypatch):
    """
    """
    # setup
    n1 = notes.Note()
    n2 = notes.Note()
    n3 = notes.Note()
    monkeypatch.setattr('sys.stdin', io.StringIO("Test 1\n2:00pm\n1/2/2005\n\n\nSome Stuff\n\nTest 2\n2:00pm\n1/1/2005\n\n\nSome Stuff\n\nTest 3\n3:00pm\n\nSomewhere\n\nSome Stuff\n\n"))
    # invoke
    n1.create_note()
    n2.create_note()
    n3.create_note()

    # analyze
    assert n2 > n1
    assert n3 > n2  # NEED TO MODIFY COMPARATORS, DON'T PROPERLY HANDEL WHEN DATE IS MISSING





# 0 - Subject, 1 - Time, 2 - Date, 3 - Location, 4 - People, 5 - Items, 6 - Additional