#import the text wrapper module
import textwrap

#sample string 
sample_string='''Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.'''
  
#fing the width of wrapper till 50   
wapper=textwrap.TextWrapper(width=50)

#using text wrapper and filling  the wapper 
string=wapper.fill(text=sample_string)

#printing the 50 width text
print(string)
