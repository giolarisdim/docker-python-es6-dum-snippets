#read names and marks
#rank sort top 3
#reward
#950+++ statement

import operator

def readdetails():
    # { }
    print()
    print ("please enter the number of students")
    numberofstudents = int(input())
    studentdetails = {}
    for students in range(0,numberofstudents):
        print ("give the name of student")
        name = input()
        print ("give his mark")
        mark = int(input())
        studentdetails[name]=mark
    print()
    return studentdetails

def ranksort(studentdetails):
    try:


        print()
        sorted_studentdetails = sorted(studentdetails.items(), key=operator.itemgetter(1),reverse = True)
        print(sorted_studentdetails)
        print (" {} is hitting the first place with a reward of 500 eurw and {} marks".format(sorted_studentdetails[0][0], sorted_studentdetails[0][1]))
        print (" {} is hitting the second place with a reward of 300 eurw and {} marks".format(sorted_studentdetails[1][0], sorted_studentdetails[1][1]))
        print (" {} is hitting the third place with a reward of 100 eurw and {} marks".format(sorted_studentdetails[2][0], sorted_studentdetails[2][1]))
        print()
        return sorted_studentdetails
    except IndexError:
        print("aint no such thing as giving wrong numbers, enter the right one please")
        quit()


def rewardstudent(sorted_studentdetails,reward):
    print()

    print ("{} first with {}".format(sorted_studentdetails[0][0],reward[0]))
    print ("{} second with {}".format(sorted_studentdetails[1][0],reward[1]))
    print ("{} third with {}".format(sorted_studentdetails[2][0],reward[2]))
    print()



def statement(sorted_studentdetails):
    print()
    for record in sorted_studentdetails:
        if record[1] >= 950:
            print ("{} congratulations! You allready have gather {} points".format(record[0], record[1]))
        else:
            break
    print()


studentdetails = readdetails()
sorted_studentdetails=ranksort(studentdetails)
reward = (500,300,100)
rewardstudent(sorted_studentdetails, reward)
statement(sorted_studentdetails)
