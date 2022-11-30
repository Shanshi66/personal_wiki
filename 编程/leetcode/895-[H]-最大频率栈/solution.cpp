#include<map>
#include<vector>
#include<queue>
#include<tuple>
#include<iostream>
#include<unordered_map>
#include<stack>

// 思路：维护一个<num，num出现次数，num最靠栈顶的位置>的堆，单独维护num出现次数，num出现位置的map
// 每次push，将出现次数+1，最新位置压入堆（会有重复，但不影响）
// 每次pop，如果有重复，都弹出堆。将次数-1，最靠顶的位置弹出。将新的元组压入堆。
// 时间复杂度：push O(1)，pop(1)

using namespace std;
using tuple_type = tuple<int, int, int>;

class TupleGT
{
public:
    bool operator() (const tuple_type a, const tuple_type b){
        if (get<1>(a) != get<1>(b)) {
            return get<1>(a) < get<1>(b);
        } 
        else {
            return get<2>(a) < get<2>(b);
        }
    }
};

class FreqStack {
public:
    map<int, vector<int>> num_index;
    map<int, int> num_count;
    priority_queue<tuple_type, vector<tuple_type>, TupleGT> num_pqueue;
    int cnt = 0;

public:
    FreqStack() {
        
    }

    void push(int val) {
        cnt += 1;
        num_count[val] += 1;
        num_index[val].push_back(cnt);
        num_pqueue.push(make_tuple(val, num_count[val], cnt));
    }
    
    int pop() {
        auto t = num_pqueue.top();
        auto [val, count, index] = t;
        num_pqueue.pop();
        while (!num_pqueue.empty() && t == num_pqueue.top()) {
            t = num_pqueue.top();
            num_pqueue.pop();
        }
        num_count[val] -= 1;
        num_index[val].pop_back();
        if (num_count[val] > 0) {
            num_pqueue.push(make_tuple(val, num_count[val], 
                num_index[val][num_index[val].size()-1]));
        }
        return val;
    }
};

//官方思路：对每个频次分别建一个栈，每次优先弹最高频次的栈，最高频次的栈弹完之后，再弹下一个栈
class FreqStack1 {
public:
    FreqStack1() {
        maxFreq = 0;
    }

    void push(int val) {
        freq[val]++;
        group[freq[val]].push(val);
        maxFreq = max(maxFreq, freq[val]);
    }

    int pop() {
        int val = group[maxFreq].top();
        freq[val]--;
        group[maxFreq].pop();
        if (group[maxFreq].empty()) {
            maxFreq--;
        }
        return val;
    }

private:
    unordered_map<int, int> freq;
    unordered_map<int, stack<int>> group;
    int maxFreq;
};

int test_case1(){
    FreqStack test;
    test.push(5);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    test.push(7);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    test.push(5);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    test.push(7);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    test.push(4);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    test.push(5);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    cout << test.pop() << endl;
    cout << test.pop() << endl;
    cout << test.pop() << endl;
    cout << test.pop() << endl;
    cout << test.pop() << endl;
    cout << test.pop() << endl;
    cout << test.pop() << endl;
}

int test_case2(){
    FreqStack test;
    test.push(4);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    test.push(0);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    test.push(9);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    test.push(3);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    test.push(4);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    test.push(2);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    cout << test.pop() << endl;
    test.push(6);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
    cout << test.pop() << endl;
    test.push(1);
    cout << get<0>(test.num_pqueue.top()) << " " << get<1>(test.num_pqueue.top()) << " " << get<2>(test.num_pqueue.top()) << endl;
}

int main() {
    test_case2();
}