// cpp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>

using namespace std;

class Widget
{
public:
	Widget() { cout << "1" << endl; }
	Widget(const Widget&) { cout << "2" << endl; }
	Widget(Widget&&) { cout << "3" << endl; }
};


int main()
{
	Widget w;
	Widget ww(Widget{});


	cout << "test" << endl;

	return 0;
}