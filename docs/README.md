<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q1)  WAP to print the size (in bytes) and range (smallest & largest) of all primitive data types available in JAVA


<br>

## CODE

```java
class Main {
    public static void main(String[] args) {
        System.out.println("Size of byte: " + Byte.BYTES + " bytes");
        System.out.println("Range of byte: " + Byte.MIN_VALUE + " to " + Byte.MAX_VALUE);

        System.out.println("\nSize of short: " + Short.BYTES + " bytes");
        System.out.println("Range of short: " + Short.MIN_VALUE + " to " + Short.MAX_VALUE);

        System.out.println("\nSize of int: " + Integer.BYTES + " bytes");
        System.out.println("Range of int: " + Integer.MIN_VALUE + " to " + Integer.MAX_VALUE);

        System.out.println("\nSize of long: " + Long.BYTES + " bytes");
        System.out.println("Range of long: " + Long.MIN_VALUE + " to " + Long.MAX_VALUE);

        System.out.println("\nSize of float: " + Float.BYTES + " bytes");
        System.out.println("Range of float: " + Float.MIN_VALUE + " to " + Float.MAX_VALUE);

        System.out.println("\nSize of double: " + Double.BYTES + " bytes");
        System.out.println("Range of double: " + Double.MIN_VALUE + " to " + Double.MAX_VALUE);

        System.out.println("\nSize of char: " + Character.BYTES + " bytes");
        System.out.println("Range of char: " + (int) Character.MIN_VALUE + " to " + (int) Character.MAX_VALUE);

        System.out.println("\nSize of boolean: 1 bit");
        System.out.println("Range of boolean: " + Boolean.FALSE + " to " + Boolean.TRUE);
    }
}
```

<br>

## OUTPUT

<center>

![1.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/1.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q2)  WAP to demonstrate the use of arithmetic and bitwise operators


<br>

## CODE

```java
class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        int c;

        System.out.println("a = " + a + " | b = " + b);

        c = a + b;
        System.out.println("a + b = " + c);
        c = a - b;
        System.out.println("a - b = " + c);
        c = a * b;
        System.out.println("a * b = " + c);
        c = a / b;
        System.out.println("a / b = " + c);
        c = a % b;
        System.out.println("a % b = " + c);
        c = a & b;
        System.out.println("a & b = " + c);
        c = a | b;
        System.out.println("a | b = " + c);
        c = a ^ b;
        System.out.println("a ^ b = " + c);
        c = ~a;
        System.out.println("~a = " + c);
        c = a << 2;
        System.out.println("a << 2 = " + c);
        c = a >> 2;
        System.out.println("a >> 2 = " + c);
        c = a >>> 2;
        System.out.println("a >>> 2 = " + c);
    }
}
```

<br>

## OUTPUT

<center>

![2.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/2.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q3)  WAP to print all the prime numbers within a range (e.g. 1 to 100)


<br>

## CODE

```java
import java.util.ArrayList;

class Main {
    public static boolean isPrime(int n) {
        boolean ret = true;
        for (int i = 2; i <= n/2; i++) {
            if (n % i == 0) {
                ret = false;
                break;
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        ArrayList<Integer> primes = new ArrayList<Integer>();
        for (int i = 2; i <= 100; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }

        System.out.println("Prime numbers between 1 and 100:");
        for (int i : primes) {
            System.out.print(i + " ");
        }
    }
}
```

<br>

## OUTPUT

<center>

![3.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/3.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q4)  WAP declaring a class Rectangle with data member’s length and breadth and member functions Input, Output and CalcArea


<br>

## CODE

```java
import java.util.Scanner;

class Rectangle {
    int length;
    int breadth;

    public void Input() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter length: ");
        length = sc.nextInt();
        System.out.print("Enter breadth: ");
        breadth = sc.nextInt();
        sc.close();
    }

    public void Output() {
        System.out.println("Length: " + length);
        System.out.println("Breadth: " + breadth);
    }

    public void CalcArea() {
        System.out.println("Area: " + length * breadth);
    }
}

class Main {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.Input();
        System.out.println();
        r.Output();
        r.CalcArea();
    }
}
```

<br>

## OUTPUT

<center>

![4.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/4.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q5)  Write a program to remove duplicates from sorted array


<br>

## CODE

```java
import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        int[] arr = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5};
        ArrayList<Integer> unique = new ArrayList<Integer>();

        System.out.println("Original array:");
        for (int i : arr) {
            System.out.print(i + " ");
        }
        
        for (int i : arr) {
            if (!unique.contains(i)) {
                unique.add(i);
            }
        }

        System.out.println("\n\nUnique elements:");
        for (int i : unique) {
            System.out.print(i + " ");
        }
    }
}
```

<br>

## OUTPUT

<center>

![5.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/5.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q6)  WAP to calculate first n Fibonacci numbers and store in an array


<br>

## CODE

```java
import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        int n = 10;
        ArrayList<Integer> fib = new ArrayList<Integer>();
        fib.add(0);
        fib.add(1);
        for (int i = 2; i < n; i++) {
            fib.add(fib.get(i-1) + fib.get(i-2));
        }

        System.out.println("First " + n + " Fibonacci numbers:");
        for (int i : fib) {
            System.out.print(i + " ");
        }
    }
}
```

<br>

## OUTPUT

<center>

![6.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/6.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q7)  WAP to demonstrate use of method overloading to calculate area of square, rectangle and triangle


<br>

## CODE

```java
class Main {
    static double area(int side) {
        return side * side;
    }

    static double area(int length, int breadth) {
        return length * breadth;
    }

    static double area(int base, double height) {
        return 0.5 * base * height;
    }

    public static void main(String[] args) {
        System.out.println("Area of square with side 5: " + area(5));
        System.out.println("Area of rectangle with length 5 and breadth 10: " + area(5, 10));
        System.out.println("Area of triangle with base 5 and height 10: " + area(5, 10.0));
    }
}
```

<br>

## OUTPUT

<center>

![7.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/7.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q8)  WAP that makes use of String class methods


<br>

## CODE

```java
class Main {
    public static void main(String[] args) {
        String x = "Hello World";

        System.out.println(x); // Hello World
        System.out.println(x.length()); // 11
        System.out.println(x.toUpperCase()); // HELLO WORLD
        System.out.println(x.toLowerCase()); // hello world
        System.out.println(x.indexOf("World")); // 6
        System.out.println(x.indexOf("world")); // -1
        System.out.println(x.substring(6)); // World
        System.out.println(x.substring(6, 8)); // Wo
        System.out.println(x.replace("World", "Universe")); // Hello Universe
        System.out.println(x.replace("world", "Universe")); // Hello World
        System.out.println(x.concat("!!!")); // Hello World!!!
        System.out.println(x + "!!!"); // Hello World!!!
        System.out.println(x.charAt(1)); // e
        System.out.println(x + 14); // Hello World14
        System.out.println(14 + x); // 14Hello World
        System.out.println(String.format("Hello %s", "World")); // Hello World
       
        String[] y = x.split("r");
        System.out.println(y[0]); // Hello Wo
        System.out.println(y[1]); // ld
    }
}
```

<br>

## OUTPUT

<center>

![8.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/8.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q9)  WAP that makes use of StringBuffer class methods


<br>

## CODE

```java
class Main {
    public static void main(String[] args) {
        StringBuffer x = new StringBuffer("Hello World");

        System.out.println(x); // Hello World
        System.out.println(x.length()); // 11
        System.out.println(x.capacity()); // 16
        System.out.println(x.reverse()); // dlroW olleH
        System.out.println(x.append("!!!")); // dlroW olleH!!!
        System.out.println(x.insert(5, "!!!")); // dlroW!!! olleH!!!
        System.out.println(x.delete(5, 8)); // dlroW olleH!!!
        System.out.println(x.deleteCharAt(5)); // dlro olleH!!!
        System.out.println(x.replace(5, 8, "!!!")); // dlro!!! olleH!!!
        System.out.println(x.substring(5)); // !!! olleH!!!
        System.out.println(x.substring(5, 8)); // !!!
        System.out.println(x.indexOf("olleH")); // 8
        System.out.println(x.indexOf("olleh")); // -1
        System.out.println(x.charAt(5)); // !
        System.out.println(String.format("Hello %s", "World")); // Hello World
    }
}
```

<br>

## OUTPUT

<center>

![9.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/9.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q10)  WAP to demonstrate the use of static variable, static method and static block


<br>

## CODE

```java
class StaticStuff {
    static int x = 10;
    static int y = 20;

    static {
        System.out.println("StaticStuff has been loaded");
    }

    static void print() {
        System.out.println("x = " + x + " | y = " + y);
    }
}

class Main {
    public static void main(String[] args) {
        StaticStuff.print();
    }
}
```

<br>

## OUTPUT

<center>

![10.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/10.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q11)  WAP to demonstrate concept of `this`


<br>

## CODE

```java
class MyClass {
    int x;
    int y;

    MyClass(int x, int y) {
        this.x = x;
        this.y = y;
    }

    void print() {
        System.out.println("x = " + this.x + " | y = " + this.y);
    }
}

class Main {
    public static void main(String[] args) {
        MyClass obj = new MyClass(10, 20);
        obj.print();
    }
}
```

<br>

## OUTPUT

<center>

![11.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/11.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q12)  WAP to demonstrate multi-level and hierarchical inheritance


<br>

## CODE

```java

// Multilevel
class A {
    void printA() {System.out.println("A");}
}
class B extends A {
    void printB() {System.out.println("B");}
}
class C extends B {
    void printC() {System.out.println("C");}
}

// Hierarchical
class D {
    void printD() {System.out.println("D");}
}
class E extends D {
    void printE() {System.out.println("E");}
}
class F extends D {
    void printF() {System.out.println("F");}
}


class Main {
    public static void main(String[] args) {
        C obj1 = new C();
        obj1.printA();
        obj1.printB();
        obj1.printC();

        System.out.println();

        E obj2 = new E();
        obj2.printD();
        obj2.printE();

        System.out.println();

        F obj3 = new F();
        obj3.printD();
        obj3.printF();
    }
}

```

<br>

## OUTPUT

<center>

![12.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/12.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q13)  WAP to use super() to invoke base class constructor


<br>

## CODE

```java
class Base {
    int x;
    Base(int x) {
        this.x = x;
        System.out.println("Base class constructor");
    }
}

class Derived extends Base {
    int y;
    Derived(int x, int y) {
        super(x);
        this.y = y;
        System.out.println("Derived class constructor");
    }
}

class Main {
    public static void main(String[] args) {
        Derived obj = new Derived(10,20);
        System.out.println("x = " + obj.x + " | y = " + obj.y);
    }
}
```

<br>

## OUTPUT

<center>

![13.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/13.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q14)  WAP to demonstrate run-time polymorphism


<br>

## CODE

```java
class Animal {
    public void sleep() {
        System.out.println("Animal is sleeping");
    }
}

class Cat extends Animal {
    @Override
    public void sleep() {
        System.out.println("Cat is sleeping");
    }
}

class Main {
    public static void main(String[] args) {
        Animal obj = new Cat();
        obj.sleep();
    }
}
```

<br>

## OUTPUT

<center>

![14.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/14.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q15)  WAP to implement abstract classes


<br>

## CODE

```java
abstract class Animal {
    abstract void sleep();
}

class Cat extends Animal {
    @Override
    void sleep() {
        System.out.println("Cat is sleeping");
    }
}

class Main {
    public static void main(String[] args) {
        Animal obj = new Cat();
        obj.sleep();
    }
}
```

<br>

## OUTPUT

<center>

![15.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/15.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q16)  WAP to demonstrate the concept of interface when two interfaces have unique methods and same data members


<br>

## CODE

```java
interface Interface1 {
    int x = 10;
    void print1();
}

interface Interface2 {
    int x = 20;
    void print2();
}


class Main implements Interface1, Interface2 {
    @Override
    public void print1() {
        System.out.println("x = " + Interface1.x);
    }

    @Override
    public void print2() {
        System.out.println("x = " + Interface2.x);
    }

    public static void main(String[] args) {
        Main obj = new Main();
        obj.print1();
        obj.print2();
    }
}
```

<br>

## OUTPUT

<center>

![16.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/16.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q17)  WAP to demonstrate checked exception during file handling


<br>

## CODE

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        try {
            File file = new File("file.txt");
            Scanner scanner = new Scanner(file);
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }
    }
}
```

<br>

## OUTPUT

<center>

![17.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/17.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q18)  Write a program to demonstrate unchecked exception


<br>

## CODE

```java
class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 0;
        int c;

        try {
            c = a / b;
            System.out.println("a / b = " + c);
        } catch (ArithmeticException e) {
            System.out.println("Division by zero");
        }
    }
}
```

<br>

## OUTPUT

<center>

![18.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/18.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q19)  WAP to demonstrate the concept of user defined exceptions


<br>

## CODE

```java
class MyException extends Exception {
    MyException(String message) {
        super(message);
    }
}

class Main {
    public static void main(String[] args) {
        try {
            throw new MyException("This is a user defined exception");
        } catch (MyException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

<br>

## OUTPUT

<center>

![19.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/19.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q20)  WAP to input salary of a person along with his name, if the salary is less than 85,000 then throw an arithmetic exception with a proper message "not eligible for loan"


<br>

## CODE

```java
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter name: ");
        String name = sc.nextLine();

        System.out.print("Enter salary: ");
        int salary = sc.nextInt();
        
        sc.close();

        if (salary < 85000) {
            throw new ArithmeticException(name + " is not eligible for loan");
        }
    }
}
```

<br>

## OUTPUT

<center>

![20.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/20.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q21)  WAP to demonstrate creation of multiple child threads


<br>

## CODE

```java
class MyRunnable implements Runnable {
    Thread t;
    String name;

    MyRunnable(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        System.out.println(this.name + " has started");
        try {Thread.sleep(1000);}
        catch (InterruptedException e) {}
        System.out.println(this.name + " has finished");
    }
}


class Main {
    public static void main(String[] args) {
        System.out.println("Main thread has started");

        MyRunnable r1 = new MyRunnable("Thread 1");
        MyRunnable r2 = new MyRunnable("Thread 2");
        MyRunnable r3 = new MyRunnable("Thread 3");

        Thread t1 = new Thread(r1);
        Thread t2 = new Thread(r2);
        Thread t3 = new Thread(r3);
        
        t1.start();
        t2.start();
        t3.start();

        System.out.println("Main thread has finished");
    }
}
```

<br>

## OUTPUT

<center>

![21.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/21.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q22)  WAP that has two threads where one thread prints table of 5 and other thread prints a string 10 times. Set and display the names and priorities of these threads


<br>

## CODE

```java

class Thread1 extends Thread {
    public void run() {
        for (int i = 1; i <= 10; i++) {
            try   {Thread.sleep(500);}
            catch (InterruptedException e) {}
            System.out.println("5 * " + i + " = " + 5*i);
        }
    }
}

class Thread2 extends Thread {
    public void run() {
        for (int i = 1; i <= 10; i++) {
            try   {Thread.sleep(500);}
            catch (InterruptedException e) {}
            System.out.println("Hello World");
        }
    }
}


class Main {
    public static void main(String[] args) {
        Thread1 t1 = new Thread1();
        Thread2 t2 = new Thread2();

        t1.setName("Table of 5");
        t2.setName("Hello World");

        t1.setPriority(Thread.MAX_PRIORITY);
        t2.setPriority(Thread.MIN_PRIORITY);

        t1.start();
        t2.start();

        System.out.println("Thread 1: " + t1.getName() + "  | Priority: " + t1.getPriority());
        System.out.println("Thread 2: " + t2.getName() +  " | Priority: " + t2.getPriority());
        System.out.println();
    }
}
```

<br>

## OUTPUT

<center>

![22.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/22.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q23)  WAP to create random access file and read & write integer data in it


<br>

## CODE

```java
import java.io.RandomAccessFile;

class Main {
    public static void main(String[] args) {
        try {
            RandomAccessFile file = new RandomAccessFile("file.txt", "rw");
            int x = 10;

            file.writeInt(x);
            file.seek(0);
            System.out.println(file.readInt());

            file.close();
        }
        catch (Exception e) {
            System.out.println("An error occurred");
        }
    }
}
```

<br>

## OUTPUT

<center>

![23.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/23.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q24)  WAP that writes student’s data (enrollment no, name, percentage, phone no.) to a file and then reads the student data back from that file and display it on the console. (Use BufferedInputStream and BufferedOuputStream)


<br>

## CODE

```java
import java.io.*;

class Student implements Serializable {
    int enrollmentNo;
    String name;
    double percentage;
    String phoneNo;

    Student(int enrollmentNo, String name, double percentage, String phoneNo) {
        this.enrollmentNo = enrollmentNo;
        this.name = name;
        this.percentage = percentage;
        this.phoneNo = phoneNo;
    }

    void display() {
        System.out.println("Enrollment No: " + enrollmentNo);
        System.out.println("Name: " + name);
        System.out.println("Percentage: " + percentage);
        System.out.println("Phone No: " + phoneNo);
    }
}


class Main {
    public static void main(String[] args) {
        try {
            String filename = "student.dat";
            Student student = new Student(198719342, "Ajay", 78.92, "9870081734");

            // Write student data to file
            FileOutputStream     file_out = new FileOutputStream(filename);
            BufferedOutputStream buff_out = new BufferedOutputStream(file_out);
            ObjectOutputStream   obj_out  = new ObjectOutputStream(buff_out);
            obj_out.writeObject(student);
            obj_out.close();

            // Read student data from file
            FileInputStream     file_inp = new FileInputStream(filename);
            BufferedInputStream buff_inp = new BufferedInputStream(file_inp);
            ObjectInputStream   obj_inp  = new ObjectInputStream(buff_inp);
            Student studentRead = (Student) obj_inp.readObject();
            obj_inp.close();
            
            studentRead.display();
        }
        
        catch (Exception e) {e.printStackTrace();}
    }
}
```

<br>

## OUTPUT

<center>

![24.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/24.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q25)  WAP that accept two file names as command line arguments. Copy only those lines from the first file to second file which contains the word “Computers”. Also count number of words in first file


<br>

## CODE

```java
import java.io.*;

class Main {
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(args[0]));
            BufferedWriter bw = new BufferedWriter(new FileWriter(args[1]));
            String line;

            int count = 0;
            while (true) {
                line = br.readLine();
                if (line == null) {break;}
                count += line.split(" ").length;

                if (line.contains("Computers")) {
                    bw.write(line);
                    bw.newLine();
                }
            }
            
            br.close();
            bw.close();
            System.out.println("Number of words in first file: " + count);
        }
        
        catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

<br>

## OUTPUT

<center>

![25.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/25.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q26)  WAP that take input from keyboard and write into a file using character stream


<br>

## CODE

```java
import java.io.*;

class Main {
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Please enter a line:");
            String line = br.readLine();
            br.close();
            
            BufferedWriter bw = new BufferedWriter(new FileWriter("output-26.txt"));
            bw.write(line);
            bw.close();
        }
        
        catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

<br>

## OUTPUT

<center>

![26.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/26.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q27)  WAP to use Byte stream class to read from a text file and display the content on the output screen


<br>

## CODE

```java
import java.io.*;

class Main {
    public static void main(String[] args) {
        try {
            FileInputStream fis = new FileInputStream("output-26.txt");
            int i;
            
            while (true) {
                i = fis.read();
                if (i == -1) {break;}
                System.out.print((char) i);
            }
            fis.close();
        }
        
        catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

<br>

## OUTPUT

<center>

![27.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/27.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q28)  WAP to use Byte stream class to read form a text file and copy the content to another text file


<br>

## CODE

```java
import java.io.*;

class Main {
    public static void main(String[] args) {
        try {
            FileInputStream  fis = new FileInputStream("output-26.txt");
            FileOutputStream fos = new FileOutputStream("output-28.txt");
            int i;
            
            while (true) {
                i = fis.read();
                if (i == -1) {break;}
                fos.write(i);
                System.out.print( (char)i );
            }
            
            fis.close();
            fos.close();
        }
        
        catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

<br>

## OUTPUT

<center>

![28.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/28.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q29)  WAP to demonstrate any event handling


<br>

## CODE

```java
import javax.swing.*;
import java.awt.event.*;

class Main {
    static int count = 0;

    public static void main(String[] args) {
        JFrame frame = new JFrame("Event Handling");
        frame.setSize(300, 100);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JButton button = new JButton("Click me");
        button.setBounds(100, 25, 100, 50);
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                count += 1;
                JOptionPane.showMessageDialog(null, "Button clicked " + count + " times");
            }
        });
        
        frame.add(button);
        frame.setLayout(null);
        frame.setVisible(true);
    }
}
```

<br>

## OUTPUT

<center>

![29.a.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/29.a.png)

![29.b.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/29.b.png)

![29.c.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/29.c.png)

![29.d.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/29.d.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q30)  Create Adapter class for mousemotion listener


<br>

## CODE

```java
import java.awt.event.*;
import javax.swing.*;
import java.awt.*;

class Main extends JFrame {
    private JLabel label;

    public Main() {
        label = new JLabel("Put your mouse here");

        label.setBackground(new Color(20, 20, 20));
        label.setForeground(new Color(255, 255, 255));
        label.setOpaque(true);

        label.addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseMoved(MouseEvent e) {
                label.setText("Mouse at: X:" + e.getX() + ", Y:" + e.getY());
            }
        });

        label.setHorizontalAlignment(JLabel.CENTER);
        label.setVerticalAlignment(JLabel.CENTER);
        setSize(300, 300);
        label.setBounds(10, 10, 280, 280);
        
        add(label);
        setLayout(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        new Main();
    }
}
```

<br>

## OUTPUT

<center>

![30.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/30.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q31) Write 4 different programs to implement all 4 layouts (Swings)

<br>

### Flow Layout

```java
import javax.swing.*;
import java.awt.*;

class Main extends JFrame {
    private JPanel panel = new JPanel(new FlowLayout());

    public Main() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        panel.add(new JButton("Button 1"));
        panel.add(new JButton("Button 2"));
        panel.add(new JButton("Button 3"));
        
        getContentPane().add(panel);
        setSize(300, 100);
        setVisible(true);
    }

    public static void main(String[] args) {
        new Main();
    }
}
```

<br>

### Border Layout

```java
import javax.swing.*;
import java.awt.*;

class Main extends JFrame {
    private JPanel panel = new JPanel(new BorderLayout());

    public Main() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        panel.add(new JButton("North"),  BorderLayout.NORTH);
        panel.add(new JButton("South"),  BorderLayout.SOUTH);
        panel.add(new JButton("East"),   BorderLayout.EAST);
        panel.add(new JButton("West"),   BorderLayout.WEST);
        panel.add(new JButton("Center"), BorderLayout.CENTER);
        
        getContentPane().add(panel);
        setSize(300, 200);
        setVisible(true);
    }

    public static void main(String[] args) {
        new Main();
    }
}
```

<br>

### Grid Layout

```java
import javax.swing.*;
import java.awt.*;

class Main extends JFrame {
    private JPanel panel = new JPanel(new GridLayout(2, 2));

    public Main() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        panel.add(new JButton("Button 1"));
        panel.add(new JButton("Button 2"));
        panel.add(new JButton("Button 3"));
        panel.add(new JButton("Button 4"));
        
        getContentPane().add(panel);
        setSize(300, 200);
        setVisible(true);
    }

    public static void main(String[] args) {
        new Main();
    }
}
```

<br>

### Grid Bag Layout

```java
import javax.swing.*;
import java.awt.*;

class Main extends JFrame {
    private JPanel panel = new JPanel(new GridBagLayout());

    public Main() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        GridBagConstraints c = new GridBagConstraints();
        c.gridx = 0;
        c.gridy = 0;
        panel.add(new JButton("Button 1"), c);
        c.gridx = 1;
        c.gridy = 0;
        panel.add(new JButton("Button 2"), c);
        c.gridx = 0;
        c.gridy = 1;
        panel.add(new JButton("Button 3"), c);
        c.gridx = 1;
        c.gridy = 1;
        panel.add(new JButton("Button 4"), c);
        
        getContentPane().add(panel);
        setSize(300, 200);
        setVisible(true);
    }

    public static void main(String[] args) {
        new Main();
    }
}
```

<br>

## OUTPUT

<center>

![31.a.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/31.a.png)

![31.b.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/31.b.png)

![31.c.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/31.c.png)

![31.d.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/31.d.png)

</center>




<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q32)  Create a class `employee` which have name, age and address of employee, include methods `getdata()` and `showdata()`. `getdata()` takes the input from the user, and `showdata()` display the data in following format:
 Name: 
 Age: 
 Address:


<br>

## CODE

```java
import java.io.*;

class employee {
    String name;
    int age;
    String address;

    void getdata() {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Please enter the name of the employee: ");
            name = br.readLine();
            System.out.print("Please enter the age of the employee: ");
            age = Integer.parseInt(br.readLine());
            System.out.print("Please enter the address of the employee: ");
            address = br.readLine();
            br.close();
        }
        catch (Exception e) {System.out.println(e);}
    }

    void showdata() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Address: " + address);
    }
}


class Main {
    public static void main(String[] args) {
        employee e = new employee();
        e.getdata();
        System.out.println();
        e.showdata();
    }
}
```

<br>

## OUTPUT

<center>

![32.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/32.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q33)  WAP to perform basic Calculator operations. Make a menu driven program to select operation to perform (+ - * / ). Take 2 integers and perform operation as chosen by user


<br>

## CODE

```java
import java.io.*;

class Main {
    public static void main(String[] args) {
        try {
            int a,b,chc;
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            
            System.out.print("Please enter the first number: ");
            a = Integer.parseInt(br.readLine());
            System.out.print("Please enter the second number: ");
            b = Integer.parseInt(br.readLine());

            boolean loop = true;
            while (loop) {
                System.out.println();
                System.out.println("Please select the operation to perform:");
                System.out.println("1. Addition");
                System.out.println("2. Subtraction");
                System.out.println("3. Multiplication");
                System.out.println("4. Division");
                System.out.println("5. Exit");
                System.out.print("Enter your choice: ");
                chc = Integer.parseInt(br.readLine());

                switch (chc) {
                    case 1:
                        System.out.println("The sum of " + a + " and " + b + " is " + (a + b));
                        break;
                    case 2:
                        System.out.println("The difference of " + a + " and " + b + " is " + (a - b));
                        break;
                    case 3:
                        System.out.println("The product of " + a + " and " + b + " is " + (a * b));
                        break;
                    case 4:
                        System.out.println("The division of " + a + " by " + b + " is " + ((float)a / b));
                        break;
                    case 5:
                        loop = false;
                        break;
                    default:
                        System.out.println("Invalid choice");
                }
            }

            br.close();
        }
        
        catch (Exception e) {System.out.println(e);}
    }
}
```

<br>

## OUTPUT

<center>

![33.a.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/33.a.png)

![33.b.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/33.b.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q34)  WAP to make use of BufferedStream to read lines from the keyboard until 'STOP' is typed


<br>

## CODE

```java
import java.io.*;
import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        String line;
        ArrayList<String> lines = new ArrayList<String>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("Please enter the lines. Type 'STOP' to stop:\n");
        try {
            while (true) {
                line = br.readLine();
                if (line.equals("STOP")) {break;}
                lines.add(line);
            }
            br.close();
        }
        catch (Exception e) {System.out.println(e);}

        System.out.println("\nThe lines you entered are:");
        for (String l : lines) {
            System.out.println(l);
        }
    }
}
```

<br>

## OUTPUT

<center>

![34.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/34.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q35)  WAP declaring a Java class called SavingsAccount with members `accountNumber` and `Balance`. Provide member functions as `depositAmount()` and `withdrawAmount()`. If user tries to withdraw an amount greater than their balance then throw a user-defined exception


<br>

## CODE

```java
class InsufficientBalanceException extends Exception {
    InsufficientBalanceException(String message) {
        super(message);
    }
}

class SavingsAccount {
    int accountNumber;
    int balance;

    SavingsAccount(int accountNumber, int balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    void depositAmount(double amount) {
        this.balance += amount;
    }

    void withdrawAmount(double amount) throws InsufficientBalanceException {
        if (amount > this.balance) {
            throw new InsufficientBalanceException("Insufficient balance");
        }
        this.balance -= amount;
    }
}


class Main {
    public static void main(String[] args) {
        SavingsAccount account = new SavingsAccount(123456, 1000);
        System.out.println("Current balance: " + account.balance);

        try {
            account.withdrawAmount(500);
            System.out.println("Withdrawn 500.  New balance: " + account.balance);
            account.depositAmount(1000);
            System.out.println("Deposited 1000. New balance: " + account.balance);
        }
        catch (InsufficientBalanceException e) {
            System.out.println(e);
        }
    }
}
```

<br>

## OUTPUT

<center>

![35.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/35.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q36)  WAP creating 2 threads using Runnable interface. Print your name in the `run()` method of first class, and "Hello Java" in the `run()` method of second thread


<br>

## CODE

```java
class Thread1 implements Runnable {
    String name;
   
    Thread1(String name) {this.name = name;}
    public void run() {System.out.println(this.name);}
}

class Thread2 implements Runnable {
    public void run() {
        System.out.println("Hello Java");
    }
}

class Main {
    public static void main(String[] args) {
        Thread1 t1 = new Thread1("Ajay");
        Thread2 t2 = new Thread2();
        Thread thread1 = new Thread(t1);
        Thread thread2 = new Thread(t2);
        thread1.start();
        thread2.start();
    }
}
```

<br>

## OUTPUT

<center>

![36.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/36.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q37)  Write program that uses swings to display combination of RGB using 3 scrollbars


<br>

## CODE

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("RGB Combination");
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(4, 1));

        JScrollBar red   = new JScrollBar(JScrollBar.HORIZONTAL, 0, 1, 0, 255);
        JScrollBar green = new JScrollBar(JScrollBar.HORIZONTAL, 0, 1, 0, 255);
        JScrollBar blue  = new JScrollBar(JScrollBar.HORIZONTAL, 0, 1, 0, 255);

        JLabel label = new JLabel();
        label.setOpaque(true);
        label.setBackground(new Color(0, 0, 0));
        label.setPreferredSize(new Dimension(300, 100));
        label.setHorizontalAlignment(JLabel.CENTER);
        label.setVerticalAlignment(JLabel.CENTER);

        red.addAdjustmentListener(new AdjustmentListener() {
            public void adjustmentValueChanged(AdjustmentEvent e) {
                label.setBackground(new Color(red.getValue(), green.getValue(), blue.getValue()));
                label.setText("rgb(" + red.getValue() + ", " + green.getValue() + ", " + blue.getValue() + ")");
            }
        });

        green.addAdjustmentListener(new AdjustmentListener() {
            public void adjustmentValueChanged(AdjustmentEvent e) {
                label.setBackground(new Color(red.getValue(), green.getValue(), blue.getValue()));
                label.setText("rgb(" + red.getValue() + ", " + green.getValue() + ", " + blue.getValue() + ")");
            }
        });

        blue.addAdjustmentListener(new AdjustmentListener() {
            public void adjustmentValueChanged(AdjustmentEvent e) {
                label.setBackground(new Color(red.getValue(), green.getValue(), blue.getValue()));
                label.setText("rgb(" + red.getValue() + ", " + green.getValue() + ", " + blue.getValue() + ")");
            }
        });

        frame.add(red);
        frame.add(green);
        frame.add(blue);
        frame.add(label);
        frame.setVisible(true);
    }
}
```

<br>

## OUTPUT

<center>

![37.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/37.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q38)  Write a swing application that uses at least 5 swing controls


<br>

## CODE

```java
import javax.swing.*;
import java.awt.*;

class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Swing Controls");
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(5, 1));

        JLabel label = new JLabel("This is a label");
        label.setHorizontalAlignment(JLabel.CENTER);
        label.setVerticalAlignment(JLabel.CENTER);

        JTextField textField = new JTextField("This is a text field");

        JButton button = new JButton("This is a button");

        JCheckBox checkBox = new JCheckBox("This is a check box");

        JRadioButton radioButton = new JRadioButton("This is a radio button");

        frame.add(label);
        frame.add(textField);
        frame.add(button);
        frame.add(checkBox);
        frame.add(radioButton);
        frame.setVisible(true);
    }
}
```

<br>

## OUTPUT

<center>

![38.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/38.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q39)  Write a program to implement border layout using Swing


<br>

## CODE

```java
import javax.swing.*;
import java.awt.*;

class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Border Layout");
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JLabel north = new JLabel("North");
        north.setHorizontalAlignment(JLabel.CENTER);
        north.setVerticalAlignment(JLabel.CENTER);

        JLabel south = new JLabel("South");
        south.setHorizontalAlignment(JLabel.CENTER);
        south.setVerticalAlignment(JLabel.CENTER);

        JLabel east = new JLabel("East");
        east.setHorizontalAlignment(JLabel.CENTER);
        east.setVerticalAlignment(JLabel.CENTER);

        JLabel west = new JLabel("West");
        west.setHorizontalAlignment(JLabel.CENTER);
        west.setVerticalAlignment(JLabel.CENTER);

        JLabel center = new JLabel("Center");
        center.setHorizontalAlignment(JLabel.CENTER);
        center.setVerticalAlignment(JLabel.CENTER);

        frame.add(north, BorderLayout.NORTH);
        frame.add(south, BorderLayout.SOUTH);
        frame.add(east, BorderLayout.EAST);
        frame.add(west, BorderLayout.WEST);
        frame.add(center, BorderLayout.CENTER);
        frame.setVisible(true);
    }
}
```

<br>

## OUTPUT

<center>

![39.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/39.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q40)  Write a java program to insert and update details data in the database


<br>

## CODE

```java
import java.sql.*;

class Main {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/database", "root", "password");
            Statement statement = connection.createStatement();

            // Insert data
            statement.executeUpdate("INSERT INTO details (name, age) VALUES ('John Doe', 25)");
            System.out.println("Data inserted");

            // Update data
            statement.executeUpdate("UPDATE details SET age = 26 WHERE name = 'John Doe'");
            System.out.println("Data updated");

            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

<br>

## OUTPUT

<center>

![40.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/40.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



# Q41)  Write a java program to retrieve data from database and display it on GUI


<br>

## CODE

```java
import java.sql.*;
import javax.swing.*;
import java.awt.*;

class Main {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/database", "root", "password");
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery("SELECT * FROM details");

            JFrame frame = new JFrame("Database Data");
            frame.setSize(400, 400);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLayout(new GridLayout(5, 1));

            JLabel label;
            while (resultSet.next()) {
                label = new JLabel(resultSet.getString("name") + " " + resultSet.getString("age"));
                label.setHorizontalAlignment(JLabel.CENTER);
                label.setVerticalAlignment(JLabel.CENTER);
                frame.add(label);
            }

            frame.setVisible(true);
            connection.close();
        }
        
        catch (Exception e) {e.printStackTrace();}
    }
}
```

<br>

## OUTPUT

<center>

![41.png](/home/mark/Documents/Study%20material%20stuff/Practical%20Files/4/Java/screenshots/41.png)

</center>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



