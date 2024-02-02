// # Code
// # Testcase
// # Test Result
// # Test Result
// # 242. Valid Anagram
// # Solved
// # Easy
// # Topics
// # Companies
// # Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// # An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// # Example 1:

// # Input: s = "anagram", t = "nagaram"
// # Output: true
// # Example 2:

// # Input: s = "rat", t = "car"
// # Output: false

// # Constraints:

// # 1 <= s.length, t.length <= 5 * 104
// # s and t consist of lowercase English letters.

// # Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

#include <string>
#include <iostream>
#include <unordered_map>
// using namespace std;

class Solution
{
public:
    bool isAnagram(std::string s, std::string t)
    {
        if (s.size() != t.size())
            return false;

        std::unordered_map<char, int> counts;
        for (int i = 0; i < s.size(); ++i)
        {
            counts[s[i]]++;
            counts[t[i]]--;
                }

        for (auto count : counts)
        {
            if (count.second != 0)
            {
                return false;
            }
        }

        return true;
    }
};

// using the above class

int main()
{
    Solution solution;
    bool result = solution.isAnagram("anagram", "nagaram");
    std::cout << (result ? "true" : "false") << std::endl;
    return 0;
}