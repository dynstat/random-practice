// 238. Product of Array Except Self
// Solved
// Medium
// Topics
// Companies
// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.

// Example 1:

// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]
// Example 2:

// Input: nums = [-1,1,0,-3,3]
// Output: [0,0,9,0,0]

// Constraints:

// 2 <= nums.length <= 105
// -30 <= nums[i] <= 30
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> productExceptSelf(vector<int> &nums)
{
    int len = nums.size();
    vector<int> ans(len);
    int sum_ = 1;
    for (int i = 0; i < len; i++)
    {
        ans[i] = sum_;
        sum_ *= nums[i];
    }
    sum_ = 1;
    for (int j = len - 1; j >= 0; j--)
    {
        ans[j] *= sum_;
        sum_ *= nums[j];
    }
    return ans;
}

int main()
{
    vector<int> nums = {1, 2, 3, 4};
    vector<int> ans = productExceptSelf(nums);
    for (int i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << " ";
    }
    cout << endl;
}
