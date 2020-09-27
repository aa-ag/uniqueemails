# Unique Email Counter

This web service accepts `http` requests and returns responses based on the condition outlined here.

This app accepts a list of email addresses and returns an integer indicating the number of unique email addresses.

Unique email addresses means they will be delivered to the same account using Gmail account matching. Specifically: Gmail will ignore the placement of "." in the username. And it will ignore any portion of the username after a "+".

## Access this program

You can access this program [here]().

## Constrains

test.email@gmail.com, test.email+spam@gmail.com and testemail@gmail.com will all go to the same address, and thus the result should be 1.
test.email@gmail.com and test.email@fetchrewards.com are two different email addresses, and thus the result should be 2.

### Technologies used

- Python
- Flask
- Bootstrap
- Javascript

### Contact

For any questions, please contact [me](https://www.linkedin.com/in/aa-ag/).