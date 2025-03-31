with open('data.txt', 'w') as file:
    file.write("Here you can find activities to practise your reading skills. \n")

with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

with open('data.txt', 'a') as file:
    file.write("Reading will help you to improve"
               " your understanding of the language and build your vocabulary. \n")

with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

def process_line(line):
    print(line.strip())

with open('data.txt', 'r') as file:
    for line in file:
        process_line(line)

with open('data.txt', 'rb') as first_file:
    file_to_copy = first_file.read()

with open('copy_data.txt', 'wb') as second_file:
    second_file.write(file_to_copy)
