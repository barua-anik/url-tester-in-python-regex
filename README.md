# url-tester-in-python-regex
A Python program to check URLs by regular expressions 

## Task
Developing in Python3 a script that takes a configured grouped list of urls to check,
for each url it must be possible to specify regular expressions that are matched
in the content.

The results of the check must be stored somehow for later analysis, at bare minimum
must contain the time of check, response time and possible error if check was not
successful.

## Features
* Python Program
* Regular Expressions or regex
* Reading files
* Writing in the files
* [PEP8] Style
* Less external dependencies
* Comments and documentations 
* Both Python and Jupyter notebook files 

## Sample Input/Output

### URL List: 

abc.com

http://test.test-75.1474.stackoverflow.com/

user:pass@example.com/etcetc

(www.itmag.com)

en.wikipedia.org

mozilla.org

accounts.google.com

plus.google.com

wordpress.org

### Regular Expression: r'\.org'

### Output: 

Regex Test Case:  \.org

Date: 06-10-2019 Time: 09:39:48:005183_PM <re.Match object; span=(525, 529), match='.org'>

Date: 06-10-2019 Time: 09:39:48:005183_PM <re.Match object; span=(1841, 1845), match='.org'>

Date: 06-10-2019 Time: 09:39:48:005183_PM <re.Match object; span=(2974, 2978), match='.org'>

Date: 06-10-2019 Time: 09:39:48:005183_PM <re.Match object; span=(3004, 3008), match='.org'>

Date: 06-10-2019 Time: 09:39:48:005183_PM <re.Match object; span=(3094, 3098), match='.org'>



## Project Status
The project is still going on and will be completed as a full application.

Also, UI, Asynchronous IO, Unit test and a seperate database will be added soon.
