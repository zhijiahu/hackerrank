// cpp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <vector>

using namespace std;

class Widget
{
public:
	Widget() { cout << "1"; }
	Widget(const Widget&) { cout << "2"; }
	Widget(Widget&&) { cout << "3"; }
};

Widget GetWidget()
{
	Widget w;
	return w;
}

int main()
{
	/*Widget w;
	Widget ww(Widget{}); */

	Widget w;
	Widget ww(GetWidget());

    vector<int> v{true, true, false, false};
    for (auto&& x: v) // must be &&, otherwise it will try to init to non-const
    {
        x = true;
        cout << x;
    }

	// std::vector<int> v{ 1, 2, 3, 4, 5 };
	// for (auto&& x : v)
	// {
	// 	x *= 2;
	// 	std::cout << x;
	// }

	return 0;
}
