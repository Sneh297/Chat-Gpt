prompts = [
  {
    "prompt": """Minimum Time to Complete Tasks with Dependencies

You are given N tasks numbered from 0 to N-1. Each task takes 1 unit of time to complete. Some tasks depend on the completion of other tasks and can only start once all their prerequisite tasks are finished. You are given a list of dependency pairs (a, b), meaning task a must be completed before task b can start.

You have unlimited resources and can run multiple tasks in parallel as long as their dependencies are satisfied. Your task is to find the minimum time required to complete all tasks.

Function Description:  
Implement the function minimumTimeToCompleteTasks with parameters:  
- N: integer, total number of tasks  
- M: integer, number of dependency pairs  
- dependencies: list of pairs (a, b) where task a must be completed before task b

Return:  
- int: minimum time to complete all tasks

Constraints:  
- 1 ≤ N ≤ 10^5  
- 0 ≤ M ≤ 10^5  
- 0 ≤ a, b < N

Sample Input:  
5 4  
0 1  
1 2  
0 3  
3 4

Sample Output:  
3

Explanation:  
- Task 0 starts at time 1  
- Tasks 1 and 3 depend on task 0, so they start at time 2  
- Task 2 depends on 1, and task 4 depends on 3, so they start at time 3  
Thus, the minimum time to complete all tasks is 3."""
  },
   {
    "prompt": """Bitwise Palindromic Paths

You are given a binary matrix of size N x M where each cell contains either 0 or 1. A path from the top-left cell (0,0) to the bottom-right cell (N-1,M-1) is valid if you can only move right or down at each step.

A path is called bitwise palindromic if the sequence of bits collected along the path forms a palindrome when interpreted as a string (e.g., 0110, 1, 101).

Your task is to count the number of such bitwise palindromic paths.

Function Description: You need to implement the function countBitwisePalindromicPaths.

Parameters:
. N: An integer representing the number of rows.
· M: An integer representing the number of columns.
· grid: A 2D list of size N x M consisting of binary values (0 or 1).

Return: An integer representing the number of valid bitwise palindromic paths from (0,0) to (N-1,M-1), modulo 10⁹+7.

Input Format:
· The first line contains a single integer N.
. The second line contains a single integer M.
. The next N lines each contain M space-separated binary digits

· 1 ≤ N, M ≤ 15

Sample input
2
2
1 0
0 1

Sample output
2

Explanation

There are 2 paths:
. Path 1: 1 → 0 → 1 forms "101", which is a palindrome
. Path 2: 1 → 0 → 1 – same path, same pattern, counted again

Note: Your code must be able to print the sample output from the provided sample input. However, your code is run against multiple hidden test cases. Therefore, your code must pass these hidden test cases to solve the problem statement.

Limits
Time Limit: 5.0 sec(s) for each input file
Memory Limit: 256 MB
Source Limit: 1024 KB

Scoring
Score is assigned if any test case passes

Allowed Languages """
  },
   {
    "prompt": """Given a string, determine how many different substrings exist that have no repeating characters. Two substrings are considered different if they have different start or end indices.

Example  
s = "abac"  

The substrings with no repeating characters are "a", "b", "a", "c", "ab", "ba", "ac", and "bac".  
Note that "aba" and "abac" do not qualify because the character 'a' is repeated in them. Also, "a" and "a" both qualify because their start indices are different: s[0] and s[2]. There are 8 such substrings.

Function Description  
Complete the function findSubstrings in the editor with the following parameter:  
string s: the given string  

Returns  
int: the number of substrings in s that have no repeating characters  

Constraints  
- 1 ≤ length of s ≤ 10⁵  
- s consists of only lowercase English letters, ascii['a'-'z']

Input Format For Custom Testing  
The only line of input contains a string, s.

Sample Case 0

Sample Input For Custom Testing  
bcada

Sample Output  
12

Explanation  
There are 12 substrings in "bcada" that have no repeating characters: "b", "c", "a", "d", "a", "bc", "ca", "ad", "da", "bca", "cad", and "bcad"

Sample Case 1

Sample Input For Custom Testing  
abcd

Sample Output  
10

Explanation  
There are 10 substrings in "abcd" that have no repeating characters: "a", "b", "c", "d", "ab", "bc", "cd", "abc", "bcd", and "abcd"""
  },
    {
    "prompt": """Minimum Time to Complete Tasks with Dependencies

You are given N tasks numbered from 0 to N-1. Each task takes 1 unit of time to complete. Some tasks depend on the completion of other tasks and can only start once all their prerequisite tasks are finished. You are given a list of dependency pairs (a, b), meaning task a must be completed before task b can start.

You have unlimited resources and can run multiple tasks in parallel as long as their dependencies are satisfied. Your task is to find the minimum time required to complete all tasks.

Function Description:  
Implement the function minimumTimeToCompleteTasks with parameters:  
- N: integer, total number of tasks  
- M: integer, number of dependency pairs  
- dependencies: list of pairs (a, b) where task a must be completed before task b

Return:  
- int: minimum time to complete all tasks

Constraints:  
- 1 ≤ N ≤ 10^5  
- 0 ≤ M ≤ 10^5  
- 0 ≤ a, b < N

Sample Input:  
5 4  
0 1  
1 2  
0 3  
3 4

Sample Output:  
3

Explanation:  
- Task 0 starts at time 1  
- Tasks 1 and 3 depend on task 0, so they start at time 2  
- Task 2 depends on 1, and task 4 depends on 3, so they start at time 3  
Thus, the minimum time to complete all tasks is 3."""
  },
   {
    "prompt": """Bitwise Palindromic Paths

You are given a binary matrix of size N x M where each cell contains either 0 or 1. A path from the top-left cell (0,0) to the bottom-right cell (N-1,M-1) is valid if you can only move right or down at each step.

A path is called bitwise palindromic if the sequence of bits collected along the path forms a palindrome when interpreted as a string (e.g., 0110, 1, 101).

Your task is to count the number of such bitwise palindromic paths.

Function Description: You need to implement the function countBitwisePalindromicPaths.

Parameters:
. N: An integer representing the number of rows.
· M: An integer representing the number of columns.
· grid: A 2D list of size N x M consisting of binary values (0 or 1).

Return: An integer representing the number of valid bitwise palindromic paths from (0,0) to (N-1,M-1), modulo 10⁹+7.

Input Format:
· The first line contains a single integer N.
. The second line contains a single integer M.
. The next N lines each contain M space-separated binary digits

· 1 ≤ N, M ≤ 15

Sample input
2
2
1 0
0 1

Sample output
2

Explanation

There are 2 paths:
. Path 1: 1 → 0 → 1 forms "101", which is a palindrome
. Path 2: 1 → 0 → 1 – same path, same pattern, counted again

Note: Your code must be able to print the sample output from the provided sample input. However, your code is run against multiple hidden test cases. Therefore, your code must pass these hidden test cases to solve the problem statement.

Limits
Time Limit: 5.0 sec(s) for each input file
Memory Limit: 256 MB
Source Limit: 1024 KB

Scoring
Score is assigned if any test case passes

Allowed Languages """
  },
   {
    "prompt": """Given a string, determine how many different substrings exist that have no repeating characters. Two substrings are considered different if they have different start or end indices.

Example  
s = "abac"  

The substrings with no repeating characters are "a", "b", "a", "c", "ab", "ba", "ac", and "bac".  
Note that "aba" and "abac" do not qualify because the character 'a' is repeated in them. Also, "a" and "a" both qualify because their start indices are different: s[0] and s[2]. There are 8 such substrings.

Function Description  
Complete the function findSubstrings in the editor with the following parameter:  
string s: the given string  

Returns  
int: the number of substrings in s that have no repeating characters  

Constraints  
- 1 ≤ length of s ≤ 10⁵  
- s consists of only lowercase English letters, ascii['a'-'z']

Input Format For Custom Testing  
The only line of input contains a string, s.

Sample Case 0

Sample Input For Custom Testing  
bcada

Sample Output  
12

Explanation  
There are 12 substrings in "bcada" that have no repeating characters: "b", "c", "a", "d", "a", "bc", "ca", "ad", "da", "bca", "cad", and "bcad"

Sample Case 1

Sample Input For Custom Testing  
abcd

Sample Output  
10

Explanation  
There are 10 substrings in "abcd" that have no repeating characters: "a", "b", "c", "d", "ab", "bc", "cd", "abc", "bcd", and "abcd"""
  }
]