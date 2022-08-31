struct Solution;

impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut stack: Vec<i32>= Vec::new();
        let mut p_pop: usize = 0;
        for &num in pushed.iter() {
            stack.push(num);
            while stack.len() > 0 && stack[stack.len()-1] == popped[p_pop] {
                stack.pop();
                p_pop += 1;
            }
        }
        if stack.len() == 0 {
            return true;
        }
        return false;
    }
}


fn main() {
    println!("{}", Solution::validate_stack_sequences(vec![1,2,3,4,5], vec![4,5,3,2,1]));
    println!("{}", Solution::validate_stack_sequences(vec![1,2,3,4,5], vec![4,3,5,1,2]));
}