from functools import reduce


def all_even(lst):
    #i for i in lst in enumerate(lst) if i % 2 == 0
    all_even = [i for i in range(100) if i % 2 == 0]

print(all_even)

def all_not_multiple(lst, n):
    if i in lst is i % n == 0:
        return lst
n = 5
print(all_not_multiple)

def max_from_2_tuples(tuples):
    if tuples is None or len(tuples)<=1:
        return tuples
    return reduce(lambda x,y:(max(x[0], y[0]), max(x[1], y[1])), tuples)

print(max_from_2_tuples(tuples))

def lower_case_words(sentence):
    x.lower() i for i in strings
        return strings

def baby_names(names, last_name):
    lis = [i + " " + j + " " + baby_names[1] for i in baby_names[0] for j in baby_names[0] if j != i]
    print(lis)


