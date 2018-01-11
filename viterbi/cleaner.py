
def classify_words(adjectives):
    total = 0
    for line in full_content:
        for word in line:
            if word in adjectives:
                total = total + 1
                adjectives[word] = adjectives[word]+1
    for key in adjectives:
        adjectives[key] = adjectives[key]/total
    return adjectives

with open("observations.txt") as f:
    content = f.readlines()
    full_content = []
    for line in content:
        line = line.replace('\n', '').lower()
        full_content.append(line.split(' '))

adjectives = {'merry':0,
              'happy':0,
              'full':0,
              'beautiful':0,
              'best':0,
              'overflowing':0,
              'joyful':0,
              'true':0,
              'great':0 }

nouns = {'christmas': 0, 'family': 0, 'joy': 0, 'love': 0,
          'moments': 0, 'memories': 0, 'cheer': 0, 'happiness': 0,
          'greetings': 0, 'god': 0, 'laughter': 0, 'dreams': 0,
          'year': 0, 'wish': 0, 'time': 0, 'wishes': 0}


classify_words(adjectives)
print(classify_words(nouns))


