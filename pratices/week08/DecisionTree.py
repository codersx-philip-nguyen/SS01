import numpy as np

def count_freq(data_set):
    freq_list = {}
    for item in data_set:
        if item in freq_list:
            freq_list[item] += 1
        else:
            freq_list[item] = 1
    return freq_list

def entropy(freq):
    len_of_freq_list = 0
    entropy_list = []
    for key in freq:
        len_of_freq_list += freq[key]

    for key in freq:
        # cal prob of each key in the sample
        probability_i = freq[key] / len_of_freq_list
        #calculate H(s) = -sum(pi*log_pi)
        if probability_i == 1:
            H_i = 0
        else:
            H_i = -probability_i*np.log2(probability_i)
        entropy_list.append(H_i)

    return entropy_list

def H_sample(_entropy_list):
    return np.sum(_entropy_list)

if __name__ == "__main__":
    freq = count_freq([1,1,1,1,1,1,2,2])
    print(freq)
    print(H_sample(entropy(freq)))
