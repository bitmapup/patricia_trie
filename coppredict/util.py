# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from ast import literal_eval
from pathlib import Path


def read_results(result_path):
    result_file = open(Path(result_path), 'r')
    sequences_raw = result_file.readlines()
    result_file.close()
    return sequences_raw


def parse_options(result_patterns):
    line = result_patterns[0]
    return literal_eval(line[0:len(line)-1])


def extract_patterns(result_path):
    sequences = []
    sequences_raw = convert_to_list(read_results(result_path))
    sequence_list = pattern_to_list(sequences_raw)

    for row in sequence_list:
        sequences.append(pd.Series([row[0], row[1], row[2]],
                                   index=["patterns", "supp", "%supp"]))

    result = pd.DataFrame(columns=['patterns', 'supp', "%supp"]).append(sequences, ignore_index=True)

    result['patterns'] = result.patterns.apply(lambda x: literal_eval(str(x)))
    return result


def get_labels(patterns):
    labels = []
    for i in range(1, get_max_pattern_len(patterns) + 1):
        labels.append("IS" + str(i))

    labels.append("supp")
    labels.append("%supp")
    return labels


def get_max_pattern_len(patterns):
    len_seq = []
    for s in patterns:
        len_seq.append(len(s))
    seq_len = np.array(len_seq)
    return max(seq_len)


def convert_to_list(result_patterns):
    patterns_list = []
    for line in result_patterns[1:]:
        patterns_list.append(literal_eval(line))
    return patterns_list


def pattern_to_list(list_patterns):
    """
    convert pattern format to list

    Parameters
    ----------
    list_patterns : list
        results patterns of sequential pattern mining


    Returns
    -------
    list
        results patterns mined in a list
    """
    result_pattern_list = []
    itemset = ''
    for row_pattern in list_patterns:
        pattern = []
        for ch in row_pattern[0]:
            if ch != '<' and ch != '>' and ch != ' ':
                itemset += ch

            if ch == '>':
                if ',' in itemset:
                    pattern.append(itemset.split(','))
                else:
                    pattern.append(itemset)
                itemset = ''
        result_pattern_list.append([pattern, row_pattern[1], row_pattern[2]])
    return result_pattern_list


def extract_patterns_old(result_path):
    sequences = []
    sequences_raw = read_results(result_path)[1:]

    for row in range(len(sequences_raw)):
        sequences.append(pd.Series(literal_eval(sequences_raw[row][0:len(sequences_raw[row])-1]),
                                   index=["patterns", "supp", "%supp"]))

    result = pd.DataFrame(columns=['patterns', 'supp', "%supp"]).append(sequences, ignore_index=True)
    result['patterns'] = result.patterns.apply(lambda x: literal_eval(str(x)))
    return result


def list_to_patterns(result_path):
    list_series = []
    patterns = extract_patterns_old(result_path)
    pattern_list = patterns.values.tolist()

    for pattern in pattern_list:
        pattern_decoded = ""
        for itemset in pattern[0]:
            if type(itemset) == list:
                cell = '<'
                for item in itemset:
                    cell += str(item)
                    cell += ','
                cell = cell[:-1]
                cell += '>'
                pattern_decoded += cell
            else:
                pattern_decoded += '<' + str(itemset) + '>'

        list_series.append(pd.Series([pattern_decoded, pattern[1], pattern[2]], index=["patterns", "supp", "%supp"]))

    return pd.DataFrame(columns=["patterns", "supp", "%supp"]).append(list_series, ignore_index=True)
