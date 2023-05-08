import numpy as np 
categoryOfProblem = ['easy', 'medium', 'hard']
numberOfProblems = [662, 1419, 592] #easy, medium, hard

def pickEasy():
    print(f"{categoryOfProblem[0]}: {np.random.randint(1, numberOfProblems[0], 1)}")

def pickMedium():
    print(f"{categoryOfProblem[1]}: {np.random.randint(1, numberOfProblems[1], 1)}")

pickEasy()
for i in range(2):
    pickMedium()