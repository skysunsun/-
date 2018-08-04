def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')#字符串分割函数
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)#排序

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)#打印第一个字符

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)#打印最后一个字符

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)#分割之后排序

def print_first_and_last(sentence):
    """Prints the first and last words of the sorted words."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
