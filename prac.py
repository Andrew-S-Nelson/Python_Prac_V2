#!/usr/bin/env python3

def q1(sentence):
    '''
    Given a string of multiple words separated by single spaces,
    return a new string with the sentence reversed. The words
    themselves should remain as they are. For example, given
    'it is accepted as a masterpiece on strategy', the returned
    string should be 'strategy on masterpiece a as accepted is it'.
    '''
    # split string into list of words
    Mylist = sentence.split(' ')
    print(Mylist)

    # parse through list and append to new list
    Newlist = []
    for i in range(len(Mylist) -1,-1,-1):
        Newlist.append(Mylist[i])

    print(Newlist)

    # return list
    outstr = ' '.join(Newlist)
    return outstr
    pass


def q2(n):
    '''
    Given a positive integer, return its string representation with
    commas seperating groups of 3 digits. For example, given 65535
    the returned string should be '65,535'.
    '''
    return '{:,}'.format(n)

def q3(lst0, lst1):
    '''
    Given two lists of integers, return a sorted list that contains
    all integers from both lists in descending order. For example,
    given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1].
    The returned list may contain duplicates.
    '''
    joinlist = lst0 + lst1
    joinlist.sort(reverse = True)
    return joinlist

def q4(s1,s2,s3):
    '''
    Given 3 scores in the range [0-100] inclusive, return 'GO' if
    the average score is greater than 50. Otherwise return 'NOGO'.
    '''

    listavg = (s1 + s2 + s3) / 3
    if listavg > 50:
        return 'GO'
    else:
        return 'NOGO'

def q5(integer, limit):
    '''
    Given an integer and limit, return a list of even multiples of the
    integer up to and including the limit. For example, if integer==3 and
    limit==30, the returned list should be [0,6,12,18,24,30]. Note, 0 is
    a multiple of any integer except 0 itself.
    '''
    outlist = []
    for i in range(0,limit + 1, 1):
        if (i % integer == 0) and (i % 2 == 0):
            #print(i)
            outlist.append(i)
    return outlist

    pass

#print(q5(10, 30))

def q6(f0, f1):
    '''
    Given two filenames, return a list whose elements consist of line numbers
    for which the two files differ. The first line is considered line 0.
    '''
    list1 = []
    with open(f0) as fp:
        for line in fp:
            list1.append(line)
    
    list2 = []
    with open(f1) as fp:
        for line in fp:
            list2.append(line)
    
    outlist = []
    for i in range(0, len(list1)):
        #print(i, end=' ')
        #print('Does', list1[i], 'equal', list2[i])
        if list1[i] != list2[i]:
            outlist.append(i)
    return outlist
#q6('1','2')

def q7(lst):
    '''Return the first duplicate value in the given list.
    For example, if given [5,7,9,1,3,7,9,5], the returned value should
    be 7.'''
    '''mylist = []
    for item in lst:    
        mylist.append(item)
        #print(item, mylist.count(item))
        if (mylist.count(item) > 1):
            return item'''

    uniquelist = []
    duplicatelist = []
    for item in lst:
        if item not in uniquelist:
            uniquelist.append(item)
        elif item not in duplicatelist:
            duplicatelist.append(item)
    return duplicatelist[0]

#q7([5,7,9,1,3,7,9,5])
    
    

def q8(strng):
    '''
    Given a sentence as a string with words being separated by a single space,
    return the length of the shortest word.
    '''
    mylist = strng.split()
    length = 9999
    for word in mylist:
        if len(word) < length:
            length = len(word)
    return length

def q9(strng):
    '''
    Given an alphanumeric string, return the character whose ascii value
    is that of the integer represenation of all of the digits in the string
    concatenated in the order in which they appear. For example, given
    'hell9oworld7', the returned character should be 'a' which has
    the ascii value of 97.
    '''
    # create list of characters
    charlist = list(strng)
    print(charlist)

    # iterate through list and grab numbers
    numlist = []
    for character in charlist:
        if character.isnumeric():
            numlist.append(character)
    print(numlist)

    # join number list and typecast as integer
    integer = int(''.join(numlist))
    print(integer)

    # turn integer into character using ascii
    print("'{}'".format(chr(integer)))
    return "{}".format(chr(integer))

#q9('hell9oworld7')

def q10(arr):
    '''
    Given a list of positive integers sorted in ascending order, return
    the first non-consecutive value. If all values are consecutive, return
    None. For example, given [1,2,3,4,6,7], the returned value should be 6. 
    '''
    '''print(arr)
    prev = arr[0] - 1
    for item in arr:
        print('Does', item, '=', prev + 1)
        if item != prev + 1:
            return item
        prev = item
    return None'''
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
