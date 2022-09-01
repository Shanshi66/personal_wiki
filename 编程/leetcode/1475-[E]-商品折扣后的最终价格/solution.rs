struct Solution;

impl Solution {
    pub fn final_prices(prices: Vec<i32>) -> Vec<i32> {
        let mut stack =  Vec::new();
        let mut new_price = Vec::new();
        for (idx, &p) in prices.iter().enumerate() {
            new_price.push(p);
            while !stack.is_empty() && p <= prices[stack[stack.len()-1] as usize] {
                new_price[stack[stack.len()-1] as usize] -= p;
                stack.pop();
            }
            stack.push(idx as i32);
        };
        return new_price;
    }
}

fn main() {
    println!("{:?}", Solution::final_prices(vec![8,4,6,2,3]));
    println!("{:?}", Solution::final_prices(vec![1,2,3,4,5]));
}