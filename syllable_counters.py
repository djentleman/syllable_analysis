from functools import reduce
import string
from nltk.corpus import cmudict
import pykakasi

kakasi = pykakasi.kakasi()
kakasi.setMode("H","a")
kakasi.setMode("K","a")
kakasi.setMode("J","a")
kakasi.setMode("s", True)
conv = kakasi.getConverter()


d = cmudict.dict()

def syllable_count_en(word):
    if word == '':
        return 0
    try:
        # try using nltk
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
    except KeyError:
        # if this fails, use the manual method from
        # https://stackoverflow.com/questions/46759492/syllable-count-in-python
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
        return count

def syllable_count_jp(word):
    # combinations of CVC, CV and V are syllables
    if word == '':
        return 0
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
        elif word[index] in vowels and word[index - 1] in vowels and \
                word[index] != word[index-1]:
            count += 1
    if count == 0:
        count += 1
    return count



def strip_punctuation(word):
    return ''.join([ch for ch in word if ch not in string.punctuation])

def syllable_count_sentence_en(sentence):
    return reduce(lambda x, y: x + y, map(lambda x: syllable_count_en(strip_punctuation(x)), sentence.split(' ')))

def syllable_count_sentence_jp(sentence):
    sentence = conv.do(sentence)
    return reduce(lambda x, y: x + y, map(lambda x: syllable_count_jp(strip_punctuation(x)), sentence.split(' ')))

