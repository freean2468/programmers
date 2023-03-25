def solution(elements):
    answer = set()
    for i, _ in enumerate(elements):
        fw = []
        bw = []
        for t in range(len(elements)):
            fw.append(elements[(t + i) % len(elements)])
            bw.append(elements[-((t + i) % len(elements))])
            answer.add(sum(fw))
            answer.add(sum(bw))
    return len(answer)