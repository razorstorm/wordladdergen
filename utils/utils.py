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


def gen_neighbors(words_to_process):
    output_map = {}

    for word in words_to_process:
        neighbor_list = gen_words(word)
        output_map[word] = neighbor_list

    return output_map
