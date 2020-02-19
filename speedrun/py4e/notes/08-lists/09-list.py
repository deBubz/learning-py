# # fname = input("Enter file name: ")
# fh = open('romeo.txt')
# lst = list()
# for line in fh:
#     for word in line.split():
#         if word not in lst:
#             lst.append(word)

# lst.sort()
# print(lst)
# print(line.rstrip())

# List Excercise

# e1
# function modifies a list removing first and last elements
# return NONE

class ListEx:
    the_list = list()
    def __init__(self):
        print("enter your list, and stop with x:")
        entry = input()
        while entry != 'x':
            if entry == '': continue
            if entry == 'x': break;
            self.the_list.append(entry)
            entry = input()
        print("the list is %d items long", len(self.the_list))
        print(self.the_list)
        print("note each ex will modify a copy of this list")

    # e1 chop function(list)
    # remove first and last item of list
    # return void
    @staticmethod
    def e1_chop(ls):
        print(ls)
        new_ls = ls[1:len(ls) - 1]
        print(new_ls)

    # e1 middle (list)
    # returns list contains without first and last elem
    def e1_middle(ls):
        copy = list()
        for i in ls: copy.append(i)

        ListEx.e1_chop(copy) 

        return copy

listing = ListEx()
print(ListEx.e1_middle(listing.the_list))
