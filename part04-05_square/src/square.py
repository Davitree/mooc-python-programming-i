# Copy here code of line function from previous exercise
def line(length,string):
    if string == "":
        print("*"*length)
    else:
        print(string[0] * length)

def square(size, character):
    length = size
    while size >0:
        line(length,character)
        size-=1
    # You should call function line here with proper parameters

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")