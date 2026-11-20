MATH_SIGNS = ["+","-","x","/"]
# input = "34+2x"
input = "123x-"

def stack_to_nb(stack):
    result = []
    if stack[-1] == "+":
        result.append(int(stack[-3]) + int(stack[-2]))
    elif stack[-1] == "-":
        result.append(int(stack[-3]) - int(stack[-2]))
    elif stack[-1] == "x":
        result.append(int(stack[-3]) * int(stack[-2]))
    elif stack[-1] == "/":
        result.append(int(int(stack[-3]) / int(stack[-2])))
    return result

def reverse_polish_notation(input):
    array = list(input)

    while len(array) > 1:
        for i in range(len(array)):
            if array[i] in MATH_SIGNS:
                nb = stack_to_nb([array[i-2],array[i-1],array[i]])
                if i > 2:
                    array = array[0:i-2] + nb + array[i+1:]
                else:
                    array = nb + array[i+1:]
                break
    return array[0]

# TEST
# print(reverse_polish_notation(input))
# OUTPUT: -5
