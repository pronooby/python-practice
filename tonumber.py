import re

def extract_numbers_from_string(string):
    return [int(item) for item in re.findall(r'\b\d+\b', string)]

with open("sample.txt", "r") as file:
    string = file.read()
    numbers = extract_numbers_from_string(string)
    sum_of_numbers = sum(numbers)

with open("result.txt", "w") as file:
    file.write(str(sum_of_numbers))

#with chatGPT 정상작동확인됨.
