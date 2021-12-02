"""Day 2: Dive!""" 
 
import sys, os, inspect

# necessary to import aoc2021/utils.py moudule
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils

exampledata = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

def course_parser1(inputdata):
    forwardPos = 0
    depthPos = 0

    for command in inputdata:
        direction, positions = command_parser(command)
        
        if direction == 'forward':
            forwardPos += positions
        elif direction == 'up':
            depthPos += -positions
        elif direction == 'down':
            depthPos += positions

    return forwardPos*depthPos

def course_parser2(inputdata):
    forwardPos = 0
    depthPos = 0
    aimDive = 0 # incresing aim will point toward the depths

    for command in inputdata:
        direction, positions = command_parser(command)
        
        if direction == 'forward':
            forwardPos += positions
            depthPos += aimDive*positions
        elif direction == 'up':
            aimDive += -positions
        elif direction == 'down':
            aimDive += positions

    return forwardPos*depthPos

def command_parser(command):
    parsed_command = command.split()
    return parsed_command[0], int(parsed_command[1]) # direction, positions

 
def main():
    # run script with arguments: load the input file
    if(2 <= len(sys.argv)):
        inputdata = utils.loadinput(sys.argv[1])
        print(f"Answer (part 1): {course_parser1(inputdata)}")# Correct answer: 1855814
        print(f"Answer (part 2): {course_parser2(inputdata)}")# Correct answer: ?
    
    # run script with no arguments: load example data
    else:
        inputdata = exampledata
        print(f"Puzzle input (example): {str(inputdata)}")
        print(f"Answer (part 1): {course_parser1(inputdata)}")           # Correct answer: 150
        print(f"Answer (part 2): {course_parser2(inputdata)}")           # Correct answer: 900
    pass 
 
if __name__ == "__main__": 
	main()