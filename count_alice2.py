# Norma
# count_alice2.py:
# Starting code for H7-1
#**************************
FILENAME = 'alice.txt'

fvar = open (FILENAME, 'r') # open file for reading

allwords = [] # accumulate the words in this list

for aline in fvar:
    mod_aline = aline.lower()

    mod_aline = mod_aline.replace('--', ' ')
    for punct in '!"#$%&()*+,./:;<=>?@[]^_`{|}~':
        mod_aline = mod_aline.replace(punct, ' ')
    words = mod_aline.split() # splits the line on whitespace (blanks, '\n', '\t')
    print (words) # just to see the words flying across the screen...

    # allwords.append(words) # why doesn't this work?
    allwords.extend(words) # this does...

    # allwords = allwords + words # as does this - but why is this inefficient?
allwords.sort()
clean_allwords =[]

for word in allwords:
    if word is not "'":
        clean_allwords.append(word)

# if len(word)> longest_length_so_far:
#     longest_word_so_far = [word]

for word in clean_allwords:
    print(word)
#print(allwords)
print("there are", len(clean_allwords), "words in Alice in Wonderland")
# print("longest words have length", longest_length_so_far)
print("there are", len(allwords), "words in Alice in Wonderland")
fvar.close()


#********************************************
# FILENAME = 'alice.txt'
#
# fvar = open(FILENAME, 'r')  # open file for reading
#
# allwords = []  # accumulate the words in this list
#
# for aline in fvar:
#
#     line = aline.lower()  # lower case it
#     line = line.replace('--', ' ')  # replace Victorian --
#
#     words = line.split()  # splits the line on whitespace (blanks, '\n', '\t')
#
#     for next_word in words:
#         allwords.append(next_word)  # add word + its line number as tuple to allwords
#
# print(len(allwords))
