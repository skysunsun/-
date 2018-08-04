import sys
script, encoding, error = sys.argv
#strict 编码解码错误默认解决方案

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()#删除开头结尾空格
    #strip(xxx)删除开头和结尾位于xxxx序列的空格
    raw_bytes = next_lang.encode(encoding, errors = errors)#编码
    cooked_string = raw_bytes.decode(encoding, errors = errors)#解码

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)
