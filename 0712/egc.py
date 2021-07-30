"""
THE EGC Sequence

In the ECG Sequence (that always starts with the numbers 1 and 2), every number that succeeds is the
smallest not already present in the sequence and that shares a factor (excluding 1) with its preceding
number. Every number in the ECG Sequence (besides 1 and 2) has a different index from its natural
index in a normal numeric sequence. See the example below to establish the ECG Sequence Index of
number 3.

# Find the smallest number that is not in sequence...
# This number shares a factor with the preceding?
SEQUENCE = [1, 2]
3 = no factors shared with 2
4 = shares factor 2 with number 2
SEQUENCE = [1, 2, 4]
3 = no factors shared with 4
5 = no factors shared with 4
6 = shares factor 2 with number 4
SEQUENCE = [1, 2, 4, 6]
3 = shares factor 3 with number 6
SEQUENCE = [1, 2, 4, 6, 3]
Number 3 is at index 4 in the ECG Sequence.
Given an integer n implement a function that returns its ECG Sequence Index.

FIRST NUMBERS:
v: 1 2 4 6 3 9 12 8 10 5
i: 0 1 2 3 4 5 6  7 8  9

v: 15 18 14 7  21 24 16 20 22 11
i: 10 11 12 13 14 15 16 17 18 19

v: 33 27 30 25 35 28 26 13 39 36
i: 20 21 22 23 24 25 26 27 28 29

Ex:
ecg_seq_index(3) = 4
ecg_seq_index(5) = 9
ecg_seq_index(7) = 13

"""

# to do
