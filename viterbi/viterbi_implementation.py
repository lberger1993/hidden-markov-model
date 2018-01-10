# need to add start prob.
def start_probability():
    # need to calculate for verb or noun
    print("need to start from the verb")


def viterbi(obs, states, start_p, trans_p, observational_probability):
    V = [{}]
    print(states)
    for st in states:
        print(observational_probability[st])
        print(obs[0])

        V[0][st] = {"prob": start_p[st] * observational_probability[st][obs[0]], "prev": None}
      # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = max(V[t-1][prev_st]["prob"]*trans_p[prev_st][st] for prev_st in states)
            for prev_st in states:
                if V[t-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * observational_probability[st][obs[t]]
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break
    for line in dptable(V):
        print (line)
    opt = []
    # The highest probability
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None

     # probaility from previous to all
     # Get most probable state and its backtrack
    for st, data in V[-1].items():
         if data["prob"] == max_prob:
             opt.append(st)
             previous = st
             break
     # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
         opt.insert(0, V[t + 1][previous]["prev"])
         previous = V[t + 1][previous]["prev"]
    print ('The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob)

def dptable(V):
     # Print a table of steps from dictionary
     yield " ".join(("%12d" % i) for i in range(len(V)))
     for state in V[0]:
         yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)

obs = ['I', 'wish', 'you', 'a', 'merry', 'Christmas']
    # "Happy Christmas to you and all your family"
    # "Let this Christmas time be full of joy and love",
    # "May beautiful moments and happy memories surround you with joy this Christmas",
    # "Have a merry Christmas full of cheer and happiness"
    # "Christmas Greetings",
    # "The best of joy, the best of cheer for Christmas",
    # "May God bless you this Christmas",
    # "Have a merry Christmas",
    # "I wish you a Christmas overflowing with love and laughter",
    # "May all your joyful Christmas dreams come true.  I love you",
    # "My love, you bring me so much joy. I wish you the best Christmas ever this year!"
    # "My one Christmas wish is always to be with you",
    # "I wish you great Christmas time full of love and happiness",
    # "My best wishes for Christmas"

states = ('P', 'V', 'N', 'A', 'S')
start_p = {'P': 1, 'V': 0, 'N':0, 'A':0, 'S':0}
trans_p = {
    'P': {'P': 0.7, 'V': .462, 'N':0, 'A': 0.08, 'S':0.46},
    'V': {'P': 0.39, 'V': 0.0, 'N': 0, 'A': 0.11, 'S': 0.44},
    'N': {'P': 0.08, 'V': 0.19, 'N': 0.19, 'A': 0.12, 'S': 0.42},
    'A': {'P': 0, 'V': 0, 'N': 0.63, 'A': 0, 'S': 0.38},
    'S': {'P': 0.07, 'V': 0.02, 'N': 0.51, 'A': 0.21, 'S': 0.19},
}
observational_probability = {
        'P': {
            'I': 5/14,
            'you': 9/14
        },
        'V': {
            'wish': 4/18,
            'let': 1/18,
            'be': 2/18,
            'may': 3/18,
            'surround': 4/18,
            'have': 2/18,
            'come': 1/18,
            'love': 1/18,
            'bring': 1/18,
            'is': 1/18,
            'bless': 1/18,
        },
        'N':{
            "Christmas":15/39,
            "family":1/39,
            "time":2/39,
            "joy":4/39,
            "love":4/39,
            'moments':1/39,
            "memories":1/39,
            "cheer":2/39,
            "happiness":2/39,
            "greetings":1/39,
            "god":1/39,
            "laughter":1/39,
            "dreams":1/39,
            "year":1/39,
            "wish":1/39,
            "wishes":1/39,

        },
        'A':{
            "merry":3/16,
            "happy":2/16,
            "full":3/16,
            "beautiful":1/16,
            "best":4/16,
            "overflowing":1/16,
            "joyful":1/16,
            "great":1/16
        },
        'S':{
            "a":4/43,
            "to":2/43,
            "and":6/43,
            "all":2/43,
            "your":2/43,
            "this":4/43,
            "of":5/43,
            "with":3/43,
            "the":3/43,
            "for":2/43,
            "true":1/43,
            "my":3/43,
            "me":1/43,
            "so":1/43,
            "much":1/43,
            "ever":1/43,
            "one":1/43,
            "always":1/43
        },
}

viterbi(obs,states,start_p,trans_p,observational_probability)