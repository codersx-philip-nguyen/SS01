from collections import Counter

'''
@overview: get the positive words list
@input: file data
@output: list of positive word
'''
def _getPositive_n_Negative_Words(file):
    file = open(file, 'r')
    raw_data = file.readlines()

    negative_val = '0'
    quite_negative = '1'
    neutral_val = '2'
    quite_positive = '3'
    postive_val = '4'

    data_list = []

    sub_postive = []
    sub_quite_negative = []
    sub_neutral = []
    sub_negative = []
    sub_quite_positive = []

    quite_negative_words = []
    positive_words = []
    neutral_words = []
    quite_positive_words =[]
    negative_words =[]
    regex = [".", ","]
    # remove the newline sign
    for i in range(len(raw_data)):
        e = raw_data[i].rstrip('\n').strip("")
        data_list.append(e)

    #loop through the datalist -> get the list of positive and negative word
    for line in data_list:
        for char in line:
            if char in regex:
                line.replace(char, '')
        if negative_val in line:
            line = line.replace('0 ', '')
            sub_negative.append(line)
        if quite_negative in line:
            line = line.replace('1 ', '')
            sub_quite_negative.append(line)
        if neutral_val in line:
            line = line.replace('2 ', '')
            sub_neutral.append(line)
        if quite_positive in line:
            line = line.replace('3 ', '')
            sub_quite_positive.append(line)
        if postive_val in line:
            line = line.replace('4 ', '')
            sub_postive.append(line)


    for i in range(len(sub_postive)):
        e = sub_postive[i].split()
        positive_words.append(e)
        positive_final = [item for sublist in positive_words for item in sublist]
    for i in range(len(sub_negative)):
        e = sub_negative[i].split()
        negative_words.append(e)
        negative_final = [item for sublist in negative_words for item in sublist]
    for i in range(len(sub_neutral)):
        e = sub_neutral[i].split()
        neutral_words.append(e)
        neutral_final = [item for sublist in neutral_words for item in sublist]
    for i in range(len(sub_quite_negative)):
        e = sub_quite_negative[i].split()
        quite_negative_words.append(e)
        quite_negative_final = [item for sublist in quite_negative_words for item in sublist]
    for i in range(len(sub_quite_positive)):
        e = sub_quite_positive[i].split()
        quite_positive_words.append(e)
        quite_positive_final = [item for sublist in quite_positive_words for item in sublist]

    return (negative_final, quite_negative_final,neutral_final, quite_positive_final, positive_final)

def getScore(word, file):
    (list1, list2, list3, list4, list5) = _getPositive_n_Negative_Words(file)
    scores = []

    if word in list1:
        scores.append(0)
    if word in list2:
        scores.append(1)
    if word in list3:
        scores.append(2)
    if word in list4:
        scores.append(3)
    if word in list5:
        scores.append(4)
    sum_ = sum(scores)

    if(len(scores) == 0):
        return "can't find the word"
    else:
        score = sum_ / len(scores)

    if score == 2:
        word_kind = 'neutral'
    elif score > 2:
        word_kind = 'positive'
    else:
        word_kind = 'negative'
    return score, word_kind

def count_word_occurrences(file):
    (list1, list2, list3, list4, list5) = _getPositive_n_Negative_Words(file)
    dict1 = Counter(list1)
    dict2 = Counter(list2)
    dict3 = Counter(list3)
    dict4 = Counter(list4)
    dict5 = Counter(list5)
    return (dict1, dict2, dict3 , dict4, dict5)

def average_score(file, word):
    (dict1, dict2, dict3, dict4, dict5) = count_word_occurrences(file)

    scores = []
    sum = 0

    score_dict_01 = dict1[word] * 0
    scores.append(score_dict_01)
    score_dict_02 = dict2[word] * 1
    scores.append(score_dict_02)
    score_dict_03 = dict3[word] * 2
    scores.append(score_dict_03)
    score_dict_04 = dict4[word] * 3
    scores.append(score_dict_04)
    score_dict_05 = dict5[word] * 4
    scores.append(score_dict_05)

    for ele in range(0, len(scores)):
        sum = sum + scores[ele]

    return sum / len(scores)

def findHighes_n_Lowest(file):
    print("In processingg...")

def sentiment_program():
    file = str(input("Learning data file name:"))
    print("what would you like to do?")
    print("1. Get the score of a word")
    print('2. Get the average score of words in a file')
    print('3. Find the highest / lowest scoring wors in a file')
    print('4. Sort the words in a file into positive.txt and negative.txt')
    print('5. Exit program')
    print('Enter a number 1 - 5:')
    task = str(input())

    if task == '1':
        print('Which word?')
        word = str(input())
        score, word_kind = getScore(word, file)
        print("score = ",score)
        print(word, "is ", word_kind )
    if task == '2':
        file_name = str(input("file name?"))

    if task == '3':
        file_name = str(input("file name?"))

def main():
    sentiment_program()
main()


