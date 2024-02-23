// 347. Top K Frequent Elements
// Solved
// Medium
// Topics
// Companies
// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]

// Constraints:

// 1 <= nums.length <= 105
// -104 <= nums[i] <= 104
// k is in the range [1, the number of unique elements in the array].
// It is guaranteed that the answer is unique.

// Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;
struct MyStruct
{
    int intValue;
    char charValue;
    double doubleValue;
};
class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> count_map;
        vector<vector<int>> ans(nums.size() + 1);
        vector<int> final;
        for (int num : nums)
        {
            try
            {
                count_map[num] += 1;
            }
            catch (...)
            {
                count_map[num] = 1;
            }
        }

        for (const auto &pair : count_map)
        {
            int key = pair.first;
            int val = pair.second;

            ans[val].push_back(key);
        }
        for (auto subarr = ans.rbegin(); subarr != ans.rend(); subarr++)
        {
            for (int num : *subarr)
            {
                final.push_back(num);
                k--;
                if (k <= 0)
                {
                    return final;
                }
            }
        }
        // for (auto &subarr : ans)
        // {
        //     for (int num : subarr)
        //     {
        //         final.push_back(num);
        //         k--;
        //         if (k <= 0)
        //         {
        //             break;
        //         }
        //     }
        // }

        return final;
    }
};

int main()
{
    Solution sol;
    // vector<int> nums = {1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5};
    // vector<int> nums = {1, 2};
    vector<int> nums = {4, 1, -1, 2, -1, 2, 3};
    int k = 2;
    vector<int> ans = sol.topKFrequent(nums, k);
    for (int num : ans)
    {
        cout << num << " ";
    }
    return 0;
}