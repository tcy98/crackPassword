#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:14:57 2020

@author: t.t
"""
import hashlib

# declear list
cipher = []

password = []
random_str = []
pair = []

f = open("password.txt",'w')

def checkPassword(guesses):
    print('number of guesses: ',len(guesses))
    count = 0
    for line in cipher:
        flag = False
        count += 1
        print(count)
        for g in guesses:
            ghex = hashlib.sha256(g.encode().strip()).hexdigest()
            # print('guess:', ghex)
            if line == ghex:
                flag = True
                f.write(line + ':' + g + '\n')
                print('found')
                break
        if flag == False:
            f.write(line + ':' + '\n')
    f.close()

# return list of possible word
import itertools


def dic_attack():
    result = []
    with open("10k-most-common.txt") as d:
        from itertools import islice
        for line in d:
           #get all upper case lower case combination 
           m = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in line.strip())))
           result.extend(list(m))
    return result

import random
import string

#create 1000 random string with length 2-6 
def brute_force_setup():
    num_random_str = 10000
    #one letter: add all
    random_str.extend(list(string.ascii_letters+string.digits))
    for a in range(2,7):
        x = 0
        while x < num_random_str:
            #create random string with 6 char
            str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(a)])
            print(str)
            random_str.append(str)
            x += 1
    # print(random_str)
    return random_str
    

def add_punctuation(): #10k took so long so use best1050.txt instead
    add = list('!@#&*' + string.digits) #add puncs and digits
    print(add)
    result = []
    
    with open("1-1000.txt") as d:
        for line in d[:500]:
            for a in add:
                result.append(line.strip() + a)
    #two more at the end
    for r in result:
        print(r)
        for a in add:        
            result.append(r + a)
    for r in result:
        print(r)
        for a in add:        
            result.append(r + a)
    for r in result:
        print(r)
        for a in add:        
            result.append(r + a)
    return result

import re
def replace_letter():
    # a=4,@ i = 1 0 = o,O
    
    result = []
    with open("google-10000-english.txt") as d:

        for line in d:
            line = line.strip()
            t1 = re.subn('a','@',line)
            t2 = re.subn('o','0',line)   #return 0 in tuple[1] if not found
            
            if t1[1] == 0 and t2[1] == 0:
                pass
            elif t1[1] > 0 and t2[1] > 0: #there are both character chagned
                
                result.append(t1[0])
                result.append(t2[0])
                #change t1's o to 0 as well
                t3 = re.sub('o','0',t1[0])
                print('t3:', t3)
                result.append(t3)
            elif t1[1] > 0:
                result.append(t1[0])
            elif t2[1] > 0:
                result.append(t2[0])
            else:
                print('shouldnt happen')

        
    
    return result

#twoenglishWord
def appendWord():
    result = []
    words = []
    with open("google-10000-english.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    for i in words[:500]:   #no way i can finish all 10k files
        print(i)
        for q in words:
            result.append(i+q)
            result.append(i.title()+q)
            result.append(i+q.title())
            result.append(i.title()+q.title())
     
    return result
#twoenglishWord (found nothing)
def longword():
    result = []
    words = []
    #longword in wiki-100k.txt
    with open("wiki-100k.txt", "r") as f:
        for line in f:
            if(len(line) > 11 and line[0] != '#'):
                print(line.strip())
                words.append(line.strip())
    # wordlist from https://www.lexico.com/explore/what-is-the-longest-english-word
    with open("longWord.txt", "r") as f:
        for line in f:
            print(line.strip())
            words.append(line.strip())
    for i in words:
        # if len(i) <26 and len(i) > 11:
        result.append(i)
     
    return result

def useEnglishWord():
    result = []
    words = []
    with open("google-10000-english.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    for i in words:
        print(i)
        for q in words:
            result.append(i+q)
            result.append(i.title()+q)
            result.append(i+q.title())
            result.append(i.title()+q.title())
    for line in words:
        t1 = re.subn('a','@',line)
        t2 = re.subn('o','0',line)   #return 0 in tuple[1] if not found        
        if t1[1] == 0 and t2[1] == 0:
            pass
        elif t1[1] > 0 and t2[1] > 0: #there are both character chagned
            result.append(t1[0])
            result.append(t2[0])
            #change t1's o to 0 as well
            t3 = re.sub('o','0',t1[0])
            print('t3:', t3)
            result.append(t3)
        elif t1[1] > 0:
            result.append(t1[0])
        elif t2[1] > 0:
            result.append(t2[0])
        else:
            print('shouldnt happen')

def combinations():
    result = []
    for i in range(1,5):
        keywords = [''.join(i) for i in itertools.product(string.digits+string.ascii_letters, repeat = i)]
        result.extend(keywords)
    return result


def main():
    with open("hashes.txt", "r") as f:
        for line in f:
            cipher.append(line.strip())
    guesses =[]
   
    # guesses.extend(dic_attack())
    # guesses.extend(brute_force_setup())
    # print(guesses)
    # guesses.extend(appendWord())
    # guesses.extend(combinations())
    guesses.extend(longword())
    # guesses.extend(add_punctuation())
    # guesses.extend(replace_letter())
    checkPassword(guesses)

    

    


if __name__ == "__main__":
    main()
