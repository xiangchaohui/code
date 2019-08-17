"""
test script
"""

import recursion_part1 as rec


Q1_data = [(7,645,238), (11,2), (283719,)]
Q2_data1 = [[], [66,[73, 89, 42, 32], 62, [24, 32], 99], [-10, 12]]
Q2_data2 = [[], [66,[73, 89, 42, 32], 62, [24, 32], 99], [-10, 12]]
Q3_data = [10, 0, 2, 1, 7]

Q4_data = [[], [1,2], [1], [1,2,3]]

Q5_data = [6431, 321]

Q6_data = [(11, [1,5,12,14,18]), (7, [1,3,5,10])]


def main():
    for data in Q1_data:
        print('The answer of question 1:', rec.findPairs(data))

    for data in Q2_data1:
        print('The answer of question 2(1):', rec.recMin(data))

    for data in Q2_data2:
        print('The answer of question 2(2):', rec.mergeList(data))

    for data in Q3_data:
        print('The answer of question 3:', rec.addNext(data))

    for data in Q4_data:
        print('The answer of question 4:', rec.swapElements(data))

    for data in Q5_data:
        print('The answer of question 5:', end=' ')
        rec.funkyNums(data)

    for data in Q6_data:
        print('The answer of question 6:', rec.calcStamp(data))

main()