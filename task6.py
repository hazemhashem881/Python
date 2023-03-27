def is_pangram(sentence):
    sentence = sentence.lower()
    alphabets = set('abcdefghijklmnopqrstuvwxyz')
    return set(sentence)>= alphabets

sentence1 = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence1))    