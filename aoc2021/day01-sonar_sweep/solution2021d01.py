"""Day 1: Sonar Sweep""" 
 
import sys, os, inspect

# necessary to import aoc2021/utils.py moudule
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils

exampledata = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def increment_counter(inputdata):
    counter = 0

    for i in range(1,len(inputdata)):
        # 1st measurements[0] is excluded
        if(inputdata[i-1] < inputdata[i]):
            counter+=1
    return counter

def window_sum(i,inputdata):
    # sum elements from i-1 to i+1, with i+2 excluded
    return sum(inputdata[i-1:i+2])

def windowed_increment_counter(inputdata):
    counter = 0
    
    for i in range(2,len(inputdata)-1):
        # current window is compared to the previous one, so 1st window is excluded
        if(window_sum(i-1,inputdata) < window_sum(i,inputdata)):
            counter+=1
    return counter
 
def main():
    # run script with arguments: load the input file
    if(2 <= len(sys.argv)):
        inputdata = utils.to_int((utils.loadinput(sys.argv[1])))
        print(f"Answer (part 1): {increment_counter(inputdata)}")           # Correct answer: 1696
        print(f"Answer (part 2): {windowed_increment_counter(inputdata)}")  # Correct answer: 1737
    
    # run script with no arguments: load example data
    else:
        inputdata = exampledata
        print(f"Puzzle input (example): {str(inputdata)}")
        print(f"Answer (part 1): {increment_counter(inputdata)}")           # Correct answer: 7
        print(f"Answer (part 2): {windowed_increment_counter(inputdata)}")  # Correct answer: 5

    pass 
 
if __name__ == "__main__": 
	main()