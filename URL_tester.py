# A Python program to check URLs by Regular Expressions 

# Importing libraries 

import re
from datetime import datetime


class URL_Tester():
    """ This class takes a configured grouped list of urls and then 
    checked by one or more regular expressions. The output results
    are saved by automatically creating a new file with details info. 
    
    Example: We have a list of URL eg. www.google.com and
    we run a regular expression eg. '\.com' that finds if
    the given URL is matched with the part '.com'. If it finds 
    the match, it will write the output value in the text file as follows:
    
    Date: 06-10-2019 Time: 08:26:36:994348_PM <re.Match object; span=(3, 7), match='.com'>
    """

    def __init__(self, source_file, output_file, reg_ex=r'.'):
        """Initializes the URL_Tester class with the parameters
        
        Args: 
        source_file = Name of the file that has the lists of URLS 
        output_file = Name of the file that will be saved as output
        
        """
        
        self.source_file = source_file
        self.output_file = output_file
        self.reg_ex = reg_ex

    def url_check(self):
        """ This function checks the list of URLs in according to 
        the regular expressions passed in as parameters.
        """

        try:
            time = datetime.now().strftime("Date: %d-%m-%Y Time: %I:%M:%S:%f_%p")

            patterns = self.reg_ex

            # Extracting the regular expressions 
            for regex in patterns:
                pattern = re.compile(regex)

                # Reading the Source/URL files
                with open(self.source_file, 'r') as f:
                    urls = f.read()
                    matches = pattern.finditer(urls)

                # Writing the outputs in the file 
                with open(self.output_file, 'a') as f:
                    print('Regex Test Case: ', regex, file=f)
                    
                    for match in matches:
                        print(time, match, file=f)

            print("Nice, The program executed successfully. ")

        except:
            print("Oops, an exception occurred!")


# Writing the regular expressions 
regex_patterns = [
    r'(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.#?&//=]*)',
    r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*',
    r'\.com',
    r'\.org']

# Executing the program by class name and required arguments 
URL_Tester('URL_list.txt', 'Checked_urls.txt', regex_patterns).url_check()


