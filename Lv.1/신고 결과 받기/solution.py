# https://school.programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    reported = dict.fromkeys(id_list)

    for key, value in reported.items():
        reported[key] = {'count': 0, 'by': set()}

    for s in set(report):
        split = s.split(' ')
        reported[split[1]]['count'] += 1
        reported[split[1]]['by'].add(split[0])

    answer = [0 for v in range(len(id_list))]

    for i, v in enumerate(id_list):
        if reported[v]['count'] >= k:
            for reporter in reported[v]['by']:
                answer[id_list.index(reporter)] += 1

    return answer
