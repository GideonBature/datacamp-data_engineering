0x00. Performing a Code Review
===================


Resources
---------

**Read or watch:**

*   [Conventions and PEP-8]()
*   [Classes and the DRY principle]()
*   [Writing unit tests with pytest]()
*   [Creating fixtures with pytest]()
*   [Unit-testing a data pipeline]()
*   [PEP-8 Tutorial: Code Standards in Python](https://www.datacamp.com/tutorial/pep8-tutorial-python-code)
*   [Modularity]()

Project Description
-------------------

For the past five years, you've honed your skills as a Senior Data Scientist for a global university. Your team leverages its data analytics and machine learning skill sets to help other departments make data-driven decisions. One such department is the procurement team, who is trying to decide the best new mobile phone to offer to the university's employees. For the last week, a Junior Data Scientist on your team has been developing a workflow to help provide insight to the procurement team. You will be reviewing their code to ensure it's ready to ship to production.

The first chunk of code that you'll be reviewing is your colleague's function to prepare smartphone data from a CSV file for visualization. After ingesting and cleaning the smartphone data, your colleague has prepared a function to plot a variable passed to the function, versus `"price"`. However, within this function, there is code that does not adhere to DRY principles and is copied and pasted. Make sure to refactor the code appropriately, using the `column_to_label()` function defined below.

Wow, your colleague even included a unit test to ensure `NaN` values were removed from the cleaned DataFrame! However, it doesn't seem like the unit test is passing when executed. Re-work this unit test to ensure that it matches the transformation logic in the `prepare_smartphone_data()` function.

Once you've made changes to the `test_nan_values` unit test, you'll want to ensure that these unit tests execute with `ExitCode.OK`. This means that the `pytest` defined above has passed testing, and the code is one step closer to being to be shipped to production.

For context, there is a print statement in the `prepare_smartphone_data()` function in the first cell of the notebook below that can be used to visualize the dataset your Junior Data Engineer has been working with. Feel free to update this line of code as needed. This can then be removed after the dataset has been investigated. Best of luck!

Requirements
------------

*   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `pycodestyle` style (version 2.5)
*   All your files must be executable
*   The length of your files will be tested using `wc`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   All your functions should be type annotated

Project Instructions
-----

* [1] Review the definition of the `prepare_smartphone_data()` function to ensure the code is well-documented and is easily "readable". Update the existing code to remedy any issues with documentation or readability.
* [2] Review and update the `prepare_smartphone_data()` function to ensure that it adheres to PEP-8 principles.
* [3] Review code in the `visualize_versus_price()` function for adherence to DRY principles. Use the `column_to_label()` function to remove any logic that was previously duplicated.
* [4] Review the unit test written below to ensure the test matches logic in the `prepare_smartphone_data()` function, and make changes as needed. Run the cell to validate the test passes when executed.

Copyright © 2024 DataCamp, All rights reserved.
