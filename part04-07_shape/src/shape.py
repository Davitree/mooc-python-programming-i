# Copy here code of line function from previous exercise and use it in your solution
def line(length,string):
    if string == "":
        print("*"*length)
    else:
        print(string[0] * length)
def shape(size,character,newSize,newCharacter):
    i=1
    nSize =newSize 
    length = size

    while i <= size:
        line(i,character)
        i +=1
    while newSize >0:
        line(size,newCharacter)
        newSize-=1
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")