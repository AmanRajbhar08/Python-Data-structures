#dictionary 1
first_dict={
     "one":1,
     "two":2
}
#dictionary 2
second_dict={
    "three":3,
    "four":4   
}

#dictionary 3
third_dict={
    "five":5,
    "six":6
}

#new dictionary  by concation all three
first_dict.update(second_dict)
first_dict.update(third_dict)

#printing the final dictionary
print(first_dict)

