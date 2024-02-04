// 49. Group Anagrams
// Solved
// Medium
// Topics
// Companies
// Given an array of strings strs, group the anagrams together. You can return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Example 2:

// Input: strs = [""]
// Output: [[""]]
// Example 3:

// Input: strs = ["a"]
// Output: [["a"]]

// Constraints:

// 1 <= strs.length <= 104
// 0 <= strs[i].length <= 100
// strs[i] consists of lowercase English letters.

// The task is to generate code to group the anagrams together from the given array of strings.
// We can use a hashmap to group the anagrams by their sorted representation.
// Then, we can iterate through the hashmap and collect the grouped anagrams into a result vector.

#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <iostream>

#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <iostream>

std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string> &strs)
{
    std::unordered_map<std::string, std::vector<std::string>> anagramMap;

    for (std::string &s : strs)
    {
        std::string sortedStr = s;
        // Sort the characters of the string in ascending order
        std::sort(sortedStr.begin(), sortedStr.end());
        anagramMap[sortedStr].push_back(s);
    }

    std::vector<std::vector<std::string>> result;
    for (auto &entry : anagramMap)
    {
        result.push_back(entry.second);
    }

    return result;
}

int main()
{
    std::vector<std::string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    std::vector<std::vector<std::string>> result = groupAnagrams(strs);
    for (std::vector<std::string> &vec : result)
    {
        for (std::string &s : vec)
        {
            std::cout << s << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}