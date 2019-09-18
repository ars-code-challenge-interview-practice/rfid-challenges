"""
We parse a lot of log files at {company}. Write a method that reads through a file one line at a time and finds all lines that have these elements in them:

o    the line starts with 'WARNING<n...>' where 'n' is a variable length integer, e.g. WARNING1, WARNING10759, etc. WARNING must be all caps and there must be at least one integer following it -- no spaces before the integer

o    The line ends with one or more spaces followed by 3 asterisks " ***"

o    There can be any text content between these 2 elements, or no content between them e.g "WARNING1 blahblah ***", or "WARNING1 ***" are valid lines.

o    For all lines that match the specification above, print out the line number and the line content.
"""

# example file from here: https://www.ibm.com/support/knowledgecenter/SSLTBW_2.2.0/com.ibm.zos.v2r2.hald001/exmlogfile.htm

# look up how to read through files in python

# Check for WARNING<int> - should start with WARNING
    #  print line #, print line content
    #  separate on spacw

# line ends with " ***"
    #  print line #, print line content
    #  separate on spacw

def read_stuff():
    file = open("sample_log.txt", "r")

    file_lines = file.readlines()

    warn = "WARNING"
    asterix = " ***\n"

    for line in file_lines:
        if warn in line:
            print(line)
        if asterix in line:
            print(line)

if __name__ == "__main__":
    read_stuff()