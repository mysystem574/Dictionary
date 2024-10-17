'''
The program takes a dictionary and prints the sum of all the items in the dictionary.
Problem Solution:
1. Declare and initialize the n number of dictionary values from the user.
2. Find the sum of all the values in the dictionary.
3. Print the total sum.
4. Exit.
Sample Input:
3
100
540
239
Sample Output :
879
'''

n=int(input())
dict_={'A':0,'B':0,'C':0}
for i in range(n):
    value=int(input())
    dict_[value]=value
sum_of_values=sum(dict_.values())
print(sum_of_values)

'''
output:
3
100
540
239
879
'''
