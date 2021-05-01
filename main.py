# this is the unittest for the decoder in dream_work.
from dream_work import *
import sys
from pathlib import Path


def print_about(about):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi there, {about}')  # Press Ctrl+F8 to toggle the breakpoint.


print("THIS IS A DEMONSTRATION! It shows how the decoder works! \n\tThis is the sample list to decode: {0}\n\t"
      "This is the decoded list: {1}\n".format(expected_to_fail, decoder(test_to_fail2)))
print("press enter to use 'sys.stdin'")
'''
*********************************************
Task: SYS.STDIN
    - use stdin to load data from a text file
**********************************************
'''
for something in sys.stdin:
    # assign data to "text"
    dataFolder = Path(r'C:\Users\ncssa\PycharmProjects\dreamWork\sample-1.txt')
    text = dataFolder.read_text()
    # split string to a list
    list1 = text.rsplit(" ")
    print("list to decode: ", list1)

    # this is the decoder function
    def decoder(work):
        number = 0  # int variable to store converted numbers - temporary
        list2 = []  # This is a new list to hold the decoded numbers
        for item in work:
            number += int(item)
            list2.append(number)
        return list2


    # call the decoder function
    decoded_list1 = decoder(list1)
    print("decoded list: ", decoded_list1)


lines = sys.stdin.readlines()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_about('this is the test for the decoder.')
