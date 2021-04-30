# this is the unittest for the decoder in dream_work.
from dream_work import *


def print_about(about):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi there, {about}')  # Press Ctrl+F8 to toggle the breakpoint.


print("THIS IS A DEMONSTRATION! It shows how the decoder works! \n\tThis is the sample list to decode: {0}\n\t"
      "This is the decoded list: {1}\n".format(sample1, decoder(sample1)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_about('this is the test for the decoder.')
