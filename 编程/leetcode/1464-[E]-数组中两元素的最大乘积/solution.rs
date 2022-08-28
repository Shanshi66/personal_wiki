struct Solution;

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let (mut max_first, mut max_second) = (-1, -1);
        for &n in nums.iter() {
            if n >= max_first {
                max_second = max_first;
                max_first = n;
            } else if n > max_second {
                max_second = n;
            }
        };
        (max_first-1)*(max_second-1)
    }
}


fn main() {
    let result = Solution::max_product([3,4,5,2].to_vec());
    println!("{}", result)
}