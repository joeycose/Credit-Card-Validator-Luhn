def is_valid_credit_card_number(card_number):
    # Get the checking number and the credit card number without the checking number
    checking_number = int(card_number[-1])
    credit_card_number = card_number[:-1]

    # Reverse the credit card number and convert it into a list of integers
    reversed_card_number = [int(x) for x in reversed(credit_card_number)]

    # Double every other digit in the reversed credit card number
    doubled_digits = []
    for i in range(len(reversed_card_number)):
        if i % 2 == 0:
            doubled_digit = reversed_card_number[i] * 2
            if doubled_digit > 9:
                doubled_digit -= 9
            doubled_digits.append(doubled_digit)
        else:
            doubled_digits.append(reversed_card_number[i])

    # Sum up all the digits in the modified credit card number
    modified_sum = sum(doubled_digits)

    # Add the checking number back to the sum
    total_sum = modified_sum + checking_number

    # Check if the final sum is divisible by 10
    if total_sum % 10 == 0:
        print("Credit card number is valid")
    else:
        print("Credit card number is not valid")


#main
card_number = input("Enter your credit card number: ")
is_valid_credit_card_number(card_number)
