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

    auto compare = [](const std::pair<int, int> &a, const std::pair<int, int> &b)
    {
        return a.second < b.second;
    };

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