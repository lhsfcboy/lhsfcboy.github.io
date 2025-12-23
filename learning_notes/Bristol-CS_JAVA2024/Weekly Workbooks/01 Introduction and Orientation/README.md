## Introduction and Orientation
### Task 1: Introduction


Welcome to this first practical workbook for the Object Oriented Programming with Java unit.
The aim of these workbooks is to explore key theoretical concepts that underlie the unit and 
give you the opportunity to apply these in practical programming exercises. In the previous teaching block, you learnt to program in C (to varying degrees of success ;o). In this unit however, you will be using **Java** and as such the _organisation_ of your code _should_ be very different. There are a number of key concepts that are fundamental to **Object Oriented** code. These will be introduced in the lecture sessions to this unit - it is essential that you engage with these lecture sessions before attempting the practical exercises. In order to complete the workbooks, you will also need to make use of the material from each weeks briefing session. The slides for both the lecture and briefing sessions can be found on GitHub.

This first workbook is relatively simple and straightforward - the aim is to provide a gentle introduction to the unit, before we start to address more complex and sophisticated language concepts.
Where you see the blue "Slides" and "Video" buttons at the top of some of the sections in a workbook, 
you should view this material _before_ attempting the practical activities described in that section. 
Note that it is easier to 'clone' the GitHub repository and view the workbook materials locally on your own computer
(rather than trying to browse them online via the GitHub website).



  


# 
### Task 2: IntelliJ IDE


Previously on this programme, the emphasis was on learning to program.
In this current teaching block, we will be focusing on the skills required to turn you into a _developer_.
Part of this skillset is the ability to effectively use an Integrated Development Environment (IDE).
In this unit, we will therefore be using the IntelliJ IDE in order to support development.
This is already installed on the lab machines and can be found either via the application menus or on the command line at 
`/opt/idea/2024/bin/idea.sh`. This installation _should_ already have the UoB license enabled, 
If however it asks you to provide license details when you first run it, enter the following as the on-site license server:
`http://ls-jetbrains.bris.ac.uk:8080`

You do not HAVE to install IntelliJ on your own laptop, however many people choose to do so (in order to work from home).
If you plan to use your own computer for writing code, now is a good time to get IntelliJ installed.
Follow the step-by-step installation instructions that were provided in the briefing slides for this session (available via GitHub).
For a more detailed walk-through, see the following platform-specific videos for getting started with IntelliJ on 
<a href="https://web.microsoftstream.com/video/608b2c4c-1834-4429-9c86-bf19530c7f3a" target="_blank">Ubuntu</a>, 
<a href="https://web.microsoftstream.com/video/382a7600-3940-4415-a680-002de6960b99" target="_blank">Windows</a> and
<a href="https://mediasite.bris.ac.uk/Mediasite/Play/e879f20d3cb44e989202926a64f5be481d" target="_blank">Mac OSX</a>.
  


# 
### Task 3: Hello World
 <a href='03%20Hello%20World/slides/segment-1.pdf' target='_blank'> ![](../../resources/icons/slides.png) </a> <a href='03%20Hello%20World/video/segment-1.mp4' target='_blank'> ![](../../resources/icons/video.png) </a>

Traditionally, the first program that you write in _most_ languages is "Hello World".
Take a look at the slides and video above that describe "Hello World" in Java.
Now work through the following step in order to create and run the "Hello World" program using IntelliJ. If you already have IntelliJ installed on your laptop, you might like to follow these steps using your own computer. If not, don't worry - you can work through this activity on the lab machines.

1. Create a new project in IntelliJ (see screenshot below for suggested project settings).
2. Find the `java` folder in the project view panel (it should be inside the `src/main` folder).
3. Right click on the `java` folder (`control` click on a Mac) to open up the pop-up menu
4. Select `New > Java Class` and create a new Java Class called `HelloWorld`
5. Copy the code from the above slide and paste it into your new class (replacing any existing code)
6. Click on the green `Run` button on the top-bar menu (or to the left of the `main` method)

There will be a short delay as IntelliJ compiles and runs your code.
If everything is successful you should see the following output in the console panel:

```
Hello World!

Process finished with exit code 0
```  


![](03%20Hello%20World/images/new-project.jpg)

# 
### Task 4: Template Project


Rather than you having to create a new project each time we start a workbook or assignment,
we will often provide you with an existing template project (in order to help you get started).
These templates will contain all of the rules and dependencies required to build a project. One of the main benefits is that these projects can be imported directly into Intellij (or any other IDE for that matter). This will save us a lot of time installing required libraries and setting up the build environment.

For the next couple of workbooks, we will be using the <a href="extras/IntelliJ Template/" target="_blank">shapes</a> template project.
You should copy the entire `cw-shapes` directory into your work folder (wherever you want to keep your code for this unit). In order to open an existing project in IntelliJ, simply click on the `Open` button on the IntelliJ startup screen and pick the `cw-shapes` folder using the file dialog. 

Open the `cw-shapes` project now and make sure you can run the code before moving on to the next task. The first time you open a project, you may find that you have to wait some time before you can run it - this is due to the need for IntelliJ to download any dependencies and generate various project setting files (see the progress bar at the bottom of the window for details). Note that the first time you open the project you may well need to select a JDK from the list of available development kits (if you see the `Project JDK is not defined - Setup JDK` message when you open the project).  


# 
### Task 5: Command Line


During this workbook, we have spent the majority of the time exploring the use of IntelliJ.
At this stage however, it is worth spending a little bit of time taking a look at how we can build and run
Java projects from the command line. This is important because the assessed exercises later on in the
unit will be marked on the command line (and you need to make sure that your code will actually build and run from there).

You may have used *GNU Make* previously - this software saves you from having
to manually type out all the compile and linking commands every time you want to build your software.
`make` takes care of running all the required build commands (as specified in the `Makefile`)
and intelligently works out what needs to be done.
`make` however isn't commonly used for Java development since building Java projects
usually involves much more complicated activities than just running a set of commands.
This is where the **Maven** build system comes in - it provides various tools for building and running complex Java projects.

On your command line, change into the project root folder (the directory where the `pom.xml` file resides) and type one of the following commands (depending on your platform):

    Linux/OSX:   ./mvnw clean compile
    Windows:     mvnw clean compile

**Note**: On some unix systems, you _might_ need to make `mvnw` executable first (i.e. by running `chmod u+x mvnw`)

The command is doing 2 separate things in sequential order:

1. `clean` ensures that everything will be freshly built by cleaning out (deleting) previously generated files
2. `compile` compiles and builds all files and resources (stopping if any build errors are encountered)

Note that you can learn more about these and other build tasks in the official <a href="https://maven.apache.org/guides/getting-started/index.html" target="_blank">Maven documentation</a>.

The first time you run the compile command, it might take a while to complete so be patient. This is because Maven may need to download various project dependencies. If successful, the output on the command line should looks something like this:

    [INFO] ------------------------------------------------------------------------
    [INFO] BUILD SUCCESS
    [INFO] ------------------------------------------------------------------------
    [INFO] Total time: 42 s
    [INFO] Finished at: 2022-01-01T00:00:00Z
    [INFO] ------------------------------------------------------------------------

If you get a `BUILD FAILURE`, it means the project failed to complete some of the specified tasks.
If this is the case, it would be wise to go back into IntelliJ and make sure no code issues are detected there
(i.e. no code is highlighted in red and the project can still be built and run).
Fix any problems in IntelliJ and then return to the command line.

Once you have successfully built your code on the command line, you can run your program using:

    Linux/OSX:   ./mvnw exec:java
    Windows:     mvnw exec:java

For a given project, there may be many different things that can be executed - the above command runs the `main` method of the Java part of the project (currently the only thing we have written).

If you are interested in finding out more about Maven, take a look at <a href="extras/maven.pdf" target="_blank">this document</a> that describes the of operation of the built tools in more detail.  


# 
