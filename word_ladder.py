# coding=utf-8
from flask import Flask

app = Flask(__name__)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


@app.route('/<input_word>', methods=['GET'])
def serve(input_word):
    print('input_word', input_word)
    return '<br>'.join(gen_words(input_word))


def gen_words(input_word):
    words = []
    potential_words = []

    print('starting')

    with open('words.txt', 'r') as words_fh:
        for word in words_fh:
            words.append(word.strip())

    words_set = set(words)

    for i, letter in enumerate(input_word):
        print(potential_words)
        if i == 0:
            # prepend
            for l in letters:
                potential_word = l + input_word
                if potential_word in words_set:
                    potential_words.append(potential_word)

        # change
        for l in letters:
            potential_word = input_word[0:i] + l + input_word[i+1:]
            # print potential_word
            if potential_word in words_set:
                potential_words.append(potential_word)

        # append
        for l in letters:
            potential_word = input_word[0:i] + letter + l + input_word[i+1:]
            # print potential_word
            if potential_word in words_set:
                potential_words.append(potential_word)

    return potential_words

