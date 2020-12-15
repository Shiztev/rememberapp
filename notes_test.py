'''
Test module for notes

@author Stevie Alvarez
'''


import notes


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


def test_find():
    """
    """
    # setup
    n = notes.Note()
    n.set_sub("Testing")
    n.set_location("More tests")
    n.set_additional("\"Some major tests going down\"")

    # invoke
    #actual = n.find("test")

    # analyze
    pass # UNSURE IF FIND METHOD IS NECESSARY