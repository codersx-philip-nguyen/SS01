# Read all data from data file
# include username, booktitle, rating
# input: file contain data
# output: list of tuple ((str)username, (str)booktitle, (int)rating) contain all data
def getData(filepath):
    file = open(filepath, 'r')
    raw_data = file.readlines()
    data_list = []

    assert (len(data_list)%3 == 0)

    # remove the newline sign, spare blankspaces
    for i in range(len(raw_data)):
        e = raw_data[i].rstrip('\n').strip(" ")
        if (i+1) % 3 == 0:
            e = int(e)
        data_list.append(e)

    raw_data_list = []
    i = 0
    #turn into list of tuple ((str)username, (str)booktitle, (int)rating) contain all data
    while i < len(raw_data):
        t = (data_list[i], data_list[i+1], data_list[i+2])
        i += 3
        raw_data_list.append(t)

    return(raw_data_list)

# Get all the booktitle from the data - no duplication
# Turn to list
# input: list of tuple (username, booktitle, rating) contain all data
# output: list of all booktitle
def splitListTuplpleBy(tuple_list,i):
    s = set()
    for e in tuple_list:
        s.add(e[i])

    lst = list(s)
    return lst

def getBooktitle(raw_data_list):
    book_title_list = splitListTuplpleBy(raw_data_list, 1)
    return book_title_list

# Create dictionary of user - rating for each book
# e.g. 'Kalid' : [0,0,1,-3,3,0]
# input: (list of booktitle, list of tuple (username, booktitle, rating))
# output: dictionary of user - rating for each book
def getUserRating(book_title_list, raw_data_list):
    # create dictionary of book_title_list assign each book with an index
    book_title_dict = {}
    for i in range(len(book_title_list)):
        book_title_dict[book_title_list[i]] = i

    # get all username from raw_data_list
    username_list = splitListTuplpleBy(raw_data_list, 0)

    # create the dictionary of empty data
    user_rating_dict = {}
    for i in range(len(username_list)):
        user_rating_dict[username_list[i]] = [0]*len(book_title_list)


    # fill the rating number into the dict
    for i in range(len(raw_data_list)):
        user_rating_dict[raw_data_list[i][0]][book_title_dict[raw_data_list[i][1]]] += raw_data_list[i][2]

    return user_rating_dict

# Averages

# List of tuple of all (books, average rating)
# sort by average rating
# input: (list of all booktitle, dictionary of user - rating for each book)
# output: list of tuple of all (books, average rating)
def average_service(book_title_list, user_rating_dict):
    # create dictionary of book_title_list assign each book with an index
    book_title_dict = {}
    for i in range(len(book_title_list)):
        book_title_dict[i] = book_title_list[i]

    # create the dictionary of empty data
    average_dict_temp = {}
    average_dict = {}
    for i in range(len(book_title_list)):
        average_dict_temp[book_title_list[i]] = []
        average_dict[book_title_list[i]] = 0

    # fill data into average_dict_temp
    for e in user_rating_dict:
        array = user_rating_dict[e]
        for i in range(len(array)):
            if array[i] != 0:
                average_dict_temp[book_title_dict[i]].append(array[i])

    # get the real average_dict
    for e in average_dict_temp:
        if len(average_dict_temp[e]) == 0:
            average_dict[e] = float(0)
        else:
            average_dict[e] = sum(average_dict_temp[e]) / len(average_dict_temp[e])

    average_tuple_list = [(k, v) for k, v in average_dict.items()]

    average_tuple_list.sort(key = lambda x:x[1], reverse=True)

    return average_tuple_list

# Recommendations
# The user is in the list then
# - Calculate similarity. need "dictionary of user - rating"
# input: ((str)user, dictionary of user - rating for each book)
# output: dict of 4 most similar users in the type of list of user - rating for each book
def dotproduct(K,L):
    if len(K)==len(L) and len(K)!=0:
        return sum([K[n]*L[n] for n in range(len(K))])
    else:
        return 0

def similarity_calculate(given_user, user_rating_dict):
    #initial calculatio_dict
    calculation_dict = {}
    for username in user_rating_dict:
        calculation_dict[username] = 0

    for username in user_rating_dict:
        calculation_dict[username] = dotproduct(user_rating_dict[given_user], user_rating_dict[username])

    slice_index = len(user_rating_dict)
    if len(user_rating_dict) > 4:
        slice_index = 4
    calculation_list = list(sorted(calculation_dict.items(), key=lambda item: item[1], reverse=True))[:slice_index]


    calculate_dict = {}
    for e in calculation_list:
        if e[0] == given_user:
            continue
        calculate_dict[e[0]] = user_rating_dict[e[0]]
    return calculate_dict

# - Calculate the average of rating for each book by first 3 person not include the given user
# call the Averages function (list of all book title, dictionary of 4 user - their rating for each book)
# input (list of all book title, dict of 4 user - their rating for each book)
# output (list of tuple of all (books, average rating)
def recommend_service(book_title_list, calculate_dict):
    averages_tuple_list = average_service(book_title_list, calculate_dict)
    return averages_tuple_list

# Create the interface (which will run first from main)
# require input("User?")

# The user is not in the data -> call Averages
# input (raw_data_list, book_title_list, user_rating_dict)
# output boolean...
def recommendationSystem(raw_data_list, book_title_list, user_rating_dict):
    print("""Welcome to the CSC110 Book Recommender. Type the word in the 
            left column to do the action on the right
            recommend: recommend books for a particular user
            averages: output the average ratings of all books in the system
            quit: exit the program
            next task? """)

    require = str(input())
    if require == "recommend":
        given_user = str(input("User? "))
        if given_user not in user_rating_dict:
            print(average_service(book_title_list, user_rating_dict))
            return False
        else:
            calculate_dict = similarity_calculate(given_user, user_rating_dict)
            print(recommend_service(book_title_list, calculate_dict))
            return False
    if require == "averages":
        print(average_service(book_title_list, user_rating_dict))
        return False
    if require == "quit":
        return True


def main():
    raw_data_list = getData("ratings-small.txt")
    # list of tuple (str,str,int)
    book_title_list = getBooktitle(raw_data_list) # list [string]
    user_rating_dict = getUserRating(book_title_list,raw_data_list) # dictionary 'user' : [int]

    exit_code = False

    while(not exit_code):
        exit_code = recommendationSystem(raw_data_list, book_title_list, user_rating_dict)

    return

main()




