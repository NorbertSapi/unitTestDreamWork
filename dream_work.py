# this is the module to work on function test: decoder

# These are the sample list from the exercise
# samples are not decoded yet.
sample1 = [28, 2, 3, -3, -2, 1, 2, 35, -1, 0, 0, -1]
sample2 = [5, 1, 1, 1, 1, 0, 0, 0, -1, -1, -1, -1]
sample3 = [14, 2, -2, -3, 0, -1, 4, 0, -1, 1, 4, -2, -3, -3, -2]
sample4 = [-123, -11, 6, 14, -1, -3, 4, 9, 1, 5, -6, 3, -10, 155, -7, 0, 14, -9, 15, 3, 11, -1, -10, -8, 5]
# this is the variable to expected to fail
test_to_fail = [12, 1, 0, -2, 1]

# these are the expected list
expected_list1 = [28, 30, 33, 30, 28, 29, 31, 66, 65, 65, 65, 64]
expected_list2 = [5, 6, 7, 8, 9, 9, 9, 9, 8, 7, 6, 5]
expected_list3 = [14, 16, 14, 11, 11, 10, 14, 14, 13, 14, 18, 16, 13, 10, 8]
expected_list4 = [-123, -134, -128, -114, -115, -118, -114, -105, -104, -99, -105, -102, -112, 43, 36, 36, 50, 41,
                  56, 59, 70, 69, 59, 51, 56]
# this is the variable to expected to fail
expected_to_fail = [12, 13, 13, 11, 12]


# this is the decoder function
# This function will decode the sample list
def decoder(work):
    number = 0  # int variable to store converted numbers - temporary
    list2 = []  # This is a new list to hold the decoded numbers
    for item in work:
        number += int(item)
        list2.append(number)
    return list2
