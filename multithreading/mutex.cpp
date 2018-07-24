
#include <iostream>
#include <vector>
#include <thread>
using namespace std;

int accum = 0;

void square(int x) {
    std::thread::id this_id = std::this_thread::get_id();

    cout << "thread " << this_id << " start..." << endl;
    cout << "current accum = " << accum << endl;
    accum += x * x;
    cout << "thread " << this_id << " end "<< endl;
}

int main() {
    vector<thread> ths;
    for (int i = 1; i <= 1000; i++) {
        ths.push_back(thread(&square, i));
    }

    for (auto& th : ths) {
        th.join();
    }
    cout << "accum = " << accum << endl;
    return 0;
}
