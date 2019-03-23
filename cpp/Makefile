
CXX = g++
CXXFLAGS += -std=c++11

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
project_path := $(dir $(mkfile_path))

build: ensure-bin main

main: move.cpp
	$(CXX) $^ -o $(project_path)bin/$@

ensure-bin:
	-mkdir -p $(project_path)bin

clean:
	-rm -r $(project_path)bin
	-rm *.o
