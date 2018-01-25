# coding=utf-8
from flask import Flask

app = Flask(__name__)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = []

with open('words.txt', 'r') as words_fh:
    for word in words_fh:
        words.append(word.strip())

words_set = set(words)

words_set_neighbors = gen_neighbors(words)


@app.route('/<input_word>', methods=['GET'])
def serve(input_word):
    print('input_word', input_word)
    outputs = []

    if input_word not in words_set_neighbors:
        outputs = gen_words(input_word)
    else:
        outputs = words_set_neighbors[input_word]

    outputs.sort()
    return '<br>'.join(outputs)


def gen_words(input_word):
    potential_words = []

    print('starting')

    for i, letter in enumerate(input_word):
        if i == 0:
            # prepend
            for l in letters:
                potential_word = l + input_word
                if potential_word in words_set and potential_word != input_word:
                    potential_words.append(potential_word)

        # change
        for l in letters:
            potential_word = input_word[0:i] + l + input_word[i+1:]
            if potential_word in words_set and potential_word != input_word:
                potential_words.append(potential_word)

        # append
        for l in letters:
            potential_word = input_word[0:i] + letter + l + input_word[i+1:]
            if potential_word in words_set and potential_word != input_word:
                potential_words.append(potential_word)

    return potential_words

def gen_neighbors(words):
    output_map = {}

    for word in words:
        neighbor_list = gen_words(word)
        output_map[word] = neighbor_list

    return output_map
