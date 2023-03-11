# Credit-Card-Validator-Luhn
This code prompts the user to input a credit card number, performs a validation check on the credit card number using the Luhn algorithm, and then prints whether the credit card number is valid or not.

The Luhn algorithm works by taking the credit card number and performing the following steps:

Remove the last digit from the credit card number (this is the checking number).
Reverse the remaining digits of the credit card number.
Double every other digit in the reversed credit card number.
If any of the doubled digits are greater than 9, subtract 9 from them.
Sum up all the digits in the modified credit card number.
Add the checking number back to the sum.
If the final sum is divisible by 10, the credit card number is valid.
The code implements these steps by first getting the checking number and the credit card number without the checking number. It then reverses the credit card number and converts it into a list of integers. The code then uses a for loop to double every other digit in the list of integers and add up the modified digits. Finally, it adds the checking number back to the sum and checks if the final sum is divisible by 10.

If the final sum is divisible by 10, the code prints "Credit card number is valid". If the final sum is not divisible by 10, the code prints "Credit Card Number is not valid".
