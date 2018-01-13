def viterbi(obs, states, start_p, trans_p, obs_p):
    V = [{}]

    for st in states:
        V[0][st] = {"prob": start_p[st] * obs_p[st][obs[0]], "prev": None}

    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})

        for st in states:
            max_tr_prob = max(V[t - 1][prev_st]["prob"] * trans_p[prev_st][st] for prev_st in states)

            for prev_st in states:
                if V[t - 1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * obs_p[st][obs[t]]
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break

    for line in dptable(V):
        print(line)
    opt = []

    # The highest probability
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None

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
    print('The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob)


def dptable(V):
    # Print a table of steps from dictionary
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)


input = "god bless christmas"
obs = input.lower().split(" ")
states = ('A', 'N', 'P', 'S', 'V')
start_p = {'A': 1/15, 'N': 1/15, 'P': 3/15, 'S':4/15, 'V': 6/15}
trans_p = {
    'A': {
        'A': 0,
        'N': 0.5882352941,
        'P': 0.05882352941,
        'S': 0.3529411765,
        'V': 0},
    'N': {
        'A': 0.1538461538,
        'N': 0.1923076923,
        'P': 0.07692307692,
        'S': 0.4615384615,
        'V': 0.1153846154},
    'P': {
        'A': 0.1538461538,
        'N': 0,
        'P': 0,
        'S': 0.3846153846,
        'V': 0.3846153846},
    'S': {
        'A': 0.1818181818,
        'N': 0.5227272727,
        'P': 0.04545454545,
        'S': 0.25,
        'V': 0},
    'V': {
        'A': 0.08333333333,
        'N': 0,
        'P': 0.5833333333,
        'S': 0.3333333333,
        'V': 0}}

obs_p = {
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
        if not ob in obs_p[state]:
            obs_p[state][ob] = 0

viterbi(obs, states, start_p, trans_p, obs_p)