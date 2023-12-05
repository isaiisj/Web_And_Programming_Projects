/**
 * @param {number[]} nums
 * @return {number}
 */
 /*
 Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
  */

//Way one to solve it
/*var majorityElement = function(nums) {
    const  threshold  = nums.length/2;
    const numsMap = {};
    for(let i = 0; i < nums.length; i++){
        numsMap[nums[i]] = (numsMap[nums[i]] || 0) + 1;
        if(numsMap[nums[i]] > threshold){
            return nums[i];
        }
    }
    
};*/

//Second way to solve it saving memory
var majorityElement = function(nums) {
    let count = 1;
    let result = nums[0];
    for(let i = 1; i < nums.length; i++){
        if(nums[i] === result){
            count++;
        }else{
            count--;
        }
        if(count === 0){
            result = nums[i];
            count = 1;
        }
    }
    return result;
};
