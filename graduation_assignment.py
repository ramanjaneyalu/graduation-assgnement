import itertools


def graduation_ceremony(number_of_days):
    all_ways = [''.join(x) for x in itertools.product('AP', repeat=number_of_days)]

    present_ways = [x for x in all_ways if x.find('AAAA') == -1]

    number_of_ways = len(present_ways)
    prob_miss_grad = 0
    for day in present_ways:
        if day[-1] == 'A':
            prob_miss_grad += 1
    return f"{prob_miss_grad}/{number_of_ways}"


if __name__ == '__main__':
    assert graduation_ceremony(5) == "14/29"
    assert graduation_ceremony(10) == "372/773"
