# GrandFather - 5 crore
#       |
# Father - 3 crore
#       |
# Ami - 2 crore


class GrandFather:
    def property(self):
        print("I have 5 crore taka")
    
class Father(GrandFather):
    def property(self):
        print("I have 3 crore taka")
    def father(self):
        super().property()

class Child(Father):
    def property(self):
        print("I have 2 crore taka")
    def father(self):
        super().property()
    def grandFather(self):
        super().father()

ami = Child()
ami.property()
ami.father()
ami.grandFather()


========================================================================================
#C++
#include <iostream>
using namespace std;

class GrandFather {
public:
    void property() {
        cout << "I have 5 crore taka" << endl;
    }
};

class Father : public GrandFather {
public:
    void property() {
        cout << "I have 3 crore taka" << endl;
    }

    void father() {
        GrandFather::property();
    }
};

class Child : public Father {
public:
    void property() {
        cout << "I have 2 crore taka" << endl;
    }

    void father() {
        Father::property();
    }

    void grandFather() {
        Father::father();
    }
};

int main() {
    Child ami;
    ami.property();
    ami.father();
    ami.grandFather();

    return 0;
}