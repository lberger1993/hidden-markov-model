# need to add start prob.
def start_probability():
    # need to calculate for verb or noun
    print("need to start from the verb")


def viterbi(obs, states, start_p, trans_p, observational_probability):
    V = [{}]

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

input = "I wish you merry christmas"

obs = input.lower().split(" ")
states = ('P', 'V', 'N', 'A', 'S')
start_p = {'A': 0.2, 'N': 0.2, 'P': 0.2, 'S': 0.2, 'V': 0.2}
trans_p = {
    'P': {'P': 0.7, 'V': .462, 'N':0, 'A': 0.08, 'S':0.46},
    'V': {'P': 0.39, 'V': 0.0, 'N': 0, 'A': 0.11, 'S': 0.44},
    'N': {'P': 0.08, 'V': 0.19, 'N': 0.19, 'A': 0.12, 'S': 0.42},
    'A': {'P': 0, 'V': 0, 'N': 0.63, 'A': 0, 'S': 0.38},
    'S': {'P': 0.07, 'V': 0.02, 'N': 0.51, 'A': 0.21, 'S': 0.19},
}

observational_probability = {
    'A': {'merry': 0.1764705882, 'happy': 0.1176470588, 'full': 0.1764705882, 'beautiful': 0.05882352941,
          'best': 0.2352941176, 'overflowing': 0.05882352941, 'joyful': 0.05882352941, 'true': 0.05882352941,
          'great': 0.05882352941},
    'N': {'christmas': 0.3846153846, 'family': 0.02564102564, 'joy': 0.1025641026, 'love': 0.1025641026,
          'moments': 0.02564102564, 'memories': 0.02564102564, 'cheer': 0.05128205128, 'happiness': 0.05128205128,
          'greetings': 0.02564102564, 'god': 0.02564102564, 'laughter': 0.02564102564, 'dreams': 0.02564102564,
          'year': 0.02564102564, 'wish': 0.02564102564, 'time': 0.05128205128, 'wishes': 0.02564102564},
    'P': {'i': 0.3333333333, 'you': 0.6666666667},
    'S': {'a': 0.09090909091, 'to': 0.04545454545, 'and': 0.1363636364, 'all': 0.04545454545, 'your': 0.04545454545,
          'this': 0.09090909091, 'be': 0.04545454545, 'of': 0.1136363636, 'may': 0.06818181818, 'with': 0.06818181818,
          'for': 0.04545454545, 'my': 0.06818181818, 'me': 0.02272727273, 'so': 0.02272727273, 'much': 0.02272727273,
          'ever': 0.02272727273, 'only': 0, 'is': 0.02272727273, 'always': 0.02272727273, 'the': 0.04545454545,
          'one': 0.02272727273},
    'V': {'wish': 0.3333333333, 'let': 0.08333333333, 'surround': 0.08333333333, 'have': 0.1666666667,
          'bless': 0.08333333333, 'come': 0.08333333333, 'love': 0.08333333333, 'bring': 0.08333333333}}



for ob in obs:
    for state in states:
        if not ob in observational_probability[state]:
            observational_probability[state][ob] = 0

viterbi(obs,states,start_p,trans_p,observational_probability)