## 15 Must-Know OOP Questions

### 1. What is the programming paradigm? It’s type and example.
- Programming Paradigm is a way to structure code. There are 3 type of it
- Monolithic programming: Writing an entire program in one big module/structure. used in old web applications.
- Procedural programming: Writing code as a sequence of step-by-step instructions with functions. C, PHP
- Object Oriented Programming(OOP): modern way to code. Used in Python, Java, C++

### 2. What is OOP? Why do we use it? What are the 4-pillers of oop?
`==>` OOP is a way of coding using class, object and real world concepts.
`==>` It makes code reusable, maintainable, secure and facilitate team collaboration through well defined structure.
`==>` 4-pillars of OOP are Abstraction, Polymorphism, Inheritance & Encapsulation. Technique: A-PIE

3. What is class, object and Singleton class?
⇒ class is the blueprint or template for creating objects.
⇒ Object is the instance of class. We can create objects with different name from the same class.
⇒ Singleton Class: A class designed to allow only one object to ever exist.
4. What is the method? Difference between method(function) overriding and overloading?
⇒ The function which is written inside the class is called a method.
⇒ When a child class implements a method which is already defined in its parent class it is called method overriding.
⇒ Overloading:  In the same class defining multiple methods with the same name but different parameters.

5. What is Constructor and Destructor? Can you override or overload them?
⇒ Constructor is a special type of  method(__init__) that runs when an object is created. Used to initialize values/parameters during the creation of objects.
⇒ Destructor is a method(__del__) that runs when an object is destroyed. Used to clean up resources.

⇒ In python, we cannot override or overload the constructor like normal methods.
⇒ We can override the destructor because the child class can define its own destructure.   but we cannot overload the destructor. 

6. What is Inheritance? Explain the type of Inheritance.
⇒ Inheritance is a technique which allows a child class to use the properties and methods of its parent class.
Single Inheritance: The child class inherits only one parent.
Multiple Inheritance:The child class inherits multiple parents.
Multilevel Inheritance: A child inherits from a parent, which itself inherits from another parent.
Hierarchical Inheritance: Multiple children inherit from one parent.
Hybrid Inheritance: Combination of two or more types of inheritance.


7. What is Polymorphism? Explain its type.
⇒ The word Polymorphism means "many forms" and it refers to the ability of methods/functions with the same name that can be executed on many forms. For example: the len function of python is also a polymorphic function as we know that through the  len function we can find the length of different datatypes like: size of  list, string, set etc.

There are 2 type of polymorphism:
⇒ Run-time polymorphism: method overriding is a runtime polymorphism.
⇒ Compile-time polymorphism: method overloading is a compile-time polymorphism.

⇒ Compile-time: The time when the code is translated into machine language by the compiler.
⇒ Run-time: When the code is running. 
⇒ When we write code and execute it. The compiler translates it into machine language first then the code runs. For this reason, those codes which are executed in compile-time are fast or executed first. Then the run-time code.


8. What is Abstraction? Abstract class? Abstract method? Can an abstract class have a constructor? Can we instantiate abstract class? What is the super() keyword used for?
Difference between Abstract class and interface.
⇒ Abstraction hides implementation details and shows only what is needed.  
⇒ An Abstract method is a function which is empty or not implemented yet. 
⇒ An Abstract class is a class which has at least one abstract method. The abstract class forces  all of its child classes to implement this empty method.If the child class implements the abstract method they can use the properties and methods of the abstract class.
⇒ Yes. An abstract class can have a constructor.
⇒ Instantiate abstract class means to create objects from abstract class directly.
⇒ No. We cannot instantiate abstract classes. We must create a child class and implement all the abstract methods in it then we can create objects from the child class.
⇒ The super() keyword is used to call the parent classes properties,  methods and constructors.
⇒ The Abstract class can contain abstract methods, normal methods and constructors.
⇒ But the interface only contains the abstract class. No constructor or other methods.

9. What is Encapsulation? Type? What access modifiers commonly used in encapsulation.
⇒ Before we learn  Encapsulation, We should know one thing and that is
			“Nothing is Strictly Private in Python”
In fact, the private value in encapsulation is also accessible by the help of some technique. 🙂

Encapsulation is a technique to prevent misuse and restrict direct access of data from outside by using public, protected and private modes.
public ⇒ The properties and methods are Accessible anywhere.
Protected ⇒ Accessible within class and subclasses. Defined by _single underscore.
private ⇒ Accessible only within class. Defined by __double underscore.  

Two common access modifiers method are:
⇒ Getter: Method to read private/protected data
⇒ Setter: Method to modify private/protected data safely

10. Two major differences between Abstraction and Encapsulation.
Abstraction
Encapsulation
⇒ Abstraction hides implementation details(properties, methods etc.) and shows what is only necessary.
⇒ Encapsulation prevents misuse of data and restricts direct access of data from outside(object).
⇒ it’s achieved using abstract class, abstract methods and interface.
⇒ it’s achieved using public, protected, private mode and getter, setter method.



11. What is exception handling?
⇒ A mechanism to handle errors that occur during program execution, so the program doesn’t crash.
Exception handling in python try…except…finally.  In javascript try…catch…finally
try:					⇐ code that may cause an error
    x = 10 / 0
except:					⇐ code that handle error
    print("Cannot divide by zero")
finally:					⇐ finally always run (it’s optional)
    print("This always runs")



12. What is coupling? Why is it important?
Coupling refers to how much one class depends on another. There are 2 type of it
⇒ Tightly coupled: Classes depend heavily on each other → hard to maintain.
⇒ Loosely coupled: Classes depend minimally → easy to maintain.
Importance:
⇒ Reduces dependency between classes.
⇒ Makes code more flexible, reusable, and maintainable.

13.  What is structure? Difference between structure and class.
⇒ A structure is a collection of variables of different data types grouped together under one name.
struct Student {
    string name;
    int age;
    float marks;
};
⇒ structure is  public, can have functions and has limited OOP features.
⇒ class supports all oop features and can have function, constructor and destructor.

14.  What are two major disadvantages of OOP?
⇒ Performance Overhead: Objects and method calls take more memory and processing, making OOP slower than procedural programming in some cases.
⇒ Complexity: OOP programs can become large and complicated, especially with many classes and inheritance.
