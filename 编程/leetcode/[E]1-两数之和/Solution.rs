// 0ms代码，优雅
// 遍历数组，利用序解决元素重复等问题
use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let len = nums.len();
        let mut hash = HashMap::with_capacity(len-1);
        hash.insert(nums[0],0);
        for i in 1..len {
            let opt = hash.get(&(target - nums[i]));
            match opt {
                None=>{
                    hash.insert(nums[i],i);
                },
                Some(t)=>{
                    return vec![*t as i32 ,i as i32]
                }
            }
        }
        return vec![0; 2];
    }
}

fn main() {
    let v = vec![1,2,3,4];
    let target = 7;
    let result = Solution::two_sum(v, target);
    println!("{:?}", result);
}

// 第一次用rust刷题，这么简单写了一小时，而且特别丑。。
// WA了很多次，典型case
// [3,3] 6 ==> 0,1
// [3,2,4] 6 ==> 1,2

// impl Solution {
//     pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
//         use std::collections::HashMap;
//         let mut map= HashMap::with_capacity(nums.len());
//         for (idx, num) in nums.iter().enumerate() {
//             if map.get(num) == None {
//                 let tmp_vec = Vec::with_capacity(2);
//                 map.insert(num, tmp_vec);
//             }
//             if let Some(v) = map.get_mut(num) {
//                 v.push(idx);
//             }
//         }
//         // println!("{:?}", map);
//         let mut result = Vec::new();
//         for num in &nums {
//             if num*2 > target || map.get(&(target-num)) == None || result.len() > 0 {
//                 continue;
//             }
//             if target-num == *num {
//                 if map[num].len() < 2 {
//                     continue;
//                 }
//                 result.push(map[num][0] as i32);
//                 result.push(map[num][1] as i32);
//             }
//             else {
//                 result.push(map[num][0] as i32);
//                 result.push(map[&(target-num)][0] as i32);
//             }
//         }
//         result
//     }
// }
// @lc code=end

