## Object Oriented Concepts
### Task 1: Introduction


There are a number of key concepts that we must have a solid grasp of if we are to effectively use Object Oriented programming languages (such as Java !). These structures build on top of each other (as illustrated in the diagram below) with higher-level concepts being built upon the foundation of the lower-levels.

In the following sections of this workbook, we explore these constructs in more detail - introducing them in theory and then applying them in practice to programming activities. These concepts are closely interlinked, so we will introduce them in pairs in the following workbook tasks.  


![](01%20Introduction/images/concepts.jpg)

# 
### Task 2: Objects and Classes
 <a href='02%20Objects%20and%20Classes/slides/segment-1.pdf' target='_blank'> ![](../../resources/icons/slides.png) </a> <a href='02%20Objects%20and%20Classes/slides/segment-2.pdf' target='_blank'> ![](../../resources/icons/slides.png) </a> <a href='02%20Objects%20and%20Classes/video/segment-1.mp4' target='_blank'> ![](../../resources/icons/video.png) </a> <a href='02%20Objects%20and%20Classes/video/segment-2.mp4' target='_blank'> ![](../../resources/icons/video.png) </a>

**Objects** and **Classes** are fundamental building blocks of Object Oriented code.
View the first set of slides and first video above to see an overview of these constructs.  

The second set of slides and second video illustrate the concepts with a concrete example.
At the end of the video a question is posed - see if you can work out the answer to this problem
(Note that the green "substring" at the bottom of the last slide _isn't_ the solution, but was a _link to the solution_ for use during the lecture).
Once you have an idea of what the output should be, hover over this <img src="answer.jpg" title="The substring is: 01" style="vertical-align:bottom" />
button to reveal the actual solution.

Once you are happy with the concepts presented in the lecture materials, attempt the following practical activity in order to apply your knowledge:
- Open up the `Shapes` project that we gave you last week and find the `Triangle` class file (it should be somewhere in the `src` folder !)
- Add a constructor method to the `Triangle` class that takes three `int` parameters (which are the lengths of each side of the triangle)
- Add some `int` attributes to the top of the `Triangle` class and use these to store the lengths of the three sides passed into the constructor
- Write a method called `getLongestSide` that returns the length of the longest side of the triangle (i.e. the largest of the three ints)

Inside the project's `main` method (which is contained in the `Shapes` file), add the following code to create a new instance of
the `Triangle` class and print out its longest side:

``` java
Triangle testTriangle = new Triangle(5, 7, 9);
int longestSide = testTriangle.getLongestSide();
System.out.println("The longest side of the triangle is " + longestSide);
```

Create a number of different instances of `Triangle`, each with different length sides
and check that your `getLongestSide` method operates as expected for each instance.

Notice how in the above code you can "glue" separate Strings together in Java by using the `+` concatenation operator.
Java will even let you concatenate _different_ types together (in the above example, a `String` and an `int`).

Now use this knowledge to add a `toString` method to your Triangle class that returns a suitable `String` that describing the Triangle
(e.g. `This is a Triangle with sides of length 4, 5, 7`)
  


# 
### Task 3: Inheritance and Polymorphism
 <a href='03%20Inheritance%20and%20Polymorphism/slides/segment-1.pdf' target='_blank'> ![](../../resources/icons/slides.png) </a> <a href='03%20Inheritance%20and%20Polymorphism/video/segment-1.mp4' target='_blank'> ![](../../resources/icons/video.png) </a> <a href='03%20Inheritance%20and%20Polymorphism/deep/segment-1.pdf' target='_blank'> ![](../../resources/icons/deep.png) </a> <a href='03%20Inheritance%20and%20Polymorphism/deep/segment-1.mp4' target='_blank'> ![](../../resources/icons/deep.png) </a>

View the slides and video above to refresh your memory on the concept of **Inheritance**. Then attempt the following task which will add to your existing project. Note that the "PRO" slides and video aren't _required_ to complete this exercise, but provide some deeper and more complex information regarding the concept of inheritance for those of you who are interested (the code fragments from the "PRO" slides can be found in <a href="pro-code.zip" target="_blank">this zipfile</a>).

There are many different types of shape in the world (in addition to just triangles !). The template project contains a simple hierarchy of shapes including a `Circle` and `Rectangle`. If you open these classes in IntelliJ, you will see that both share the same super class called `TwoDimensionalShape` (from which all 2D shapes will inherit). Currently your `Triangle` class in not part of the inheritance hierarchy - you should add it now by using the `extends` keyword at an appropriate place in the `Triangle` file to link it to the `TwoDimensionalShape` class.

The slides and video linked to above also discussed the notion of **Polymorphism**. Let us explore this concept in your code: inside the project's `main` method, create a variable that can hold an instance of the `TwoDimensionalShape` class. Try to fill this variable with each type of shape in turn (`Circle`, `Rectangle` and `Triangle`). Each time, print the content of the variable - just to show what type it currently holds.  


**Hints & Tips:**  
If you try to print out an instance of a class by passing it to `println`, it will call the `toString` method of that object in order to get a printable string. Luckily you wrote just such a method for your `Triangle` class in the previous task of this workbook !  


# 
### Task 4: Abstraction and Encapsulation
 <a href='04%20Abstraction%20and%20Encapsulation/slides/segment-1.pdf' target='_blank'> ![](../../resources/icons/slides.png) </a> <a href='04%20Abstraction%20and%20Encapsulation/slides/segment-2.pdf' target='_blank'> ![](../../resources/icons/slides.png) </a> <a href='04%20Abstraction%20and%20Encapsulation/video/segment-1.mp4' target='_blank'> ![](../../resources/icons/video.png) </a> <a href='04%20Abstraction%20and%20Encapsulation/video/segment-2.mp4' target='_blank'> ![](../../resources/icons/video.png) </a> <a href='04%20Abstraction%20and%20Encapsulation/deep/segment-1.pdf' target='_blank'> ![](../../resources/icons/deep.png) </a> <a href='04%20Abstraction%20and%20Encapsulation/deep/segment-1.mp4' target='_blank'> ![](../../resources/icons/deep.png) </a>

**Abstraction** and **Encapsulation** are closely linked concepts. Abstraction provides a simplified view of complex objects by only presenting a small number of high-level, easily understandable behaviours and properties. Encapsulation goes one step further by locking away low-level detail and preventing programmers from interfering with the internal operation of objects. View the slides and video linked to above to gain a deeper understanding of these two concepts.

With the knowledge gained from the above, you will now add some elements of internal state to your project. In addition to a number of sides, all shapes also have a colour. Add a new variable to the `TwoDimensionalShape` class that allows the shape's colour to be stored.

To help you in this task, we have provided you with a `Colour` class. The class is already part of the template project and can be found in the `src` folder along with all the other classes. The `Colour` class contains a number of predefined colours, which can be accessed in the following way:

```java
Colour firstColour = Colour.RED;
Colour secondColour = Colour.YELLOW;
Colour thirdColour = Colour.WHITE;
```
Again, there is an optional PRO slide and video linked to at the top of this section which discusses the importance and implications of data hiding through encapsulation.  


# 
### Task 5: Controlling Access
 <a href='05%20Controlling%20Access/slides/segment-1.pdf' target='_blank'> ![](../../resources/icons/slides.png) </a> <a href='05%20Controlling%20Access/video/segment-1.mp4' target='_blank'> ![](../../resources/icons/video.png) </a> <a href='05%20Controlling%20Access/deep/segment-1.pdf' target='_blank'> ![](../../resources/icons/deep.png) </a> <a href='05%20Controlling%20Access/deep/segment-1.mp4' target='_blank'> ![](../../resources/icons/deep.png) </a>

It is no good being able to store the colour of a shape if there is no way to access it ! After all, how would we draw a shape if there was no way to find out what colour it was ? Take a look at the slides and video above to find out why we need to be careful when providing access to encapsulated data. Using this knowledge, add `setColour` and `getColour` methods to the `TwoDimensionalShape` class that allow the colour to be updated and retrieved.

Now update the `toString` method of your Triangle class so that the printable String that is returned also contains the colour of the triangle (e.g. "This is a BLUE Triangle with sides of length 4, 5, 7"). Test this out in your main method by creating a triangle, setting its colour and then printing it out.

Now, what if we wanted to add colour details to all shapes' `toString` methods ? So that calling `toString` on Circles, Rectangles etc. would also return the colour of that shape as part of the String. What would be the most efficient way of doing that (i.e. writing the least amount of code, with the minimum amount of replication) ?

Finally in this task: as programmers, we have a lot of control over the access to our variables, methods and classes. Check out the "PRO" slides and video above for more details on the various options available.  


# 
### Task 6: Enumerations
 <a href='06%20Enumerations/slides/segment-1.pdf' target='_blank'> ![](../../resources/icons/slides.png) </a> <a href='06%20Enumerations/video/segment-1.mp4' target='_blank'> ![](../../resources/icons/video.png) </a> <a href='06%20Enumerations/deep/segment-1.mp4' target='_blank'> ![](../../resources/icons/deep.png) </a>

Some shapes (such as Circles) come in only one variant - a Circle is a Circle !
Other shapes however (Triangles for example) can come in range of different variants (Isosceles, Right-angle, Equilateral etc).
We _could_ create a range of subclasses of the `Triangle` class to represent each of these...
However this might be seen as overkill, since the various sub-classes wouldn't have any additional attributes or methods,
so we could end up with a lot of almost empty files (causing unnecessary clutter in our file system !)

Instead, we will use this opportunity to explore another feature of Java - **enumerations**.
In Java there is an enumeration mechanism (very much like that in C).
This allows us to declare a predefined list of values that a variable can hold.
Take a look at the slides and videos above to find out more details regarding enumerations,
then attempt the task described below.

With the knowledge you have gained from these slides and video, add to your `Triangle` Class to make it "self-aware":
so that instances of the class will _know_ what kind of triangle they are.
As a programmer, we aren't going to actually _tell_ the triangle what variant it is, the triangle will work it out for itself
(based on the length of the sides passed into the constructor).

Add some code to your `Triangle` constructor method so that it works out what kind it is and stores the result in a private variable.
We have provided you with an enumeration called `TriangleVariant` (found in the `src/main/java/` folder)
that can be used to differentiate between the various triangle variants. For this task, start out simply by just checking
to see if the triangle is an equilateral (i.e. all sides are exactly the same size) - you will get the chance to implement the
more complex triangle checks in the next task.

If all sides are of equal length, set the variant to be `TriangleVariant.EQUILATERAL`. If the sides are not equal,
leave the variable blank (called `null` in Java) for the time being.

Add a new method `getVariant` to your `Triangle` class so that external objects can find out the type of a particular triangle. 
Make sure your code works by creating a number of different equilateral triangles and checking what is returned when you call their `getVariant` method.
  


# 
### Task 7: Systematic Testing


In this next task, you will implement checks for all the other triangle variants.
Rather than manually testing your code (which can get tedious for lots of triangles),
we are going to employ a mechanism for automated testing !
We have provided a <a href="Test Script/TriangleTests.java" target="_blank">triangle test script</a>
that contains a variety of test cases to verify the operation of your triangle variant detection code.
This test file makes use of a testing framework called **JUnit** (which you will learn more about in another unit !)

Download the test script and drop it into the `src/test/java/edu/uob` folder in your project
(be sure to save it with a `.java` extension - some browsers will try to append a `.txt` extension !).
You can run individual test methods by opening the `TriangleTests` file in the IntelliJ editor and then
clicking on the green "play" button to the left of each test method name.
Once the tests have finished running, you should see a report detail which tests have failed
(when tests pass, you don't get much textual feedback - just some green ticks !)

Add additional code to your `Triangle` constructor method that determines the type of triangle being created.
You should implement detection of each type of triangle in turn (first Equilateral, then Isosceles, then Scalene etc.).
Make sure your code passes all of the tests for a particular variant before moving on to the next.
You will need to think carefully however about the order in which your checks for each triangle appear in your code
(e.g. some illegal triangles might at first sight _appear_ to meet the criteria for an isosceles triangle !). 

The final group of tests (to do with overflow) are more difficult, so you should leave those until the end.
Note that these final tests may require you to refactor your code a fair bit (depending on how you wrote it in the first place) !  


**Hints & Tips:**  
Perhaps the simplest way to approach this task is to create a multi-branch IF statement that will classify the triangle. The order of the branches of the IF statements will be very important: you should check for specific/special cases at the top, with more general cases at the bottom (you'll soon understand why later !)

Before you ask, yes the test cases are all correct !  All triangle are as listed in the test file.
The final three scalene triangles are _almost_ other types of triangle, but not quite ;o)  


# 
### Task 8: Command line Testing


In some situations (e.g. during the coursework marking process) it is useful to be able to run the test cases from the command line
(rather than having to start up IntelliJ). In order to run all of the unit tests present within a Maven project,
change into the project root folder in your command prompt and type:

    Linux/OSX:   ./mvnw clean test
    Windows:     mvnw clean test


If your code passes all of the tests, you should see the following in the Maven output messages:

    [INFO] Tests run: 9, Failures: 0, Errors: 0, Skipped: 0
    [INFO] 
    [INFO] ------------------------------------------------------------------------
    [INFO] BUILD SUCCESS
    [INFO] ------------------------------------------------------------------------


If on the other hand you fail some tests, the output will look something like the following:

    [ERROR] Tests run: ?, Failures: ?, Errors: ?, Skipped: ?
    [INFO] 
    [INFO] ------------------------------------------------------------------------
    [INFO] BUILD FAILURE
    [INFO] ------------------------------------------------------------------------

Make sure you are able to pass all of the tests before you consider this workbook finished !  


# 
