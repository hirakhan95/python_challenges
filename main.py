from word_count import frequency_more_than_num
from urllib.request import urlopen


def cleanhtml(raw_html):
    import re
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


url = "https://en.wikipedia.org/wiki/Biology"
with urlopen(url) as resp:
    file_content = cleanhtml(str(resp.read()))

    word_lst = file_content.split(' ')

    clean_word_list = []
    for i in word_lst:
        temp = i.lower()
        if len(temp) > 3 and temp.isalpha():
            clean_word_list.append(temp)

    print(frequency_more_than_num(clean_word_list, 20))
