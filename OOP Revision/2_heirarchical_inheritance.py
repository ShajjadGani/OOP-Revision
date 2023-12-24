# Cat-> sound + eat

class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def eat(self):
        print(f"{self.name} can eat")

class Cat(Animal):
    def __init__(self,name) -> None:
        # super().__init__(name)
        Animal.__init__(self,name)
    # def eat(self):
    #     print(f"{self.name} can eat")
    def sound(self):
        print(self.name," sounds like Meeow!")
    
    def __repr__(self) -> str:
        return f"{self.name} class"

class Dog(Animal):
    # def __init__(self,name) -> None:
    #     self.name = name
    # def eat(self):
    #     print(f"{self.name} can eat")
    def sound(self):
        print(self.name," sounds like Bark!")


c = Cat("Cat")
c.eat()
d = Dog("Dog")
d.eat()

print(c)



=======================================================================================
#In C++

class Animal {
public:
    Animal(const string& name) : name(name) {} #Constructor

    void eat() const {
        cout << name << " can eat" << endl;
    }

protected:
    string name;
};

class Cat : public Animal {
public:
    Cat(const string& name) : Animal(name) {} #Constructor

    void sound() const {
        cout << name << " sounds like Meeow!" << endl;
    }
};

class Dog : public Animal {
public:
    Dog(const string& name) : Animal(name) {} #Constructor

    void sound() const {
        cout << name << " sounds like Bark!" << endl;
    }
};

int main() {
    Cat("Cat").eat();
    Dog("Dog").eat();

    return 0;
}