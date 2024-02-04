#include <vector>
#include <unordered_map>
#include <iostream>
#include <typeinfo>

std::vector<int> twoSum(std::vector<int> &nums, int target)
{
    std::unordered_map<int, int> store;
    std::vector<int> temp;
    int len = nums.size();

    for (int i = 0; i < len; i++)
    {
        int remaining_val = target - nums[i];

        int c = store.count(remaining_val);
        if (c)
        {
            // If the complement exists in the map, return the indices
            temp = {store[remaining_val], i};
            const std::type_info &typeInfo = typeid(temp);
            const char *name = typeInfo.name();
            return temp; // Return the indices as a vector
        }
        // Otherwise, store the current number and its index in the map
        store[nums[i]] = i;
    }

    // Return an empty vector if no solution is found
    return {};
}

int main()
{
    std::vector<int> test_vector = {2, 7, 11, 15};
    std::vector<int> result = twoSum(test_vector, 9);
    // Print the result
    for (int index : result)
    {
        std::cout << index << " ";
    }
    return 0;
}