import string
dic_path = '/home/anton/PycharmProjects/untitled/en-ru.txt'
text_path = '/home/anton/PycharmProjects/untitled/input.txt'
with open(dic_path) as f:
    text = f.readlines()
dictionary = {}
for i in range(len(text)):
    dictionary[text[i].split()[0]] = text[i].split()[2]

out = ''
eng_word = []
rus_word = []
with open(text_path) as f:
    for line in f:
        out += line
        sub_line = ''
        line = line.split()
        for x in line:
            for i in x:
                if i in string.punctuation:
                    x = x [:-1]
            if x.lower() in dictionary:
                x = dictionary[x.lower()]
            sub_line += (x+' ')
        out += (sub_line+'\n')

with open('/home/anton/PycharmProjects/untitled/output.txt', 'w') as f:
    f.write(out)