with open('input.txt', 'r', encoding='UTF8') as f:
    lines = f.readlines()

with open('output.txt', 'w', encoding='UTF8') as f:
    for line in lines:
        words = line.split()
        new_line = ' '.join(words[2:])
        f.write(new_line + '\n')

#with chatGPT 비정상작동확인됨. 
#encoding='UTF8'추가
#정상작동확인
