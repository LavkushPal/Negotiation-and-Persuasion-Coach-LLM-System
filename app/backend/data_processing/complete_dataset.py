
from sklearn.model_selection import train_test_split
import json
import random



dataset=[]

with open('training_data_casino.jsonl','r') as file:
    for line in file:
        dataset.append(json.loads(line))

with open('training_data_pfg.jsonl','r') as file:
    for line in file:
        dataset.append(json.loads(line))

with open('training_data_cmy.jsonl','r') as file:
    for line in file:
        dataset.append(json.loads(line))


random.shuffle(dataset)


# total-23461, --> training- 19,941, valdation- 2,992, test- 528 <-- approximate
train, val_test = train_test_split(dataset, test_size=0.15, random_state=42)
val, test = train_test_split(val_test, test_size=0.15, random_state=42)

print(len(dataset),len(train), len(val), len(test))



with open('negotiation_training.jsonl','w') as file:
    for record in train:
        file.write(json.dumps(record) + '\n')


with open('negotiation_validation.jsonl','w') as file:
    for record in val:
        file.write(json.dumps(record) + '\n')

with open('negotiation_test.jsonl','w') as file:
    for record in test:
        file.write(json.dumps(record) + '\n')
