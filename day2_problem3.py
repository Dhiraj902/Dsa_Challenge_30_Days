"""
Problem Statement
In the kingdom of Techlandia, a powerful sorcerer named Zael has hidden treasures in an enchanted vault, and the only way to open it is by entering a secret password. However, Zael has set two conditions for the password:

Every number in the password must appear an even number of times.
At least one number must appear exactly twice.
To solve the puzzle, adventurers must verify if the password meets these conditions and also identify the most frequent element in the password. If they succeed, the vault will open, revealing the treasures hidden inside. The fate of Techlandia’s treasures depends on solving this magical riddle!

Input Format
The first line contains an integer N, representing the number of elements in the password.

The second line contains N space-separated integers, representing the elements of the password array.

Output Format
Print "VALID" if the password satisfies the conditions; otherwise, print "INVALID".

In either case, also print the most frequent element in the password. If there are multiple elements with the same highest frequency, print the smallest one.

 
Constraints
2 <= N <= 10^6

1 <= Ai <= 10^7

Sample Testcase 0
Testcase Input
6
2 2 4 4 4 4
Testcase Output
VALID
4
Explanation
All elements appear an even number of times.
The number 4 appears the most frequently (4 times).
The number 2 appears exactly twice, satisfying the requirement of at least one element appearing exactly twice.

Sample Testcase 1
Testcase Input
5
1 1 2 2 3
Testcase Output
INVALID
1
Explanation




The frequencies of elements are 1:2, 2:2, and 3:1.
The number 3 appears an odd number of times, violating the frequency condition.
The most frequent element is 1 (or 2 since both appear twice, but the smallest is selected).




"""


from collections import Counter

def validate_password(password):
    freq = Counter(password)

    all_even = all(count % 2 == 0 for count in freq.values())
    has_exactly_two = any(count == 2 for count in freq.values())

    max_freq = max(freq.values())
    most_frequent = min([num for num, count in freq.items() if count == max_freq])

    if all_even and has_exactly_two:
        return ("VALID", most_frequent)
    else:
        return ("INVALID", most_frequent)
arr= [1,1,2,2,3]#[2, 2, 4, 4, 4, 4]
print(validate_password(arr))
