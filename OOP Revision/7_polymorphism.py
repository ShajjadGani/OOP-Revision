# compileTime-> static binding-> early binding->overloading
# runtime-> dynamic binding -> late binding -> overriding

class Calculator:
    def add(self,a,b,c=-1):
        if c==-1:
            return a+b
        return a+b+c
    
c = Calculator()
print(c.add(2,3))
print(c.add(2,3,5))


=====================================================================================
#C++
#include <iostream>
using namespace std;

class Calculator {
public:
    int add(int a, int b, int c = -1) {
        if (c == -1) {
            return a + b;
        }
        return a + b + c;
    }
};

int main() {
    Calculator c;

    cout << c.add(2, 3) << endl;
    cout << c.add(2, 3, 5) << endl;

    return 0;
}
