# Puzzle-Students-Locker
# Problem Description
A high school has "n" number of students and "m" number of Lockers.
For Simplicity we are taking 100 students and 100 Lockers.
On the first day of School the principal plays the following game: 
She asks the first student to go and close all the lockers. She then asks 
the second student to go and close all the even-numbered lockers. The third
student is asked to check every third locker. If it is open, then student closes it; 
and if it is closed the opens it. The fourth student is asked to check every fourth locker.
If it is open the student closes it and if it is closed the student opens it.
The remaining students continue this game. In general, the nth Student checks every nth
Locker. if the locker is Open, the student closes it and if it is closed then open it.
After all the students have taken their turn, some of the lockers are open and some are closed.
your job is to tell how many lockers are open at the end of the game. and if
we take 100 students and 100 lockers the result should be 10

# Task to do
There are two main tasks to do 
# 1 
    You have to implement this senario using a function named "OpenLocks()",
    which takes two input parameters i.e number_of_lockers and
    number_of_students that returns the number of lockers that are opened.
# 2
    Your job now, is to write a function named "mostTouchableLocker()" which
    takes  two input parameters i.e number_of_lockers and number_of_students
    that returns the locker number which is touched by the most of the students
# Note:
There is a slight confusion in the current assignment, where in some cases
there are multiple lockers(instead of one) that are touched the most.
One instance of such a case is that if you have 10 students and 10 lockers, 
the locker number 6,8 and 10 are all touched the most i.e 4 times. If you
have such a situation you can just return the last locker among the most touched
lockers which in this case is the 10th locker.