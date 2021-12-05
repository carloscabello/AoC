"""Day 3: Binary Diagnostic""" 
 
import sys, os, inspect

# necessary to import aoc2021/utils.py moudule
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils

exampledata = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

def power_consumption(inputdata):
    nlines = len(inputdata)     # size of the inputdata list
    ndigits = len(inputdata[0]) # assuming all binary numbers have the same number of digits
    ac = [0] * ndigits          # counter of 1s for each digit
    for inputline in inputdata:
        linedigits = list(map(int,list(inputline)) ) # str to int list
        for j in range(len(ac)):
            ac[j] += linedigits[j]
    
    gammabin = '0b'
    epsilonbin = '0b'
    for n_one in ac:
        if nlines - n_one < n_one: # more 1s than zeros
            gammabin += '1'
            epsilonbin +='0'
        else:
            gammabin += '0'
            epsilonbin +='1'
    
    gamma = int(gammabin, base=2)
    epsilon = int(epsilonbin, base=2)

    return gamma * epsilon

def life_rating(inputdata):

    o2bin = rating_finder('', inputdata, True)
    co2bin = rating_finder('', inputdata, False)
    
    o2 = int(o2bin,base=2)
    co2 = int(co2bin,base=2)

    return o2*co2

def rating_finder(binmask, inputlist, criteria=True):
    """Recursive function to find the rating depending of the criteria
    
    Parameters
    ----------
        binmask : str
            Part of the binary number that is being searched
        inputlist : list
            List of the remaining candidates for the searched binary number
        criteria : boolean
            If true, concatenate the most common digit when calculating the next bit of the searched number"""
    listsize = len(inputlist)
    inputlist_copy = inputlist.copy()
    if(listsize<=1):
        return inputlist[0]
    else:
        ibit = len(binmask)
        ac = 0 # 1s counter
        for elem in inputlist_copy:
            ac += int(elem[ibit])

        consider_most_common_bit = (listsize - ac <= ac) if criteria else (listsize - ac > ac)
        
        if consider_most_common_bit:
            binmask += '1'
        else:
            binmask += '0'
        
        return rating_finder(binmask, binlist_filter(binmask, inputlist_copy), criteria)
    

def binlist_filter(binmask, inputlist):
    aux_inputlist = inputlist.copy()
    for elem in aux_inputlist:
        if binmask!=elem[:len(binmask)]:
            inputlist.remove(elem)
    return inputlist

def main():
    # run script with arguments: load the input file
    inputdata = []
    if(2 <= len(sys.argv)):
        inputdata = utils.loadinput(sys.argv[1])
    # run script with no arguments: load example data
    else:
        inputdata = exampledata
        print(f"Puzzle input (example): {str(inputdata)}")

    print(f"Answer (part 1): {power_consumption(inputdata)}") # Correct example answer: 150
    print(f"Answer (part 2): {life_rating(inputdata)}") # Correct example answer: 230
    pass
 
if __name__ == "__main__": 
	main()