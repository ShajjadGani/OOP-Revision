# senior-> Project->Database
#           |
# dekstop         mobile
# login           login


from abc import ABC,abstractmethod
class Project(ABC):
    def details(self):
        self.balance =50
        print("I am core project")
    @abstractmethod
    def security(self):
        pass
class App(Project):
    def security():
        pass
    def details(self):
        print("I am from app")

b = Project()
print(b.balance)


============================================================
#C++
#include <iostream>
using namespace std;
class Project {
public:
    Project() : balance(50) {}

    virtual void details() {
        balance = 50;
        cout << "I am core project" << endl;
    }

    virtual void security() = 0;  // Pure virtual function

    int getBalance() const {
        return balance;
    }

private:
    int balance;
};

class App : public Project {
public:
    void security() override {
        // Implementation of the pure virtual function
    }

    void details() override {
        cout << "I am from app" << endl;
    }
};

int main() {
    Project* b = new App();
    b->details();

    cout << "Balance: " << b->getBalance() << endl;

    delete b;

    return 0;
}

""" 1. Virtal Keyword is mainly used in the context of polymorphism, specifically for virtual functions & virtual inheritance.
   
     2. Declare a function as virtual in a base class, this indicate to the compiler that this function may be overridden by derived classes. This enables dynamic dispatch, allowing the correct function to be called based on the actual type of the object at runtime.
"""