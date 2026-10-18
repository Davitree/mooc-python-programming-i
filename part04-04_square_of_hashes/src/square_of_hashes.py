
def line(length,string):
    if string == "":
        print("*"*length)
    else:
        print(string[0] * length)
# Copy here code of line function from previous exercise

def square_of_hashes(size):
    length = size

    # You should call function line here with proper parameters
    while size > 0:
        line(length, "#")
        size -=1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
