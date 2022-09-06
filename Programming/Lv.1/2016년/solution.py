# https://school.programmers.co.kr/learn/courses/30/lessons/12901?language=python3
import datetime

def solution(a, b):
    return datetime.datetime(2016, a, b).strftime("%a").upper()