'''

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

'''


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Declare an empty hashmap
        hashmap = {}

        # First fill the hashmap
        for num in nums:
            # if hey exists add 1
            if num in hashmap:
                hashmap[num] += 1
            else:
                # if not add it and add one
                hashmap[num] = 1

        # Create a list of empty lists 
        freq_list = [[] for i in range(len(nums))]
        # Fill frequency list
        for key, value in hashmap.items():
            # index is the times it appears the value
            index = value - 1
            freq_list[index].append(key)

        # Create a list to return most freq elements
        most_freq_elem = []

        # Check the frequency list from end to start
        # unitl number of items in most freq elems are
        # equal to k
        
        for i in range(len(freq_list)-1,-1,-1):
            # Check if the index has a non empty list
            if freq_list[i]:
                # Iterate that list
                for e in freq_list[i]:
                    # if elements are less than k
                    if len(most_freq_elem) < k:
                        # append it to most freq
                        most_freq_elem.append(e)
                    else:
                        # if are greater than 2 end loop
                        # to avoid senseless iterations
                        return most_freq_elem

        return most_freq_elem

# Time complexity: O(n)
