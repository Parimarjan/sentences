import nltk.data

digraphs = ['ab', 'bc', 'as', 'ss', 'sw', 'wo', 'or', 'rd', 'mu', 'us', 'st',
        'ta', 'an', 'ng', 'le', 'et', 'tm', 'me', 'ei', 'in']

file_name = 'sherlock.txt'
fp = open(file_name)
data = fp.read()
sentences = data.split('.')

# find sentences that maximize the use of digraphs

def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

def count_digraphs(sentence, digraphs_list):
    '''
    returns number of digraphs from digraph_list in the sentence
    '''
    char_list = list(sentence)
    bigrams = find_ngrams(char_list, 2)
    # print(bigrams)
    bigrams = [b[0] + b[1] for b in bigrams]
    count = 0
    for bigram in bigrams:
        if bigram in digraphs_list:
            count += 1
    
    return count

print('******************************')
results = []
for sentence in sentences:    
    num = count_digraphs(sentence, digraphs)
    results.append((num, sentence))

results.sort(key=lambda x: x[0], reverse=False)

for i, result in enumerate(results):
    if len(result[1].split(' ')) > 20:
        continue
    if result[0] <= 10:
        continue
    print('{} : {}'.format(result[1], result[0]))
