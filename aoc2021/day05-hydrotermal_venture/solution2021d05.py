"""Day 4: Giant Squid""" 
 
import sys, os, inspect

# necessary to import aoc2021/utils.py moudule
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils

exampledata = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2']

def input_parser(inputdata):
    """Given the input of the puzzle represent it with a list of tuples
    
    Parameters
    ----------
        inputdata : list
            A list of strings, each being a line of the raw input file.
    Returns
    ----------
        inputdata : list
            A list of strings, each being a line of the raw input file.
        max_x : int
            Max x coordinate value from all points
        max_y : int
            Max y coordinate value from all points
    """
    res = []
    max_x = 0
    max_y = 0
    for line in inputdata:
        pointpair = ()

        for strpoint in line.split('->'):
            strpoint = strpoint.strip()
            point = ()

            for indexcoord, strcoord in enumerate(strpoint.split(',')):
                valuecoord = int(strcoord)
                point += (valuecoord,)
                if(indexcoord==0 and max_x<valuecoord):
                    max_x = valuecoord
                elif(0<indexcoord and max_y<valuecoord):
                    max_y = valuecoord

            pointpair += (point,)
        res.append(pointpair)
    # return a list of points-pair (x1,y1) and (x2,y2)
    #   each point is a pair x,y coordinates
    return res, max_x, max_y

def closedrange(start, stop):
    "Return all values in the interval [start,stop] no matter which one is greater"
    step = 1 if (start<=stop) else -1
    return range(start, stop + step, step)

def vent_mapper(inputdata, include_diagonal_lines=False):
    """Given the already parsed input data from puzzle aoc2021day05 return the final solution
    
    Parameters
    ----------
        inputdata : list
            A list of tuples, each tuple representing a pair of points. Each point itself is a tuple (int,int).
        include_diagonal_lines : bool (Default=False)
            If points describe a diagonal line, include them in the mapping.
            The default behavior is to only include vertical o diagonal lines
    """
    ventpointpairs, max_x, max_y = input_parser(inputdata)
    ventmap = [[0]*(max_x+1) for i in range(max_y+1)] # to index the ventmap: ventmap[y][x]

    for ventsegment in ventpointpairs:
        x1,y1 = ventsegment[0]
        x2,y2 = ventsegment[1]

        # only horizontal and vertical lines
        if(x1 == x2):
            for y in closedrange(y1, y2):
                ventmap[y][x1] += 1
        elif(y1 == y2):
            for x in closedrange(x1, x2):
                ventmap[y1][x] += 1
        # diagonal line at exactly 45 degrees
        elif (include_diagonal_lines):
            for x,y in closedrange_diag( (x1,y1), (x2,y2) ):
                ventmap[y][x] += 1

    return vent_counter(ventmap,2)

def closedrange_diag(start, stop):
    "Return all points (x,y) from a 45º diagonal line from (x1,y1) to (x2,y2)"
    x1, y1 = start
    x2, y2 = stop
    return zip(closedrange(x1, x2), closedrange(y1, y2))

def vent_counter(ventmap, overlap):
    res = 0
    for ventrow in ventmap:
        for ventelem in ventrow:
            if (overlap <= ventelem):
                res +=1
    return res

def main():
    inputdata = []

    # run script with arguments: load the input file
    if(2 <= len(sys.argv)):
        inputdata = utils.loadinput(sys.argv[1])
    # run script with no arguments: load example data
    else:
        inputdata = exampledata
        print(f"Puzzle input (example)")
        print(f"{exampledata}\n")

    print(f"Answer (part 1): {vent_mapper(inputdata)}\n") # Correct example answer: 5
    print(f"Answer (part 2): {vent_mapper(inputdata, True)}") # Correct example answer: 12
    pass
 
if __name__ == "__main__": 
	main()