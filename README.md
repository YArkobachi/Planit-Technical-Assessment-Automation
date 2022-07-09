# Planit-Technical-Assessment-Automation
For the automation was used Pyhton + Selenium

For running the testcases please install Python. In my case I was using 3.10.5 

Also please create virtual environment "python.exe -m venv [PATH_TO_DIR]"

After creating the venv please activate it

Install Selenium: pip install selenium


To run test please run this line in the project root folder: python -m unittest TC1.py TC2.py TC3.py TC4.py


1. What other possible scenario’s would you suggest for testing the Jupiter Toys application?
  
  There numerous scenarios that can be implemented, it will mostly depend on project's requirements

2. Jupiter Toys is expected to grow and expand its offering into books, tech, and modern art. We are
expecting the of tests will grow to a very large number.
  1. What approaches could you used to reduce overall execution time?
     
     Multithreading might be an option, also make sure to use efficient coding techniques, do not use implicit wait
  
  2. How will your framework cater for this?
     
     Python is capable for mulithreading, so it shouldn't be a problem with this 

3. Describe when to use a BDD approach to automation and when NOT to use BDD
  
  In my opinion, BDD should be used for verifying the most important parts of the application using end-to-end tests. BDD should also be used to verify the     wanted behaviour using integration tests.
  
