import math

stop_words = []
stop_word_file_path = input("Stop word file path: ")

with open(stop_word_file_path, 'r') as file:
    for line in file:
        stop_word = line.strip()
        stop_words.append(stop_word)


Vocab_size = 0
Vocabulary = set()
data = set()


def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:

            words = line.split()
            processed_line = ""

            for word in words:
                word = word.lower()

                if word not in stop_words:
                    Vocabulary.add(word)
                    processed_line += word + " "

            data.add(processed_line)


def prob_func(w, d):
    word_in_line = 0

    for i in d:
        if i == w:
            word_in_line += 1

    prob = (word_in_line + 1) / (len(d) + Vocab_size)

    return prob


def similarity_score(d1, d2):
    similarity = 0

    for w in Vocabulary:

        prob_w_d1 = prob_func(w, d1)
        prob_w_d2 = prob_func(w, d2)

        similarity += (
            prob_w_d1 *
            math.log10(prob_w_d1 / prob_w_d2)
        )

    return similarity


def query_preprocessing(sample_query):
    processed = ""

    query_words = sample_query.split()

    for word in query_words:
        word = word.lower()

        if word not in stop_words:
            processed += word + " "

    return processed


# ---------------- MAIN PROGRAM ----------------

file_path = input("Enter the input file path : ").strip()
sample_query = input("Enter the query : ")

read_file(file_path)

Vocab_size = len(Vocabulary)

processed_query = query_preprocessing(sample_query)

similarity_dict = {}

d1 = processed_query

for d2 in data:
    similarity_dict[d2] = similarity_score(d1, d2)


similarity_tuple = []

for stat, score in similarity_dict.items():
    similarity_tuple.append((stat, score))


most_similar_stat_with_score = sorted(
    similarity_tuple,
    key=lambda x: x[1]
)


print("\nMost similar sentence is :")
print(most_similar_stat_with_score[0][0])

print("\nSimilarity score is :")
print(most_similar_stat_with_score[0][1])