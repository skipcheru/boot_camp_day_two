# function to find the max and min of numbers in a list
def find_max_min(list_a):
    try:
        if isinstance(list_a, list):
            list_b = sorted(list_a)
            if list_b[0] == list_b[-1]:
                return [len(list_b)]  # return length of list
            else:
                return [list_b[0], list_b[-1]]  # return type must be list
    except ValueError():
        return 'Lists only accepted'




