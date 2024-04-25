<img src="images/BOSCO_Icon.png" width="100" height="100">

# BOSCO

[![Language:
Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://github.com/gkapfham/chasten/search?l=python)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/gkapfham/5300aa276fa9261b2b21b96c3141b3ad/raw/covbadge.json)

## 🐶 Overview of BOSCO

BOSCO stands for Benchmarking of Sorting & Computational Operations -
but mostly is a way to include the name of the Allegheny College CIS
Department's favorite dog in our work.

BOSCO provides support in analyzing the performance of any algorithm
that takes a list of input through running a doubling experiment.
This is expanded on in this blog post: TODO

### 🖱️ How to Use BOSCO

TODO

### 📝 For Contributers

There are numerous algorithms that process a list of values. The purpose of this
algorithm all-hands assignment is to design, implement, test and then use in an
empirical study a tool that can automatically conduct doubling experiments to
measure the performance of an arbitrary list processing algorithm. The tool that
you implement, tentatively called `bosco`, should operate in a fashion that is
as general-purpose as is possible. This means that it should, whenever possible,
be able to automatically detect and invoke a list-processing function in a
provided Python source code file, determine the type of list that is input into
that function, and then generate data that is suitable for the purposes of
running a doubling experiment to identify its likely worst-case time complexity.

Ultimately, this algorithm all-hands assignment invites you to apply what you
learned in the algorithm analysis course, by implementing a benchmarking
framework that operates in the following fashion:

- Accept as input one or more Python source code files that contain one or more
functions that perform list processing. For the purposes of creating your
benchmarking framework you can assume that all list-processing algorithms will
implement some type of function that accepts as input a list and that it will be
this list whose contents are doubled during the execution of a doubling
experiment.
- Accept as input the fully-qualified name of a list-processing function that
should be subject to benchmarking through a doubling experiment.
- Accept as input the description of an input generation procedure that can
automatically generate data suitable for the purposes of conducting a doubling
experiment to evaluate the performance of the list-processing algorithm.
- Automatically extract the list-processing function from the provided Python
source code file(s) and then reflectively invoke the function to sort data that
was automatically generated.
- In a series of automatically completed benchmarking rounds, the tool should
conduct a doubling experiment by which it generates data sets of increasing size
and then uses them to evaluate the performance of the list-processing algorithm.
- The tool should produce diagnostic data that shows the execution time for each
round of the doubling experiment, a computed version of the doubling ratio based
on the collected data, and a statement about the likely worst-case time
complexity suggested by the doubling ratio.
- Your tool must be implemented with the Python programming language and use the
Poetry system for managing dependencies and packaging.
- Your tool must provide a command-line interface implemented through the use of
Typer and offer command-line arguments that fully support its configuration.
- Your tool can leverage Python source code that you previously implemented as a
part of a course project as long as you carefully document the source of any
Python code segments.

As you work to build and evaluate this system in a team-based fashion, please
keep in mind the following considerations and tasks:

- Organize your class, which comprises the team for this algorithm all-hands
project, into sub-teams organized around completing the following task:
    - **Infrastructure**: Using the provided GitHub repository for the `bosco`
    project, this members of this sub-team will define and implement a process
    for reviewing and merging the tool's source code, setup and configure GitHub
    Actions, make releases of the tool to PyPI, and handle all other
    infrastructure-related tasks. This team is also responsible for setting up
    and managing the GitHub repository that will contain the list-processing
    algorithms chosen by the members of the list-processing algorithms sub-team.
    - **Benchmarking Framework**: The members of this sub-team will specify,
    design, implement, and test the `bosco` tool, ensuring that it correctly
    runs a doubling experiment for any type of list-processing algorithm that
    meets the stated expectations of the tool. This team will work with the
    infrastructure team to ensure that their changes are merged into the `main`
    branch of the GitHub repository. The team's members will also work with the
    team that finds the list-processing algorithms to confirm that `bosco` works
    correctly for every one of the chosen algorithms. Finally, this team will
    assist the members of team tasked with the experimental and analytical
    evaluation, thereby ensuring that they can run the needed experiments.
    - **List-Processing Algorithms**: The members of this sub-team will identify
    and commit a wide variety of list-processing algorithms, leveraging a
    separate GitHub repository that they work with the infrastructure team to
    create and manage. The members of this team are also responsible for running
    the `bosco` tool on each of the list-processing algorithms and confirming
    that the tool produces the expected output. When this team discovers that
    `bosco` does not work correctly for a specific list-processing algorithm,
    they will work with the members of the benchmarking framework team to ensure
    that the tool is correctly implemented to handle the identified issue. This
    team will also assist the team members tasked with performing the experimental
    and analytical evaluation to ensure that they can run the needed experiments.
    - **Experimental and Analytical Evaluation**: The members of this sub-team
    will complete the article published to the algorithm all-hands section of
    the Algorithmology web site. In addition to writing the article, the members
    of this team will perform a preliminary analytical evaluation of each
    function identified by the team tasked with finding the list-processing
    algorithms. The team members will use the results of their analytical
    evaluation to guide their use of the completed `bosco` tool when running a
    doubling experiment to evaluate the performance of each algorithm. This team
    will also write the final report and work with the course instructor to
    publish it to the Algorithmology web site by the following Friday.
- Meet in your assigned groups to discuss how your team is going to design,
implement, test, and evaluate your benchmarking framework. Make sure that you
give your benchmarking framework a descriptive name that reflects its purpose.
- Discuss with your team members which GitHub repository you are going to use to
coordinate your work. As you make this decision, please bear in mind that the
final version of your framework will be transferred to the course's GitHub
organization and so that it may be considered for use in follow-on projects.
- Specify, design, and implement a benchmarking framework that supports the
experimental evaluation of any list-processing algorithm function that you and
your team members agree your benchmarking framework should support.
- Collect a group of list-processing algorithms and use them to conduct a series
of doubling experiments that experimentally evaluate their performance with the
ultimate goal of determining which algorithm is the fastest and characterizing
the likely time complexity of each algorithm.
- Write and publish on the course web site a blog post that explains (a) how you
designed and implemented your benchmarking framework, (b) the list-processing
functions that you chose to use in your doubling experiments, (c) the runtime
results from your experimental study with the benchmarking framework that you
implemented and (d) the running time results from an analytical evaluation that
you conducted. Your blog post should clearly articulate (a) whether or not the
experimental and analytical results for your function are in alignment with each
other, (b) what is most likely to be the realistic runtime and true running time
of a list-processing function, and (c) why you judge that your function has this
runtime and running time.
