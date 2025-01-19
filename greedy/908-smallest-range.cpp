class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        int minNum=INT_MAX, maxNum=INT_MIN;
        for ( int i =0; i<nums.size();i++)
        {
            minNum = min(minNum,nums[i]);
            maxNum=max(maxNum,nums[i]);
        }
        minNum+=k;
        maxNum-=k;
        cout << maxNum-minNum;
        return max(0,maxNum-minNum); // if it's negative we could've used a smaller value of k on either side to get 0
        
    }
};