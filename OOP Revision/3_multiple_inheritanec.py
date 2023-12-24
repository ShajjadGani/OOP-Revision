# employee -> employe
#     name,age -> person
#     company name,location -> company

class Person:
    def __init__(self,pname,age) -> None:
        self.pname = pname
        self.age = age
    def details(self):
        print("Name = ",self.pname," Age=", self.age)

class Company:
    def __init__(self,cname,location) -> None:
        self.cname = cname
        self.location = location
    def details(self):
        print("Company Name = ",self.cname," location=", self.location)


class Employee(Person,Company):
    def __init__(self,pname,age, cname, location) -> None:
        Company.__init__(self,cname,location)
        Person.__init__(self,pname,age)
        


empObj = Employee("Salauddin",27,"Google","USA")
empObj.details()


===============================================================================
#C++
""" 1. In C++, Function name must be different in diffent class. Otherwise if there has same named function 
and we want to access them; then Get Ambigious Message. """
#include <iostream>
#include <string>
using namespace std;

class Person {
public:
    Person(const string& pname, int age) : pname(pname), age(age) {}

    void detail() {
        cout << "Name = " << pname << " Age = " << age << endl;
    }

private:
    string pname;
    int age;
};

class Company {
public:
    Company(const string& cname, const string& location) : cname(cname), location(location) {}

    void details() {
        cout << "Company Name = " << cname << " Location = " << location << endl;
    }

private:
    string cname;
    string location;
};

class Employee : public Person, public Company {
public:
    Employee(const string& pname, int age, const string& cname, const string& location)
        : Person(pname, age), Company(cname, location) {}
};

int main() {
    Employee empObj("Salauddin", 27, "Google", "USA");
    empObj.detail();

    return 0;
}