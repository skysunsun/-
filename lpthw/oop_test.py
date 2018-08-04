import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
        "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
        "class %%%(object) : \n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** params.",
        "class %%%(object) : \n\tdef ***(self, @@@)" :
        "class %%% has-a function *** that takes self and @@@ params.",
        "*** = %%%()":
        "Set *** to an instance of class %%%.",
        "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@. ",
        "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

#函数原型：random.sample(sequence, k)
#参数：sequence是一个list，k是一个整数
#返回值：返回一个list，该list由sequence中随机的k个元素组成，sequence不变
# do they want to drill phrases first

#函数原型：str.join(sequence)
#参数：sequence – 要连接元素的list
#返回值：返回通过str连接序列中元素后生成的字符串

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the word from the website
for word in urlopen(WORD_URL).readlines():#读取网页
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet,phrase):
    class_names = [w.capitalize() for w in#首写字母变大写函数
                   random.sample(WORDS, snippet.count("%%%"))]#统计次数
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(','.join(
                            random.sample(WORDS, param_count)))
    for sentence in snippet, phrase:
        result = sentence[:]

          # fake class class_names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        #fake other name
        for word in other_names:
            result = result.replace("***", word, 1)
        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

     #keep going until they hit ctrl_d
try:
    while True:
        snippets = list(PHRASES.keys())#提取值
        random.shuffle(snippets)#shuffle打乱顺序

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

                print(question)

                input(">")
                print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
