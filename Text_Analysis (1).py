import re
import os
import pandas as pd
os.chdir(r'E:\Internship\Good_Boy')

file_list = [i for i in os.listdir() if ".txt" in i]
print(file_list)

# 1 Cleaning using Stop Words Lists

def clean_words(file_name):
    data = open("%s" %file_name).read()
    stop_words = open("stop_words.txt","r").read()
    stop_free = []
    for word1 in data.split():
        if word1.lower() not in stop_words:
            stop_free.append(word1) 
    total_words_af_cl = len(stop_free)
    return total_words_af_cl


#Creating a dictionary of Positive and Negative words

# Positive Score

def positive_score(file_name):
    data = open("%s" %file_name).read()
    stop_words = open("stop_words.txt","r").read()
    positive_words = open("positive-words.txt","r").read()
    stop_free = []
    for word1 in data.split():
        if word1.lower() not in stop_words:
            stop_free.append(word1) 
    positive_score_count = []
    for word1 in stop_free:
        if word1.lower() in positive_words:
            positive_score_count.append(word1)
    count = len(positive_score_count)
    return count


    # Negative Score

def negative_score(file_name):
    data = open("%s" %file_name).read()
    stop_words = open("stop_words.txt","r").read()
    negative_words = open("negative-words.txt","r").read()
    stop_free = []
    for word2 in data.split():
        #print(word2)
        if word2.lower() not in stop_words:
            stop_free.append(word2) 
    negative_score_count = []
    #print(stop_free)
    for word2 in stop_free:
        if word2.lower() in negative_words:
            negative_score_count.append(word2)
    count_2 = len(negative_score_count)
    return count_2


# Polarity Score

def polarity_score(file_name):
    # data = open("%s" %file_name).read()
    Polarity_Score = (positive_score(file_name) - negative_score(file_name))/((positive_score(file_name) + negative_score(file_name)) + 0.000001)
    return Polarity_Score


# Subjectivity Score
def subjectivity_score(file_name):
    Subjectivity_Score = (positive_score(file_name) + negative_score(file_name))/ ((clean_words(file_name)) + 0.000001)
    return Subjectivity_Score


# 2 Analysis of Readability
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count




# Average Number of Words Per Sentence

def avg_sentence_len(file_name):
   data = open("%s" %file_name).read()
   sentences = data.split(".") #split the text into a list of sentences.
   words = data.split(" ") #split the input text into a list of separate words
   if(sentences[len(sentences)-1]==""): #if the last value in sentences is an empty string
    average_sentence_length = len(words) / len(sentences)-1
   else:
     average_sentence_length = len(words) / len(sentences)
   return average_sentence_length #returning avg length of sentence


#Complex Word Count


def percentage_of_complex_words(file_name):
    sentence = []
    data = open("%s" %file_name).read()
    for word in data.split():
        sentence.append(word)
    com_word = []
    for i in sentence:
        if syllable_count(i) >2:
            com_word.append(i)
    num_comp_words = len(com_word)
    tot_words = len(sentence)
    percentage_of_comp_words = num_comp_words/tot_words
    return percentage_of_comp_words # percentage of complex words

# Fog Index

def fog_index(file_name):
    data = open("%s" %file_name).read()
    avg_sentence_len(file_name)
    percentage_of_complex_words(file_name)
    fog_index = 0.4 * (avg_sentence_len(file_name) + percentage_of_complex_words(file_name))
    return fog_index


def anwps(file_name):
    data = open("%s" %file_name).read()
    sentences = data.split(".")
    sentence = []
    for word in data.split():
        sentence.append(word)
    tot_words = len(sentence)
    anwps = tot_words/len(sentences)
    return anwps



# Complex word count

def len_of_complex_words(file_name):
    sentence = []
    data = open("%s" %file_name).read()
    for word in data.split():
        sentence.append(word)
    com_word = []
    for i in sentence:
        if syllable_count(i) >2:
            com_word.append(i)
    num_comp_words = len(com_word)
    return num_comp_words



# Word Count

def clean_words(file_name):
    data = open("%s" %file_name).read()
    stop_words = open("stop_words.txt","r").read()
    stop_free = []
    for word1 in data.split():
        if word1.lower() not in stop_words:
            stop_free.append(word1) 
    total_words_af_cl = len(stop_free)
    return total_words_af_cl




def syllable_count_per_word(file_name):
    data=open("%s" %file_name).read()
    total_characters = []
    for word in data:
        total_characters.append(syllable_count(word))
    sentence=[]
    for word in data.split():
        sentence.append(word)
    av_word_length = sum(total_characters)/len(sentence)
    return av_word_length


def count_personal_pronoun(file_name):
    data=open("%s" %file_name).read()
    pronoun_count = []
    pronounRegex = re.compile(r'\bI\b|\bwe\b|\bWe\b|\bmy\b|\bMy\b|\bours\b|\bus\b')
    l=pronounRegex.findall(data)
    countl=len(l)
    pronoun_count.append(countl)
    return pronoun_count



def average_word_length(file_name):
    data=open("%s" %file_name).read()
    total_characters = []
    for word in data:
        character=0
        for word in word.split():
            character+=len(word)
            total_characters.append(character)
    sentence=[]
    for word in data.split():
        sentence.append(word)
    av_word_length = sum(total_characters)/len(sentence)
    return av_word_length

avg_word_length = []
personal_pronoun = []
syllable = []
word_count = []
comp_words = []
avg_wps = []
fog_idex = []
complex_words_percentage = []
avg_sent_length = []
sub_score = []
pol_score = []
neg_score = []
pos_score = []
for file_name in file_list:
    pos_score.append(positive_score(file_name))
    neg_score.append(negative_score(file_name))
    pol_score.append(polarity_score(file_name))
    sub_score.append(subjectivity_score(file_name))
    avg_sent_length.append(avg_sentence_len(file_name))
    complex_words_percentage.append(percentage_of_complex_words(file_name))
    fog_idex.append(fog_index(file_name))
    avg_wps.append(anwps(file_name))
    comp_words.append(len_of_complex_words(file_name))
    word_count.append(clean_words(file_name))
    syllable.append(syllable_count_per_word(file_name))
    personal_pronoun.append(count_personal_pronoun(file_name))
    avg_word_length.append(average_word_length(file_name))


data=pd.DataFrame({"FILE_ID":file_list,"POSITIVE_SCORE":pos_score,"NEGATIVE_SCORE":neg_score,"POLARITY_SCORE":pol_score,"SUBJECTIVITY_SCORE":sub_score,"AVERAGE_SENTENCE_LENGTH":avg_sent_length,"PERCENTAGE_OF_COMPLEX_WORDS":complex_words_percentage,"FOG_INDEX":fog_idex,"AVERAGE_NUMBER_OF_WORDS_PER_SENTENCE":avg_wps,"COMPLEX_WORD_COUNT":comp_words,"CLEAN_WORDS_COUNT":word_count
,"SYLLABLE_PER_WORD":syllable,"COUNT_OF_PERSONAL_PRONOUN":personal_pronoun,"AVERAGE_WORD_LENGTH":avg_word_length})



data.to_csv('output.csv')




  
