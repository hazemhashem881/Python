
def count_upper_lower_case(string):
    upper_case_count = 0
    lower_case_count = 0
    for char in string:
        if char.isupper():
            upper_case_count +=1
        elif char.islower():
            lower_case_count +=1
    print("No. of upper case char is :",upper_case_count)
    print("No. of lower case char is :",lower_case_count) 

count_upper_lower_case("This Is For Test")