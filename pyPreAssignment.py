#Q1
def hello_name(user_name):
    print(user_name)

#Q2
def first_odds():
    for num in range(1, 1001):
        if num % 2 == 1:
            print(num)

#Q3
def max_num_in_list(a_list):
    return max(a_list)

#Q4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
    else:
        return False

#Q5
def is_consecutive(a_list):
    for i in range(0, len(a_list)-1):
        if a_list[i+1] <= a_list[i]:
            return False
    return True

#hello_name("Chan")
#first_odds()
#max_num_in_list([1,2,10,4,5])
#print(is_leap_year(2022))
#print(is_consecutive([1,2,5,10]))