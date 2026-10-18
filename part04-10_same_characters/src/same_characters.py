# Write your solution here
# You can test your function by calling it within the following block
def same_chars(string,index1,index2):
    if index1 >=0 and index1<len(string) and index2 >=0 and index2<len(string) :
       if string[index1] == string[index2]:
          return True
       else:
          return False
    else:
       return False
    
    
    
    
if __name__ == "__main__":
  print(same_chars("abc", 0, 3))