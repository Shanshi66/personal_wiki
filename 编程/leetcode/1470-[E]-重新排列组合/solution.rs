struct Solution;

impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut new_nums: Vec<i32> = Vec::new();
        for i in 0..n {
            new_nums.push(nums[i as usize]);
            new_nums.push(nums[(i+n) as usize]);
        };
        new_nums
    }
}

fn main() {
    println!("{:?}", Solution::shuffle(vec![2,5,1,3,4,7], 3))
}