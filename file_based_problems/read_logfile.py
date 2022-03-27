import re

import pytest

'''
  Problem: given a log file with a consistent format on each line
  '20 July 2018 21:35:48 Respawn took 0 seconds execution time 9 seconds processing time 2 seconds'
  Determine the average execution time and average processing time
  Extra the time stamp as well for extra credit
'''

def analyze_log_file(filename):
    # the tuple statement below reads all lines from a file into a list collection
    # similar to this while loop
    # with open(filename, "r") as ins:
    #     lines = []
    #     for line in ins:
    #         lines.append(line)
    lines = tuple(open(filename, 'r'))
    print(lines)
    avg_exec = 0
    avg_process = 0
    for line in lines:
        num_set = re.findall(r'\d+', line)
        time_stamp = re.findall(r'\b\d{2}/\d{2}/\d{4}\b|\b\d{2}:\d{2}\b:\d{2}\b', line)
        print(f'num_set = {num_set}')
        print(f'time_stamp = {time_stamp}')
        avg_process += int(num_set[len(num_set) - 1])
        avg_exec += int(num_set[len(num_set) - 2])
    avg_process = avg_process / len(lines)
    avg_exec = avg_exec / len(lines)
    print(f'avg_process was {avg_process}')
    print(f'avg_exec was {avg_exec}')


def test_analyze_log_file():
    analyze_log_file('./test_data/sample_log_file.txt')