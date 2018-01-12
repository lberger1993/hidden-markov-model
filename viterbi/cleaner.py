
def classify_words(part_of_speech_group):
    total = 0
    for line in full_content:
        for word in line:
            if word in part_of_speech_group:
                total = total + 1
                part_of_speech_group[word] = part_of_speech_group[word]+1
    for key in part_of_speech_group:
        part_of_speech_group[key] = part_of_speech_group[key]/total
    return part_of_speech_group

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

verbs = {'wish': 0, 'let': 0, 'surround': 0, 'have': 0,
          'bless': 0, 'come': 0, 'love': 0, 'bring': 0}

stop_words =  {'a': 0, 'to': 0, 'and': 0, 'all': 0, 'your': 0,
      'this': 0, 'be': 0, 'of': 0, 'may': 0, 'with': 0,
      'for': 0, 'my': 0, 'me': 0, 'so': 0, 'much': 0,
      'ever': 0, 'only': 0, 'is': 0, 'always': 0, 'the': 0,
      'one': 0}

pronouns = {'i': 0, 'you': 0}

obs_p = {'A': classify_words(adjectives),
         'N': classify_words(nouns),
         'P': classify_words(pronouns),
         'S': classify_words(stop_words),
         'V': classify_words(verbs),
         }

print(obs_p)

