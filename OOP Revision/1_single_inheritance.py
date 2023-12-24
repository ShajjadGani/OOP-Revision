# Cat-> sound + eat

class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def eat(self):
        print(self.name," can eat")

class Cat(Animal):
    def sound(self):
        print(self.name," sounds like meow")
    def __repr__(self) -> str:
        return "I am cat class"

cat = Cat("Cat")
# cat.sound()
print(cat)


#C++ Syntax
// Base class
class Animal {
  public:
    string animal_name = "Cat";
};

// Derived class
class Cat: public Animal {
  public:
    string sound = "Meow Meow";
};

int main() {
  Cat myAnimal;
  cout << myAnimal.animal_name + " " + myAnimal.sound;
  return 0;
}