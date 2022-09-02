text = input('Enter a sentence: ')

wdict = {}
words = text.split()

for word in words:
    if word in wdict:
        wdict[word] += 1
    else:
        wdict[word] = 1
        
# printing the dictionary
for key in wdict:
    print(key, wdict[key])