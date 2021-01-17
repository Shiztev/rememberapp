'''
Make quick notes of anything you come accross. Whether it's 
a doctors appointment or something you heard on the radio, you
can make a note in just a few seconds.

@author Stevie Alvarez
'''


from notebook import *  # create notebook - queue of notes
import sys  # sys.argv to gather arguments/options from command line
import getopt  # parse arguments from command line input


# Main function, utilize sys to gather and process args/opts
def main():
    """
    Main, processes user arguments from command line

    # After init implimentation w/ file storage, look into mysql storage adaption?
    """

    # initialize notebook
    n = Notebook()
    n.fill()

    try:
        # verify sys.argv[1] is an option
        argv = sys.argv[1]
        if argv[0] == "-":
            # run method with respect to option
            if argv == "-a":
                n.add()
            elif argv == "-u":
                n.update()
            elif argv == "-d":
                n.delete()
            elif argv == "-r":
                try:
                    n.read()
                except IndexError as ie:
                    print(ie)

            else:
                raise ValueError("\'" + argv + "\'" + " is not a valid option!")

        else:
            raise ValueError("\'" + argv + "\'" + " is not a valid option!\nMust include a '-' (dash) at front.")

    # handel errors - raise errors when possible
    except ValueError as ve:
        print(ve)
        
    except TypeError as te:
        print(te)

    except IndexError:
        print("Please provide an option!")


if __name__ == "__main__":
    main()
