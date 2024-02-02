// # 217. Contains Duplicate
// # Solved
// # Easy
// # Topics

// # Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// # Example 1:

// # Input: nums = [1,2,3,1]
// # Output: true
// # Example 2:

// # Input: nums = [1,2,3,4]
// # Output: false
// # Example 3:

// # Input: nums = [1,1,1,3,3,4,3,2,4,2]
// # Output: true

// # Constraints:

// # 1 <= nums.length <= 105
// # -109 <= nums[i] <= 109

#include <iostream>
#include <vector>
#include <algorithm> // For std::sort

using namespace std;

class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; i++)
        {
            if (nums[i] == nums[i + 1])
                return true;
        }
        return false;
    }
};

int main()
{
    // Example usage
    Solution solution;
    vector<int> nums = {1, 2, 3, 4, 5, 1}; // Example vector with duplicates
    bool hasDuplicates = solution.containsDuplicate(nums);

    if (hasDuplicates)
    {
        cout << "The array contains duplicates." << endl;
    }
    else
    {
        cout << "The array does not contain duplicates." << endl;
    }

    return 0;
}
