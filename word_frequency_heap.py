# Stores word-related information gathered from the input file.
data = []
word_info = dict()  # word -> [total count, number of lines containing the word]
word = ""
file_path = input("Enter your file path : ")

# Read the file line by line and collect word frequencies.
def read_file(file_path):
    with open(file_path,'r') as file:
        line_number = 0
        for line in file:
            word = ""
            unique_words_in_line = set()
            line_number += 1
            for character in line:
                if not character.isalnum():
                    if word != "":
                        unique_words_in_line.add(word)
                        if word not in word_info:
                            word_info[word] = [1,0]
                        else:
                            word_info[word][0] += 1
                        word = ""
                else:
                    word += character.lower()
            if word != "":
                unique_words_in_line.add(word)
                if word not in word_info:
                    word_info[word] = [1,0]
                else:
                    word_info[word][0] += 1
            for current_word in unique_words_in_line:
                word_info[current_word][1] += 1
                
read_file(file_path)

word_list = list(word_info)    

# Restore the max-heap property starting from index i.
def heapify(i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n:
        left_word = word_list[left]
        largest_word = word_list[largest]
        if word_info[left_word][0] > word_info[largest_word][0]:
            largest = left
    if right < n:
        right_word = word_list[right]
        largest_word = word_list[largest]
        if word_info[right_word][0] > word_info[largest_word][0]:
            largest = right
    if largest != i:
        word_list[i], word_list[largest] = word_list[largest], word_list[i]
        heapify(largest, n)

# Convert the list of words into a max heap based on total frequency.
def build_heap(word_list):
    n = (len(word_list) // 2) - 1
    for k in range(n,-1,-1):
        heapify(k, len(word_list))

build_heap(word_list)

# Repeatedly remove the most frequent word from the heap.
def heap_sort(word_list, sorted_words):
    for i in range(len(word_list)):
        sorted_words.append(word_list[0])
        word_list[0] = word_list[-1]
        word_list.pop()
        if len(word_list) > 0:
            heapify(0, len(word_list))
    return sorted_words

sorted_words = []

answer = heap_sort(word_list, sorted_words)
for i in answer:
    print(f"Word : {i} , Total_Count : {word_info[i][0]} ,Line_Count : {word_info[i][1]}")
