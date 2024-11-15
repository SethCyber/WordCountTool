import os
import time
from colorama import *
result = ""


def get_word_count(path: str) -> int:
    """Returns amount of spaces after characters of a given file"""
    lines = []
    with open(path, 'r') as file:
        for line in file:
            lines.append(line)
    all_words = ''
    for line in lines:
        all_words += line + '\n' + ' '
    words = 0
    while True:
        if all_words[len(all_words) - 1] == " ":
            all_words = all_words.rstrip()
        else:
            break
    for i in range(len(all_words)):
        if i == 0:
            pass
        else:
            if all_words[i-1] != " " and all_words[i] == " ":
                words += 1
    if all_words[-1] != " ":
        words += 1
        return words
    else:
        return words


def get_character_count(path: str) -> int:
    """Returns amount of characters of a given file"""
    lines = []
    with open(path, 'r') as file:
        for line in file:
            lines.append(line)
    all_words = ''
    for line in lines:
        all_words += line
    return len(all_words)


def get_paragraph_count(path: str) -> int:
    """Returns amount of blank lines of a given file"""
    count = 0
    lines = []
    with open(path, 'r') as file:
        for line in file:
            lines.append(line)
    for i in range(len(lines)):
        if lines[i] == '\n':
            count += 1
    return count+1


def get_line_count(path: str) -> int:
    """Returns amount of lines of a given file"""
    lines = []
    with open(path, 'r') as file:
       for line in file:
            lines.append(line)
    return len(lines)


def get_sentence_count(path: str) -> int:
    """Returns amount of periods, exclamation points, and question marks in a given file"""
    lines = []
    with open(path, 'r') as file:
        for line in file:
            lines.append(line)
    all_words = ''
    for line in lines:
        all_words += line
    count = 0
    for char in all_words:
        if char == '.':
            count += 1
        elif char == '?':
            count += 1
        elif char == '!':
            count += 1
        else:
            pass
    return count


def main():
    global result
    os.system("cls")
    print(Fore.WHITE+" _       __               __"+Fore.CYAN+" ______            __")
    print(Fore.WHITE+"| |     / /___  _________/ /"+Fore.CYAN+"/_  __/___  ____  / /")
    print(Fore.WHITE+"| | /| / / __ \\/ ___/ __  /"+Fore.CYAN+"  / / / __ \\/ __ \\/ /")
    print(Fore.WHITE+"| |/ |/ / /_/ / /  / /_/ /"+Fore.CYAN+"  / / / /_/ / /_/ / /")
    print(Fore.WHITE+"|__/|__/\\____/_/   \\__,_/"+Fore.CYAN+"  /_/  \\____/\\____/_/   ")
    print()
    print()
    print(result)
    print()
    print()
    directory = 'text.txt'#input('Directory: ')
    print(Fore.WHITE+'[1] Word Count '+Fore.CYAN+'   [2] Character Count  '+Fore.WHITE+'  [3] Paragraph Count')
    print()
    print(Fore.CYAN+'[4] Line Count '+Fore.WHITE+'   [5] Sentence Count   '+Fore.CYAN+'  [6] Live Diagnostic')
    print()
    print()
    option = int(input(Fore.WHITE+'Option Select: '+Fore.CYAN))
    if option == 1:
        result = (get_word_count(directory))
    if option == 2:
        result = (get_character_count(directory))
    if option == 3:
        result = (get_paragraph_count(directory))
    if option == 4:
        result = (get_line_count(directory))
    if option == 5:
        result = (get_sentence_count(directory))
    if option == 6:
        count6 = 0
        while True:
            count6 += 1
            word_count = get_word_count(directory)
            char_count = get_character_count(directory)
            para_count = get_paragraph_count(directory)
            line_count = get_line_count(directory)
            sentence_count = get_sentence_count(directory)
            print(Fore.WHITE+f'Words = [{word_count}]  '+Fore.CYAN+f'  Characters = [{char_count}]  '+Fore.WHITE+f'  Paragraphs =[{para_count}]  '+Fore.CYAN+f'  Lines = [{line_count}]  '+Fore.WHITE+f'  Sentences = [{sentence_count}]')
            time.sleep(1)

    main()
main()
