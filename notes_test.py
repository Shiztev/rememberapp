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
