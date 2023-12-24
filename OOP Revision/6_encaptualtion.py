# public -
# private - 
# protected - flexibilaty

class Person:
    def __init__(self,name) -> None:
        self.name = name
        self._amount = 50
    def details(self):
        print("Name=",self.name," Amount=",self._amount)


p = Person("Asad")
# print("Before change")
# p.details()

# p.__amount = 0
# print("After change")
# p.details()

# print(p.__dict__)

print(p._amount)



=======================================================================
#C++
#include <iostream>
#include <string>
using namespace std; 

class Person {
public:
    Person(const string& name) : name(name), amount(50) {}

    void details() const {
        cout << "Name = " << name << " Amount = " << amount << endl;
    }

    int getAmount() const {
        return amount;
    }

private:
    string name;
    int amount;
};

int main() {
    Person p("Asad");

    // Accessing the amount using a public getter method
    cout << "Amount = " << p.getAmount() << endl;

    return 0;
}