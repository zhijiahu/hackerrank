
#include <string.h>
#include <iostream>


char* alloc_copy(const char* str)
{
    char* r = new char[strlen(str)+1];
    char* result = r;

    while(*str != '\0')
    {
        *r = *str;
        r++;
        str++;
    }

    return result;
}


int main()
{
    const char* s1 = "Hello";
    const char* s2 = alloc_copy(s1); // memory leak

    std::cout << s1 << std::endl;
    std::cout << s2 << std::endl;
}
