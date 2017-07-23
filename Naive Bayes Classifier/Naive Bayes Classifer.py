
# coding: utf-8

# In[5]:

import operator


# In this problem we will find the maximum likelihood word based on the preceding word Fill in the NextWordProbability procedure so that it takes in sample text and a word,and returns a dictionary with keys the set of words that come after, whose values are the number of times the key comes after that word.

# In[1]:

def NextWordProbability(sampletext,word):
    myDict = dict()
    lst = sampletext.split(" ")
    if word in lst:
        lstUpdate = lst[lst.index(word)+1]
        myDict[lstUpdate] = lst.count(lstUpdate)
    return myDict


# In[2]:

#------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#
sample_memo = """Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, 
and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, 
that would be terrific, OK? Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go 
ahead and wear a Hawaiian shirt and jeans. Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and 
come in on Sunday, too...Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So 
if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to 
go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up."""


corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead","could"]


# In[4]:

def LaterWords(sample,word,distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''
    import operator
    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    firstWord = NextWordProbability(sample,word).keys()[0]
    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.

    myDict2 = dict()
    lstUpdate2 = list()
    for i in range(len(data_list)):
        if firstWord == data_list[i]:
            lstUpdate2.append(data_list[i+1])
    for word in lstUpdate2:
        myDict2[word] = lstUpdate2.count(word)
    sumOfVal = sum(myDict2.values())
    # Calculate Second Word Probability given First Word
    probabilities2 = {k: v / float(sumOfVal) for k, v in myDict2.iteritems()}
    sortedDict = sorted(probabilities2.items(), key=operator.itemgetter(1), reverse=True)
    
    return sortedDict[0][0]


# In[ ]:



