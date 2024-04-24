def calculate_frequency(text):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    count = [0] * 26

    for t in text:
        if t in alpha:
            x = ord(t) - 97
            count[x] += 1

    total_letters = sum(count)
    frequency_percentage = [(count[i] / total_letters) * 100 for i in range(26)]

    return frequency_percentage

file_names = ['file1.txt', 'file2.txt', 'file3.txt']
alpha = 'abcdefghijklmnopqrstuvwxyz'

for file_name in file_names:
    with open(file_name, 'r') as file:
        text = file.read()
    
    frequency_percentage = calculate_frequency(text)

    # print(f'FREQUENCY OF LETTERS IN {file_name.upper()}:')
    print(f'FREQUENCY OF LETTERS IN {file_name}:')
    for i in range(13):
        print(f'{alpha[i]} - {frequency_percentage[i]:.2f}%\t{alpha[i+13]} - {frequency_percentage[i+13]:.2f}%')



