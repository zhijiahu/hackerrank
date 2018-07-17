
#include <iostream>

class Enhanced
{
    virtual void method() {std::cout << "from Enhanced" << std::endl;}
public:
    virtual ~Enhanced() {method();}
    void baseMethod() {method();}
};
class Final : public Enhanced
{
    void method() {std::cout << "from Final" << std::endl;}
public:
    ~Final() {method();}
};


int* foo()
{
    int x=2;
    return &x;
}

int main()
{
    Enhanced* instance = new Final;
    instance->baseMethod();
    delete instance;

    int* f = foo();
    std::cout << f << std::endl;
}
