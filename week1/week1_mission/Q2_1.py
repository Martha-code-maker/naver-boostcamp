sentence = "way a is there will a is there where"

def reverse_sentence(sentence):
    reverse_sentence_list = sentence.split(' ')
    reverse_sentence_list.reverse()
    return ' '.join(reverse_sentence_list)
    
print(reverse_sentence(sentence))
 
