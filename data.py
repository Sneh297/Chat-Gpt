copy_prompts = [
    {
        'prompt': '''Given a string, determine how many different substrings exist that have no repeating characters. Two substrings are considered different if they have different start or end indices.

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
There are 10 substrings in "abcd" that have no repeating characters: "a", "b", "c", "d", "ab", "bc", "cd", "abc", "bcd", and "abcd" ''',

        'response': '''Given a string, determine how many different substrings exist that have no repeating characters. Two substrings are considered different if they have different start or end indices.



Example  

s = "abac"  

The substrings with no repeating characters are "a", "b", "a", "c", "ab", "ba", "ac", and "bac". Note that "aba" and "abac" do not qualify because the character 'a' is repeated in them. Also, "a" and "a" both qualify because their start indices are different: s[0] and s[2]. There are 8 such substrings.



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

There are 10 substrings in "abcd" that have no repeating characters: "a", "b", "c", "d", "ab", "bc", "cd", "abc", "bcd", and "abcd"

'''
    },
]
