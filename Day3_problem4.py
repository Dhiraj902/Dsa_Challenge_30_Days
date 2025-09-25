"""
Problem Statement
In the serene village of Blossomville, two dedicated gardeners, Lily and Rose, took pride in their flourishing gardens. Lily's garden was adorned with vibrant flowers, while Rose's garden was filled with aromatic herbs. On a beautiful sunny day, they decided to have a friendly competition to determine whose garden attracted more bees.

Lily created a list1 of N1 elements of the types of flowers she had and their quantities. Rose did the same with her herbs and created a list2 of N2 elements. They then compared their lists.

For each type of flower in Lily's garden, they compared its quantity with the quantity of the same type of herb in Rose's garden. If Lily had more of a particular flower than Rose had herbs, Lily noted down that flower in her notebook.

Lily ensured that her final list of flowers maintained the same order as they bloomed in her garden, showcasing her beautiful array of flowers.

Given two lists of integers representing the flower quantities in Lily's garden and the herb quantities in Rose's garden, you need to determine which flowers Lily should note down in her notebook based on the above criteria.

Input Format
The first line contains an integer N1, the number of flowers in Lily's garden.

The second line contains N1 space-separated integers representing the quantities of each flower in Lily's garden.

The third line contains an integer N2, the number of herbs in Rose's garden.

The fourth line contains N2 space-separated integers representing the quantities of each herb in Rose's garden.

Output Format
Print the list of space-separated flowers that Lily should note down in her notebook, preserving the order as they appear in Lily's garden.

If there are no such flowers, print -1.

Constraints
1 <= N1 <= 10^3

1 <= elementsoflist1 <= 10^4

1 <= N2 <= 10^3

1 <= elementsoflist2 <= 10^4

Sample Testcase 0
Testcase Input
5
1 2 3 2 1
5
2 3 4 3 2
Testcase Output
1 1
Explanation
Flower 1 appears twice in Lily's garden but not at all in Rose's garden. Soit is included.
Flower 2 appears twice in Lily's garden and twice in Rose's garden, so it is not included.
Flower 3 appears once in Lily's garden and twice in Rose's garden, so it is not included.
Flower 1 appears twice in Lily's garden but not at all in Rose's garden. Soit is included.
The final list of flowers maintained the same order as they bloomed in Lily's garden

Sample Testcase 1
Testcase Input
3
4 5 6
3
1 2 3
Testcase Output
4 5 6
Explanation
All flowers in Lily's garden are more frequent than any herb in Rose's garden.
"""
def user_logic(n1, flowers, n2, herbs):
    from collections import Counter
    
    # Count the occurrences of flowers and herbs
    count_flowers = Counter(flowers)
    count_herbs = Counter(herbs)
    
    result = []
    
    # Check each flower in order
    for flower in flowers:
        if count_flowers[flower] > count_herbs.get(flower, 0):
            result.append(flower)
            count_flowers[flower] -= 1  # Decrease count for duplicates
    
    # If no flowers meet the condition, return [-1]
    if not result:
        return [-1]
    
    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n1 = int(data[0])
    flowers = list(map(int, data[1:n1+1]))
    n2 = int(data[n1+1])
    herbs = list(map(int, data[n1+2:n1+2+n2]))
    
    # Call the user logic function and get the result
    result = user_logic(n1, flowers, n2, herbs)
    
    # Print the result in the required format
    if result == [-1]:
        print(-1)
    else:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()



