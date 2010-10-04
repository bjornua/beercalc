compile:
	mkdir -p bin
	g++ main.cpp `wx-config --libs` `wx-config --cxxflags` -o bin/main

run: compile
	bin/main