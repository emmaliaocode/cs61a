# Your First Assignment

## 1) What Would Python Do? (WWPD)
One component of lab assignments is to predict how the Python interpreter will behave.

> Enter the following in your terminal to begin this section:
> ```
> python3 ok -q python-basics -u
> ```
> You will be prompted to enter the output of various statements/expressions. You must enter them correctly to move on, but there is no penalty for incorrect answers.
> 
> The first time you run Ok, you will be prompted for your bCourses email. Please follow [these directions](https://cs61a.org/articles/using-ok/#signing-in-with-ok). We use this information to associate your code with you when grading.

```python
>>> x = 20
>>> x + 2
______

>>> x
______

>>> y = 5
>>> y = y + 3
>>> y * 2
______

>>> y + x
______
```

## 2) Implementing Functions
Labs will often ask you to implement functions. Open `lab00.py` in your text editor. You should see a function called `twenty_twenty_four` that has a blank `return` statement. That blank is the only part you should change. Replace it with an expression that evaluates to 2024. What's the most creative expression you can come up with?

> Don't forget to save your assignment after you edit it! Even better, turn on Auto Save (in the file menu of VS Code).

## 3) Running Tests
In CS 61A, we will use a program called `ok` to test our code. `ok` will be included in every assignment in this class.

Back to the terminal—make sure you are in the `lab00` directory we created earlier (remember, the `cd` command lets you change directories).

In that directory, you can type `ls` to verify that there are the following four files:

- `lab00.py`: the starter file you just edited
- `ok`: our testing program
- `lab00.ok`: a configuration file for Ok
Now, let's test our code to make sure it works. You can run `ok` with this command:

```bash
python3 ok
```

> Remember, if you are using Windows and the python3 command doesn't work, try using just `python` or `py`. See the the [install Python 3](https://cs61a.org/lab/lab00/#install-python-3) section for more info and ask for help if you get stuck!

If you wrote your code correctly and you finished unlocking your tests, you should see a successful test:

```bash
=====================================================================
Assignment: Lab 0
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    2 test cases passed! No cases failed.
```

If you didn't pass the tests, `ok` will instead show you something like this:

```bash
---------------------------------------------------------------------
Doctests for twenty_twenty_four

>>> from lab00 import *
>>> twenty_twenty_four()
0

# Error: expected
#     2024
# but got
#     0

---------------------------------------------------------------------
Test summary
    0 test cases passed before encountering first failed test case
```

Fix your code in your text editor until the test passes.

> Every time you run Ok, Ok will try to back up your work. Don't worry if it says that the "Connection timed out." We won't use your backups for grading.
> While `ok` is the primary assignment "autograder" in CS 61A, you may find it useful at times to write some of your own tests in the form of doctests. Then, you can try them out using the `-m doctest` option for Python).

## Appendix: Useful Python Command Line Options
Here are the most common ways to run Python on a file.

1. Using no command-line options will run the code in the file you provide and return you to the command line. If your file just contains function definitions, you'll see no output unless there is a syntax error.
    ```bash
    python3 lab00.py
    ```
2. `-i`: The `-i` option runs the code in the file you provide, then opens an interactive session (with a `>>>` prompt). You can then evaluate expressions, for example calling functions you defined. To exit, type `exit()`. You can also use the keyboard shortcut `Ctrl-D` on Linux/Mac machines or `Ctrl-Z Enter` on Windows.

    If you edit the Python file while running it interactively, you will need to exit and restart the interpreter in order for those changes to take effect.

    Here's how we can run `lab00.py` interactively:

    ```bash
    python3 -i lab00.py
    ```

3. `-m doctest`: Runs the doctests in a file, which are the examples in the docstrings of functions.

    Each test in the file consists of `>>>` followed by some Python code and the expected output.

    Here's how we can run the doctests in `lab00.py`:

    ```bash
    python3 -m doctest lab00.py
    ```

    When our code passes all of the doctests, no output is displayed. Otherwise, information about the tests that failed will be displayed.