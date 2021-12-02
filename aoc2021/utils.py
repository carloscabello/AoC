"""Basic input reader""" 
 
import sys


def to_int(strlist):
    res = list(map(int, strlist))
    return res

def loadinput(filepath):
    """Read a file and save each line as a list element
    
    Parameters
    ----------
        filepath : str
            The path to the input file of the puzzle"""
    with open (filepath, "r") as inputfile:
        inputlines = inputfile.readlines()
        inputs = [line.rstrip() for line in inputlines]
        return inputs
 
def main():
    if(2 <= len(sys.argv)):
        inputdata = loadinput(sys.argv[1])
        print(str(inputdata))

    pass
 
if __name__ == "__main__": 
	main()