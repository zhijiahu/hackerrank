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

int main()
{
	// Widget w;
    // cout << "=========" << endl;

	// Widget ww(w);
    // cout << "=========" << endl;

    Widget www(Widget());
    cout << "=========" << endl;

    vector<int> v{true, true, false, false};
    for (auto&& x: v) // must be &&, otherwise it will try to init to non-const
    {
        x = true;
        cout << x;
    }


	return 0;
}
