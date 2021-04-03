import random

text_data = input('Write your text: ').split()
text_data_index = []
for i in range(len(text_data)):
    text_data_index.append(text_data[i] + '_' + str(i+1))

shuffled_data_index = []
while text_data_index != []:
    word = random.choice(text_data_index)
    shuffled_data_index.append(word)
    text_data_index.remove(word)

secret_indexes = []
for i in range(len(shuffled_data_index)):
    index = shuffled_data_index[i].split('_')[-1]  # index in str
    index = int(index)  # index in digit
    secret_indexes.append(index)
    shuffled_data_index[i] = '_'.join(shuffled_data_index[i].split('_')[:-1])

print(shuffled_data_index)
print(secret_indexes)

answer = ''
m = 1
z = 1
o = len(secret_indexes)
for q in secret_indexes:
    for b in range(m):
        for y in shuffled_data_index:
            if q == z:
                answer += str(y)
                answer += ' '
                z += 1
            else:
                m += 1
            m = 1
print(answer, z)

