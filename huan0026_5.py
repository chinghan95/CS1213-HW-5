"""
Ching Han Huang
113510994
11/15/19

Assignment 5 : Practice With Dictionaries
"""

response = ""
d = {}

while response != 'quit':
    response = input('Would you like to enter new data, see a summary of data, or quit? (Enter ’new’ or ’summary’ or ’quit’): ')

    # Store user's input in dictionary
    # student name is keys of dict
    # assignment name is the value of student name also the key of grade
    # grade is the value of assignment name
    if response == 'new':
        studentName = input('Student name: ')
        assignmentName = input('Assignment name: ')
        grade = int(input('Grade: '))
        if (studentName not in d):
            d[studentName] = {}
        d[studentName][assignmentName] = grade
        # print(d)

    elif response == 'summary':
        seeScore = input('Would you like to see a ’total’ summary or summary of assignment ’average’ grades?')
        
        # create a set called assignments to store all the assignment name
        if seeScore == 'average':
            assignments = set()
            for studentName in d:
                for assignmentName in d[studentName]:
                    assignments.add(assignmentName)

            # use for loop to calculate all the grades of specific assignment
            # if some student doesn't have specific assignment grade,
            # 'continue' will ignore it and check next student
            for a in assignments:
                total = 0
                count = 0
                for studentName in d:
                    if a not in d[studentName]:
                        count = count + 1
                        continue
                    total = total + d[studentName][a]
                print(f'{a} average: {total/(len(d)-count)}')

        # use 'sum' to calculate the grades of specific student
        if seeScore == 'total':
            for studentName in d:
                total = sum(d[studentName].values())
                print(f'{studentName} average: {total/len(d[studentName])}')

print('Thanks for using my program.')


