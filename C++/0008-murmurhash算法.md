```c++
#include <iostream>
#include <stdio.h>
#include <string.h>
#define  uint64_t unsigned long long

using namespace std;

long long getHashVal(char* instr_c)
{
    string instr = string(instr_c);
    cout << instr << endl;
    const uint64_t seed =  0x1234ABCD;
    const uint64_t m = 0xc6a4a7935bd1e995;
    const int r = 47;

    uint64_t h = seed ^ (instr.length() * m);

    const uint64_t *data = (const uint64_t *)instr.c_str();
    const uint64_t *end = data + (instr.length()/8);

    while(data != end)
    {
       uint64_t k = *data++;

       k *= m;
       k ^= k >> r;
       k *= m;

       h ^= k;
	   h *= m;
    }

    const unsigned char * data2 = (const unsigned char*)data;

    switch(instr.length() & 7)
    {
        case 7: h ^= (uint64_t)(data2[6]) << 48;
        case 6: h ^= (uint64_t)(data2[5]) << 40;
        case 5: h ^= (uint64_t)(data2[4]) << 32;
		case 4: h ^= (uint64_t)(data2[3]) << 24;
        case 3: h ^= (uint64_t)(data2[2]) << 16;
        case 2: h ^= (uint64_t)(data2[1]) << 8;
        case 1: h ^= (uint64_t)(data2[0]);
                h *= m;
    };

    h ^= h >> r;
    h *= m;
    h ^= h >> r;

    return h;
}

int main(int argc, char *argv[]) {
    if(argc != 2) {
	printf("please give a str to hash, no more no less\n");
    } else {
	long long ret = getHashVal(string(argv[1]));
	cout << ret << endl;
    }
    return 0;
}
```

编译python可以使用的so库
```c++
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <Python.h>
#include <sstream>
#define  uint64_t unsigned long long

using namespace std;

extern "C" {

long long getHashVal(char* instr_c)
{
    string instr = string(instr_c);
    const uint64_t seed =  0x1234ABCD;
    const uint64_t m = 0xc6a4a7935bd1e995;
    const int r = 47;

    uint64_t h = seed ^ (instr.length() * m);

    const uint64_t *data = (const uint64_t *)instr.c_str();
    const uint64_t *end = data + (instr.length()/8);

    while(data != end)
    {
       uint64_t k = *data++;

       k *= m;
       k ^= k >> r;
       k *= m;

       h ^= k;
	   h *= m;
    }

    const unsigned char * data2 = (const unsigned char*)data;

    switch(instr.length() & 7)
    {
        case 7: h ^= (uint64_t)(data2[6]) << 48;
        case 6: h ^= (uint64_t)(data2[5]) << 40;
        case 5: h ^= (uint64_t)(data2[4]) << 32;
		case 4: h ^= (uint64_t)(data2[3]) << 24;
        case 3: h ^= (uint64_t)(data2[2]) << 16;
        case 2: h ^= (uint64_t)(data2[1]) << 8;
        case 1: h ^= (uint64_t)(data2[0]);
                h *= m;
    };

    h ^= h >> r;
    h *= m;
    h ^= h >> r;

    return h;
}

}
```