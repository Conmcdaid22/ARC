#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.

#Function 1: Solve 08ed6ac7.json
def solve_08ed6ac7(x):
    cols = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 5:
                if j not in cols:
                    cols.append(j)

    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 5:
                if j == cols[0]:
                    x[i][j]= 1
                if j == cols[1]:
                    x[i][j] = 2
                if j == cols[2]:
                    x[i][j]= 3
                if j == cols[3]:
                    x[i][j] = 4
    return x

#Function 2: Solve 4258a5f9.json
def solve_4258a5f9(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 5:
                x[i-1][j] = 1
                x[i+1][j] = 1
                x[i][j-1] = 1
                x[i][j+1] = 1
                x[i+1][j+1] = 1
                x[i-1][j+1] = 1
                x[i+1][j-1] = 1
                x[i-1][j-1] = 1
    return x

#Function 3: Solve 178fcbfb.json
def solve_178fcbfb(x):
    redcol = []
    bluerow = []
    greenrow = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 2:
                redcol.append(j)           
    for i in range(len(x)):
        for j in range(len(x[i])):
            if j == redcol[0]:
                x[i][j]= 2
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 3:
                greenrow.append(i)
            if x[i][j] == 1:
                bluerow.append(i)
    for i in range(len(x)):
        for j in range(len(x[i])):
            for i in greenrow:
                x[i][j]= 3
            for i in bluerow:
                x[i][j]= 1
    return x

#Function 4: Solve 5614dbcf.json
def solve_5614dbcf(x):
# Array Slicing & Reshaping
# maximum value in an array 
    blocks = []

    first_block = x[0:3, 0:9]
    lfb = first_block[0:3, 0:3]
    blocks.append(lfb)
    mfb = first_block[0:3, 3:6]
    blocks.append(mfb)
    rfb = first_block[0:3, 6:9]
    blocks.append(rfb)

    second_block = x[3:6, 0:9]
    lsb = second_block[0:3, 0:3]
    blocks.append(lsb)
    msb = second_block[0:3, 3:6]
    blocks.append(msb)
    rsb = second_block[0:3, 6:9]
    blocks.append(rsb)

    third_block = x[6:9, 0:9]
    ltb = third_block[0:3, 0:3]
    blocks.append(ltb)
    mtb = third_block[0:3, 3:6]
    blocks.append(mtb)
    rtb = third_block[0:3, 6:9]
    blocks.append(rtb)

    output_array = []
    for block in blocks:
        output_array.append(np.argmax(np.bincount(block.flat)))
    np_output = np.array(output_array)
    x = np.reshape(np_output, (3,3))
    
    return x


#Function 5: Solve 3af2c5a8.json
def solve_3af2c5a8(x):
    #Array flipping, mirroring and stacking
    input_12_array2 = np.fliplr(x)
    input_12_array3 = np.hstack((x, input_12_array2))
    input_12_array4 = np.flipud(input_12_array3)
    input_12_array5 = np.vstack((input_12_array3, input_12_array4))
    x = input_12_array5
    return x


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()

