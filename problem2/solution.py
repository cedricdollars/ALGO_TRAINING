# coding:utf-8


def evaluate_rank(runners):
    if len(runners) == 0:
        return "Empty list"
    speeds = list(map(lambda runner: runner["speed"], runners))
    speeds.sort(reverse=True)
    return speeds[:3]


def evaluate_wins(runners):
    pass
