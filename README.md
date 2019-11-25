
# Illumio Coding Challenge

Repository for Illumio Coding Challenge


# Different Approaches
  - Approach 1: Creating HashMap/HashSet which will store all the Rules. It can fetch the rule in O(1). HashMap can be organized in several ways to support this. For Hashset, every rule will be an element in the set. This can be easily implemented in Java or python. However, for storing large dataset (500k - 1M), this approach will take huge memory.
  
  - Approach 2: Using SQLite to store rules. The firewall table will store the data from csv in appropriate format. In python, SQLite3 can be implemented two ways; by storing data in memory or storing data in storage(disk). For huge dataset storing on disk can be the trade off which can be considered.

# Approach using SQLite
   - I have used SQLite to store the rules. Firewall table has attributes:  <direction, protocol, from_port, to_port, from_ip_address, to_ip_address>
   - The csv is read using pandas and each row is parsed to generate the database.
   - For storing IP address, I have converted the IPv4 to an Integer and stored it in the database. This approach helps while comparing the range.
   - SQLite3 for python is implemented in C and is considerably fast for querying data.
   - For quering, the data is parsed and and the Firewall table is queried to check if there is any matching rule that has required direction, protocol, port and IP addresses in the valid range.

# Testing
  - I have used unittest - Unit Testing framework in Python. Junit can be used if either of the approaches (1 or 2) is implemented in Java.
  - I have developed a script to create a dataset of 50k rules. The script can also generate 1M rules. Script is attached in the repo as well.

# Files and Components
  - firewall.py       : Firewall class. Generate Rules DB. Function for checking package.
  - test.py           : Unit Testing. Includes 2 tests
  - data_generator.py : Generates CSV for rules.
  
# Optimizations
  - Using HashMap or HashSet and storing data on disk. I read about a few ways like MapDB, Oracle Berkeley DB can be used to implement this approach

# Team Interests
  - I would be interested to be a part of Data team and Platform team.