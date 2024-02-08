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
#include <queue>
#include <unordered_map>
#include <iostream>

std::vector<int> topKFrequent(std::vector<int> &nums, int k)
{
    std::unordered_map<int, int> freqMap;
    for (int num : nums)
    {
        freqMap[num]++;
    }

    // Define a lambda function 'compare' that takes two pairs of integers as input parameters
    // The lambda function compares the second element of the pairs and returns true if the second element of the first pair is less than the second element of the second pair
    auto compare = [](const std::pair<int, int> &a, const std::pair<int, int> &b)
    {
        return a.second < b.second;
    };

    // Create a priority queue 'pq' of pairs of integers, with the second integer in the pair being the priority value
    // Use the 'compare' lambda function to compare the second elements of the pairs
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, decltype(compare)> pq(compare);

    for (auto &entry : freqMap)
    {
        pq.push(entry);
        if (pq.size() > k)
        {
            pq.pop();
        }
    }

    std::vector<int> result;
    while (!pq.empty())
    {
        result.push_back(pq.top().first);
        pq.pop();
    }

    return result;
}

std::vector<int> topKFrequent2(std::vector<int> &nums, int k)
{
    std::unordered_map<int, int> count_map;

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
    int max = 0;
    int second_max = 0;
    for (auto &pair : count_map)
    {
        if (pair.second > max)
        {
            second_max = max;
            max = pair.first;
        }
    }
    std::vector<int> r = {2, 3};
    return r;
}

int main()
{
    std::vector<int> nums = {1, 1, 1, 2, 2, 3};
    int k = 2;

    std::vector<int> result = topKFrequent(nums, k);

    for (int num : result)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}