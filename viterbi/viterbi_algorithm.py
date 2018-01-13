from string import punctuation


def create_observation_object():
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * obs_p[st][obs[0]], "prev": None}

    return V


def find_max_transitional_probability(V_object):
    for t in range(1, len(obs)):
        V_object.append({})
        for st in states:
            max_tr_prob = max(V_object[t - 1][prev_st]["prob"] * trans_p[prev_st][st] for prev_st in states)
            for prev_st in states:
                if V_object[t - 1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * obs_p[st][obs[t]]
                    V_object[t][st] = {"prob": max_prob, "prev": prev_st}
                    break


def find_most_probable_state(V,max):
    """ Get most probable state and its backtrack"""
    opt = []
    previous = None
    for st, data in V[-1].items():
        if data["prob"] == max:
            opt.append(st)
            previous = st
            break
    return opt, previous


def backtrack_until_first_observation(V,opt_array, previous):
    for t in range(len(V) - 2, -1, -1):
        opt_array.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]



def viterbi(obs, states, start_p, trans_p, obs_p):
    # returns the observation object
    V = create_observation_object()
    dynamic_programming_table(V)
    find_max_transitional_probability(V)
    # The highest probability
    max_prob = max(value["prob"] for value in V[-1].values())
    opt, previous = find_most_probable_state(V, max_prob)
    backtrack_until_first_observation(V, opt, previous)
    # Follow the backtrack till the first observation
    print(' & %s' % max_prob + ' & ' + ''.join(opt) + ' \\ \hline')


def dynamic_programming_table(V):
    # Print a table of steps from dictionary
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)


states = ('A', 'N', 'P', 'S', 'V')
start_p = {'A': 1/15, 'N': 1/15, 'P': 3/15, 'S':4/15, 'V': 6/15}
trans_p = {
    'A': {
        'A': 0,
        'N': 0.5882352941,
        'P': 0.05882352941,
        'S': 0.3529411765,
        'V': 0

    },
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

obs_p = {'A': {'merry': 0.1875, 'happy': 0.125, 'full': 0.1875, 'beautiful': 0.0625, 'best': 0.25, 'overflowing': 0.0625, 'joyful': 0.0625, 'true': 0.0, 'great': 0.0625}, 'N': {'christmas': 0.3611111111111111, 'family': 0.027777777777777776, 'joy': 0.05555555555555555, 'love': 0.1111111111111111, 'moments': 0.027777777777777776, 'memories': 0.027777777777777776, 'cheer': 0.05555555555555555, 'happiness': 0.027777777777777776, 'greetings': 0.027777777777777776, 'god': 0.027777777777777776, 'laughter': 0.0, 'dreams': 0.027777777777777776, 'year': 0.0, 'wish': 0.1388888888888889, 'time': 0.05555555555555555, 'wishes': 0.027777777777777776}, 'P': {'i': 0.35714285714285715, 'you': 0.6428571428571429}, 'S': {'a': 0.08333333333333333, 'to': 0.041666666666666664, 'and': 0.125, 'all': 0.041666666666666664, 'your': 0.041666666666666664, 'this': 0.08333333333333333, 'be': 0.041666666666666664, 'of': 0.10416666666666667, 'may': 0.0625, 'with': 0.0625, 'for': 0.041666666666666664, 'my': 0.0625, 'me': 0.020833333333333332, 'so': 0.020833333333333332, 'much': 0.020833333333333332, 'ever': 0.020833333333333332, 'only': 0.0, 'is': 0.020833333333333332, 'always': 0.020833333333333332, 'the': 0.0625, 'one': 0.020833333333333332}, 'V': {'wish': 0.3125, 'let': 0.0625, 'surround': 0.0625, 'have': 0.125, 'bless': 0.0625, 'come': 0.0625, 'love': 0.25, 'bring': 0.0625}}

def remove_empty(obs):
    for ob in obs:
        for state in states:
            if not ob in obs_p[state]:
                obs_p[state][ob] = 0

with open("observations.txt") as f:
    content = f.readlines()
    full_content = []
    for line in content:
        line = line.replace('\n', '').lower()

        obs = line.split(' ')
        remove_empty(obs)
        viterbi(obs, states, start_p, trans_p, obs_p)
        final_string = str(obs) + " & 0 &  0.209\\ \hline"