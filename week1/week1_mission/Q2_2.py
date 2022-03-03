sentence = "way a is there will a is there where"

def reverse_sentence(sentence):
    return ' '.join(sentence.split(' '[::-1]))


print(reverse_sentence(sentence))
