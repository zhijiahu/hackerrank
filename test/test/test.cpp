// test.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include <vector>
#include <iostream>

class Enhanced
{
    virtual void method() { std::cout << "from Enhanced" << std::endl; }
public:
    virtual ~Enhanced() { method(); }
    void baseMethod() { method(); }
};
class Final : public Enhanced
{
    void method() { std::cout << "from Final" << std::endl; }
public:
    ~Final() { method(); }
};


// int* foo()
// {
//     int x=2;
//     return &x;
// }

struct MyType { int x; };
struct Component {
    operator MyType() const { return *this; }
    int x;
};


int main()
{
    Enhanced* instance = new Final;
    instance->baseMethod();
    delete instance;

    std::vector<int> v = { 1,2 };
    v.reserve(5);
    //std::cout << v.at(4) << std::endl;

    Component c;
    MyType type = c;
    return 0;
}

