input = [6,1,9,4,8]
target = 13

def two_sum(input, target):
    discovered = {}
    output = []

    for i in range(len(input)):
        if target - input[i] in discovered.keys():
            output = [discovered[target - input[i]], i]
            break
        else:
            discovered[input[i]] = i

    return output

# TEST
# print(two_sum(input, target))
# OUTPUT: [2, 3]
