# The Abstraction and Reasoning Corpus (ARC)

This repository contains the ARC task data, as well as a browser-based interface for humans to try their hand at solving the tasks manually.

*"ARC can be seen as a general artificial intelligence benchmark, as a program synthesis benchmark, or as a psychometric intelligence test. It is targeted at both humans and artificially intelligent systems that aim at emulating a human-like form of general fluid intelligence."*

A complete description of the dataset, its goals, and its underlying logic, can be found in: [The Measure of Intelligence](https://arxiv.org/abs/1911.01547).

As a reminder, a test-taker is said to solve a task when, upon seeing the task for the first time, they are able to produce the correct output grid for *all* test inputs in the task (this includes picking the dimensions of the output grid). For each test input, the test-taker is allowed 3 trials (this holds for all test-takers, either humans or AI).


## Task file format

The `data` directory contains two subdirectories:

- `data/training`: contains the task files for training (400 tasks). Use these to prototype your algorithm or to train your algorithm to acquire ARC-relevant cognitive priors.
- `data/evaluation`: contains the task files for evaluation (400 tasks). Use these to evaluate your final algorithm. To ensure fair evaluation results, do not leak information from the evaluation set into your algorithm (e.g. by looking at the evaluation tasks yourself during development, or by repeatedly modifying an algorithm while using its evaluation score as feedback).

The tasks are stored in JSON format. Each task JSON file contains a dictionary with two fields:

- `"train"`: demonstration input/output pairs. It is a list of "pairs" (typically 3 pairs).
- `"test"`: test input/output pairs. It is a list of "pairs" (typically 1 pair).

A "pair" is a dictionary with two fields:

- `"input"`: the input "grid" for the pair.
- `"output"`: the output "grid" for the pair.

A "grid" is a rectangular matrix (list of lists) of integers between 0 and 9 (inclusive). The smallest possible grid size is 1x1 and the largest is 30x30.

When looking at a task, a test-taker has access to inputs & outputs of the demonstration pairs, plus the input(s) of the test pair(s). The goal is to construct the output grid(s) corresponding to the test input grid(s), using 3 trials for each test input. "Constructing the output grid" involves picking the height and width of the output grid, then filling each cell in the grid with a symbol (integer between 0 and 9, which are visualized as colors). Only *exact* solutions (all cells match the expected answer) can be said to be correct.


## Usage of the testing interface

The testing interface is located at `apps/testing_interface.html`. Open it in a web browser (Chrome recommended). It will prompt you to select a task JSON file.

After loading a task, you will enter the test space, which looks like this:

![test space](https://arc-benchmark.s3.amazonaws.com/figs/arc_test_space.png)

On the left, you will see the input/output pairs demonstrating the nature of the task. In the middle, you will see the current test input grid. On the right, you will see the controls you can use to construct the corresponding output grid.

You have access to the following tools:

### Grid controls

- Resize: input a grid size (e.g. "10x20" or "4x4") and click "Resize". This preserves existing grid content (in the top left corner).
- Copy from input: copy the input grid to the output grid. This is useful for tasks where the output consists of some modification of the input.
- Reset grid: fill the grid with 0s.

### Symbol controls

- Edit: select a color (symbol) from the color picking bar, then click on a cell to set its color.
- Select: click and drag on either the output grid or the input grid to select cells.
    - After selecting cells on the output grid, you can select a color from the color picking to set the color of the selected cells. This is useful to draw solid rectangles or lines.
    - After selecting cells on either the input grid or the output grid, you can press C to copy their content. After copying, you can select a cell on the output grid and press "V" to paste the copied content. You should select the cell in the top left corner of the zone you want to paste into.
- Floodfill: click on a cell from the output grid to color all connected cells to the selected color. "Connected cells" are contiguous cells with the same color.

### Answer validation

When your output grid is ready, click the green "Submit!" button to check your answer. We do not enforce the 3-trials rule.

After you've obtained the correct answer for the current test input grid, you can switch to the next test input grid for the task using the "Next test input" button (if there is any available; most tasks only have one test input).

When you're done with a task, use the "load task" button to open a new task.

### Summary
This section of the README file will cover python features and libraries used throughout the Solve_* functions that have been added to the manual_solve.py file. It will cover any commonalities or differences used in each of the tasks. There were 2 python libraries common across all tasks within the manual_solve.py file. These were:


#### 1. Import Json
The purpose of this library for these solutions, is to parse json files into python dictionaries or lists. This library was used at the beginning of each of the tasks. The library read in individual tasks which were then used within the solve functions in order to generate outputs that matched the correct solutions of the transformations. For each task, the JSON format of each file was input imported, and the "train" keys of the JSON files were used in order to determine a solution to each transformation. 


#### 2. Import Numpy as np 
This purpose of this library was to be able to work with arrays. As each of the tasks involved in this assignment were built using arrays it was an essential library required in order to complete each transformation task. The numpy library provides a range of mathematical operations that ca nbe performed on n-dimensional arrays. 

### Other Features and Methods used throughout the Solve_* Functions:
#### 1. Nested for Loops
The majority of the solve functions were built with the 'Nested for Loop' backbone for each solution. The nested for loops that were used, allowed me to segment each of the arrays into rows and columns, it also allowed me to get at each individual element of each array depending on each task. This meant I was able to isolate elements based on their values or locations within an array.  This was one of the most useful features that was used in the solutions as the transformations required an update to some or all of the elements present in each array. 

#### 2. if Statements
This feature was also common across a number of the solved tasks. The 'if statement' is a mechanism of determining whether or not a certain block of code should be executed or not. Using this simultaneously with the nested for loops meant I was able to transform specific rows, columns or elements of an array to a new value. This allowed me to perform operations on specific values in each training array and be able to create the correct outputs for a number of the tasks.

#### 3. Slicing 
Slicing was the main feature used to solve the 'solve_5614dbcf' function. This particular transformation required a reshape of the input array to mirror eactly the input, on a smaller scale, while transforming any outliers to the same colour. My solution to this was to use slicing to isolate each sub array in order to generate a correct output. This feature could be extremely beneficial for future solutions for similar tasks. 

#### 4. Array Manipulation 
Most of the solutions to the tasks used array manipulation of some sort in order to determine a correct output. This section covers the features used to solve the 'solve_3af2c5a8' function. This particular task required the  reshape of the size of the input array as well modifying the location of the elements. The most straight forward solution for me was to flip the array on both the Horizontal and vertical axis while appending each of these transformations onto either the end or bottom of the array to create a new array. This was done using the following numpy features:

       np.fliplr, np.hstack, np.flipud, np.vstack
       
#### 5. np.argmax(np.bincount(block.flat))
This feature allowed me to determine the highest value in an array by flattening the array into a 1D array and returning the value with the highest frequency present. This was required in one of the tasks to solve the transformation in order to determine what values to change any grey squares. 

### Reflection 
This assignment allowed me to explore and design functions to behave like humans and solve tasks in a way that a human would do, through the means of programming. Some of these tasks can be very easily solved by humans and determining the correct transformation for some of the more difficult task could be easily done by eye. However, converting this into programming language and expecting similar outcomes has showen me that it is a far more complex world then I'd first imagined. The use of the features discussed above, could be further enhanced and manipulated in order to tackle some of the more advanced transformations. I feel that the features used here are some of the fundamentals required to solve the vast library of ARC tasks. 

