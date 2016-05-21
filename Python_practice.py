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

import random
def random_num(n):
    s = []
    for i in range(n):
        s.append(int(random.random()*100))
    return s
n = int(raw_input("How many random number do you want to be displayed: "))
print random_num(n)









