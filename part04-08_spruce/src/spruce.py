# Write your solution here
def spruce(length):
    print("a spruce!")
    i = 1
    while i<= length:
        spaces = length -i
        stars = 2*i-1
        print(" " * spaces + "*" * stars)
        i+=1
    spaces = length -i
    print(" " * (length - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(4)