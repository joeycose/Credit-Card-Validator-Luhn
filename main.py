# Input credit card number
credit_card = input("Enter your credit card number : ")

# Checking number, last digit for our credit card
checking_number = credit_card[-1]
# Credit card without last character
new_string = credit_card[:-1]

# Reverse the new string without the checking number
reverse_string = new_string[::-1]
# convert the reversed string into int data types so we can loop
num_list = [int(x) for x in reverse_string]


# For loop to take even numbers and double them,
# if results are greater than 9 , subtract 9 from those numbers
even_sum = 0
for even_num in num_list:
    # if even_num is even
    if even_num % 2 == 0:
        # even_num = even_num + even_num
        even_num += even_num
        # if even_num is greater than 9
        if even_num > 9:
            # even_num minus 9
            even_num - 9
            even_sum += even_num
        # else if even number is less than 9, we can add the numbers untouched to even_sum
        else:
            even_sum += even_num

# add the sum of even_num and the checking number together
final_num = even_sum + int(checking_number)
print(final_num)

# final iteration, if number is divisble by 10, print card valid
# else print card is not valid.
if final_num % 10:
    print("Credit card number is valid")
else:
    print("Credit Card Number is not valid")
