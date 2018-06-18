#read names and marks
#rank sort top 3
#reward
#950+++ statement

import operator

def readdetails():
    # { }
    print()
    print ("give tha number of students mofo")
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
        print ("o {} erxete protos me aponomi 500 eurw kai {} marks".format(sorted_studentdetails[0][0], sorted_studentdetails[0][1]))
        print ("o {} erxete deuteros me aponomi 300 eurw kai {} marks".format(sorted_studentdetails[1][0], sorted_studentdetails[1][1]))
        print ("o {} erxete tritos me aponomi 100 eurw kai {} marks".format(sorted_studentdetails[2][0], sorted_studentdetails[2][1]))
        print()
        return sorted_studentdetails
    except IndexError:
        print("ase tis maimoudies ponire")
        quit()


def rewardstudent(sorted_studentdetails,reward):
    print()

    print ("{} protos me {}".format(sorted_studentdetails[0][0],reward[0]))
    print ("{} deuteros me {}".format(sorted_studentdetails[1][0],reward[1]))
    print ("{} tritos me {}".format(sorted_studentdetails[2][0],reward[2]))
    print()



def statement(sorted_studentdetails):
    print()
    for record in sorted_studentdetails:
        if record[1] >= 950:
            print ("{} gg pires {} pontous".format(record[0], record[1]))
        else:
            break
    print()


studentdetails = readdetails()
sorted_studentdetails=ranksort(studentdetails)
reward = (500,300,100)
rewardstudent(sorted_studentdetails, reward)
statement(sorted_studentdetails)
