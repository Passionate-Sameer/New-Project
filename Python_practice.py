##
##def table(num):
##    for n in range(1, num+1):
##        print
##        #print "n : ", n
##        for m in range(1, num+1):
##            #print "m : ", m
##            print m*n, '\t',
##number = int(raw_input("Please enter a number: "))
##table(number)

##string = 'sameer'
##for n in string:
##    print n,
##print string[0:3]
##print string[:]
##print string

##word = raw_input("Enter any fruit name: ")
##if word == "banana":
##    print "Yes, we have bananas!"
##elif word < "banana":
##    print "Your word, " + word + ", comes before banana."
##elif word > "banana":
##    print "Your word, " + word + ", comes after banana"
##else:
##    print "No, we DON'T have any banana!"

##def countLetters(word, letter):
##    count = 0
##    for n in word:
##        if n == letter:
##            count +=1
##    return count
##word = raw_input("Enter a word: ")
##letter = raw_input("Enter a letter to count its occurrence in the word: ")
##print "The letter", letter, "occurs", countLetters(word, letter), "times in the given word."

##string = "Sameer"
##length = len(string)
##list = []
##for n in range(length):
##    list.append(string[length - 1])
##    length -= 1
##print "".join(list)
##
##list = ['spam', 1, ['Brie', 'Roquefort', 'pol le vag'], [1, 2, 3]]
##list[2][1] = 'NEW'
##print list

##import string
##list = ["hello", [2, 5], [10, 20], ['A', 'B', 'C', 'D']]
##print string.join(list[3], '')
###print list		# Output will be ["hello", 2.0, 5, [10, 20], ['A', 'B', 'C']]

##import random
##s = []
##for i in range(10):
##    s.append(int(random.random()*100))
##print s

##def printout(n):
##    k = n
##    for i in range(n):
##        print ' O' * n
##        n = n-1
##    for m in range(k+1):
##        print ' O' * m
##
##    x = 0
##    z = k
##    for i in range(z):
##        print '  ' * x, 'O ' * z
##        z = z - 1
##        x = x + 1
##    for j in range(x+1):
##        print '  ' * x, 'O ' * z
##        x = x - 1
##        z = z + 1
##printout(10)


##list = [1, 2, 3, 4, 5]
##list[3:5] = [100, 1000]		#Square brackets are required to add an element
##print list 		# Output will be [1, 2, 3, 4, 5, 6]

##list1 = [1, 2, 3]
##list2 = [4, 5, 6]
##list3 = list1 + list2	# Lists can be concatenated by + operator
##print list3		# Output will be [1, 2, 3, 4, 5, 6]
##

##list = ["hello", 2.0, 5, [10, 20]]
##del list[-1]		# Element can be deleted
##print list		# Output will be ["hello", 2.0, 5]

##def letterCount(word):
##    letters = {}
##    for x in word:
##        letters[x] = letters.get(x, 0) + 1
##    sort_letters = letters.items()
##    sort_letters.sort()
##    print sort_letters
##word = raw_input("Please input a word and press enter: ")
##letterCount(word)

##import random
##def random_num(n):
##    s = []
##    for i in range(n):
##        s.append(int(random.random()*100))
##    return s
##n = int(raw_input("How many random number do you want to be displayed: "))
##print random_num(n)

##def copyFile(oldfile, newfile):
##    f1 = open(oldfile, "r")
##    f2 = open(newfile, "w")
##    while True:
##        text = f1.read(5)
##        if text == "":
##            break
##        f2.write(text)
##    #f2 = open(newfile, "r")
##    #print f2.read()
##    f1.close()
##    f2.close()
##    return
##oldfile = "D:/LEARNING/PYTHON/OLD.txt"
##newfile = "D:/LEARNING/PYTHON/NEW.txt"
##new = open(newfile, "r")
##print new.read()
##copyFile(oldfile, newfile)
##new = open(newfile, "r")
##print new.read()
##new.close()

##f = open("D:/LEARNING/PYTHON/OLD.txt", "w")
##f.write("Line one\nLine two\nLine three\n")
##f.close()
##f = open("D:/LEARNING/PYTHON/OLD.txt", "r")
##print f.readline()
##print f.readlines()
##print f.readline()
##print f.readlines()

##def copyFile(oldfile, newfile):
##    f1 = open(oldfile, "r")
##    f2 = open(newfile, "w")
##    while True:
##        text = f1.readline()
##        if text == "":
##            break
##        if text[0] == '#':
##            continue
##        f2.write(text)
##    f1.close()
##    f2.close()
##    return
##oldfile = "D:/LEARNING/PYTHON/OLD.txt"
##newfile = "D:/LEARNING/PYTHON/NEW.txt"
##copyFile(oldfile, newfile)
##new = open(newfile, "r")
##print new.read()
##new.close()
##
##marks = {"Sameer": 28.6, "Sona": 25.9, "Manish": 24.8, "Varsha":21.9}
##def report (marks):
##    students = marks.keys()
##    students.sort()
##    for student in students:
##        print "%-20s %12.2f" % (student, marks[student])
##report(marks)


###Create a program that asks the user to enter their name and their age.
###Print out a message addressed to them that tells them the year that they
###will turn 100 years old.
##from datetime import date
##name = raw_input("Please enter your name: ")
##age = int(raw_input("Please enter your age: "))
##current_year = date.today().year
##diff_age = 100 - age
##turn_hundred = current_year + diff_age
##print "The year in which %s will turn 100 is %d" % (name, turn_hundred)
##times = int(raw_input("Please enter a number: "))
##print times*("The year in which %s will turn 100 is %d\n" % (name, turn_hundred))
##

###Number is EVEN OR ODD
##number = int(raw_input("Please enter a number: "))
##if number%2==0:
##    print "The number(%d) you have entered is an EVEN number" % number
##    if number%4==0:
##        print "The number(%d) you have entered is divisible by 4" % number    
##else:
##    print "The number(%d) you have entered is an ODD number" % number


###A program that prints out all the elements of the list that are less than 5
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##print "The given list is ", a
##number = int(raw_input("Please enter a number: "))
##print "The numbers in this list that are less than %d are " % number
##new_list=[]
##for n in a:
##    if n < number:
##        new_list.append(n)
##print new_list

##number = int(raw_input("Please enter a number: "))
##divisors=[]
##for n in range(1, number+1):
##    if number%n == 0:
##        divisors.append(n)
##print divisors


##while True:
##    try:
##        n = int(raw_input("Please choose a number to divide: "))
##        list = [d for d in range(1, n + 1) if n % d == 0]
##        if len(list) > 2:
##            print "The divisors of %d are: " % n, list
##        else :
##            print str(n) + " is a prime number"
##    except ValueError:
##        print "\nVery funny smartness. Now give me a number."
##    try:
##        cont = raw_input("Do you want to continue(Y/N): ")
##        if cont == 'n' or cont == 'N':
##            break
##    except:               #except statement not correct
##        print "Program has exited!!" 


##def check_if_present(n):
##    for k in list:
##        if n == k:
##            return True
##        else:
##            return False



##import random
##def random_list(n):
##    s = [int(random.random()*100) for i in range(n)]
####    s = []
####    for i in range(n):
####        s.append(int(random.random()*100))
##    return s
##try:
##    n1 = int(raw_input("\nHow many random numbers do you want in list 1: "))
##    n2 = int(raw_input("How many random numbers do you want in list 2: "))
##    list1 = random_list(n1)
##    list2 = random_list(n2)
##    print "The two lists with random numbers are\n", list1, '\n', list2
##    #list = []
##    for n in list1:
##        list = [n for m in list2 if n == m and n not in list]
####      for m in list2:
####          if n == m and n not in list:
####              list.append(n)
##    if len(list) == 0:
##        print "There are no common numbers in the list"
##    else:
##        print "List of common numbers in two lists is: ", list
##except ValueError: 
##    print "\nINVALID input. Program is terminating!!!"

###Combining similar items of two lists into one
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
##c = list(set([x for x in a for y in b if x == y]))
##print c
##
### for randomly generated lists!
##import random
##a, b = random.sample(range(100),10), random.sample(range(100),10)
##c = list(set([x for x in a for y in b if x == y]))
##print c
##
###Print out whether user given string is a palindrome or not
##user_string = raw_input("Please enter a string: ")
##string_to_lowercase = user_string.lower()
##if string_to_lowercase[::-1] == string_to_lowercase:    #Reversing a string
##    print "The string you have entered is a Palindrome"
##else:
##    print "The string you have entered is NOT a Palindrome"
##

### Code for "Do you want to continue(y/n): "
##condition = True
##while condition:
##
##
##    print "Awesome"
##
##
##    reply = raw_input("\nDo you want to continue(Y/N): ")
##    if reply == 'N' or reply == 'n':
##        condition = False


#Program for "Rock, Paper, Scissors" game
#Game can be played with computer or with another player
def rules():
    print "\nRules: \nROCK beats SCISSORS\nSCISSORS beats PAPER\nPAPER beats ROCK"

def print_selection(player_1, player_2, player_1_name, player_2_name):
    print "%s chose %s and %s chose %s" % (player_1_name.upper(), convert_to_word(player_1), player_2_name.upper(), convert_to_word(player_2))
    
def clear_screen():
    for n in range(20):
        print '\n'

def convert_to_word(player):
    if player == 'r':
        return "ROCK"
    if player == 's':
        return "SCISSORS"
    if player == 'p':
        return "PAPER"

def check_if_play_again():
    condition = True
    while condition:
        play_again = raw_input("\nDo you want to play again (Y/N): ").lower()
        if play_again == 'n':
            print "\nThanks for playing. Hope you enjoyed!\n"
            condition = False
        elif play_again == 'y':
            return play_with()
        
def player_input(player_name):
    while True:
        print "\t\t\t%s \n\nIt's your turn: Please choose between Rock, Paper, Scissors." % player_name.upper()
        player = raw_input("Press R for Rock, P for Paper, S for Scissors: ").lower()
        if player == 'r' or 's' or 'p':   
            return player
        else:
            print "\n\nPlease provide a valid input."

import random
def computer_input():
    comp_turn = random.sample(range(1,4),1)
    if comp_turn == [1]:
        return 'r'
    elif comp_turn == [2]:
        return 's'
    elif comp_turn == [3]:
        return 'p'

def play_with_computer():
    print "\nYou chose to play with Computer!"
    player_1_name = raw_input("Please enter your name: ")
    player_2_name = 'COMPUTER'
    clear_screen()
    player_1 = player_input(player_1_name)
    player_2 = computer_input()
    check_who_wins(player_1, player_2, player_1_name, player_2_name)    

def play_with_friend():
    print "\nYou chose to play with friend!"
    player_1_name = raw_input("Player 1: Please enter your name: ")
    player_2_name = raw_input("Player 2: Please enter your name: ")
    clear_screen()
    player_1 = player_input(player_1_name)
    clear_screen()
    player_2 = player_input(player_2_name)
    check_who_wins(player_1, player_2, player_1_name, player_2_name)
    
def play_with():
    while True:
        print "\nDo you want to play with computer or with your friend?"
        comp_or_frnd = raw_input("Press C for computer or F for friend: ").lower()
        if comp_or_frnd == 'c': 
            return play_with_computer()
        elif comp_or_frnd == 'f':
            return play_with_friend()
        else:
            print "\n\nPlease provide a valid input."

def check_who_wins(player_1, player_2, player_1_name, player_2_name):
    if player_1 == player_2:
        print "\nIt's a tie! Both of you chose %s" % (convert_to_word(player_1))
    else:
        if ((player_2_name == 'COMPUTER') and \
            ((player_2 == 'r' and player_1 == 's') or \
                (player_2 == 's' and player_1 == 'p') or \
                (player_2 == 'p' and player_1 == 'r'))):
                print "\nCOMPUTER Won! You Lose. Better luck next time..."
                print_selection(player_1, player_2, "You", player_2_name)
                rules()
        else:
            if(player_1 == 'r' and player_2 == 's') or \
                (player_1 == 's' and player_2 == 'p') or \
                (player_1 == 'p' and player_2 == 'r'):
                print "\n%s Won!  CONGRATULATIONS!!!" % player_1_name.upper()
                print_selection(player_1, player_2, player_1_name, player_2_name)
                rules()
            elif(player_2 == 'r' and player_1 == 's') or \
                (player_2 == 's' and player_1 == 'p') or \
                (player_2 == 'p' and player_1 == 'r'):   
                print "\n%s Won!  CONGRATULATIONS!!!" % player_2_name.upper()
                print_selection(player_1, player_2, player_1_name, player_2_name)
                rules()
    check_if_play_again()

clear_screen()
print "Welcome to Rock, Paper, Scissors game!"
play_with()
