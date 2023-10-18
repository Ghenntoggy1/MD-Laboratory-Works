# # 1. Subsets:
def subsets(set):
    set.sort()  # sort the set introduced by user
    powset = [[]]  # initialize the power set
    for el in set:  # take every element in the user set
        for ss in powset:  # take every subset element in powerset
            powset = powset + [ss + [el]]  # add to the power set a new subset with a set that contains the subset
            # and adds the element from the user set to this subset
            # we concatenate a list to another list ( example [[]] + [[1]] = [[], [1]] )
    return powset


b = input("set = ")  # user input the set of elements
ul = b[1:-1].split(',')  # takes elements omitting [ ] chars, split the string into chars and omits the comma
h = subsets(ul)
translation = {39: ""}
ul1 = str(h).translate(translation)
print(ul1)
print(len(h))