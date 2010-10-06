compile:
	mkdir -p bin
	g++ src/main.cpp `wx-config --libs` `wx-config --cxxflags` -Wall -o bin/main

run: compile
	bin/main
