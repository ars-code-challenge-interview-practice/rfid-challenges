"""
We parse a lot of log files at {company}. Write a method that reads through a file one line at a time and finds all lines that have these elements in them:

o    the line starts with 'WARNING<n...>' where 'n' is a variable length integer, e.g. WARNING1, WARNING10759, etc. WARNING must be all caps and there must be at least one integer following it -- no spaces before the integer

o    The line ends with one or more spaces followed by 3 asterisks " ***"

o    There can be any text content between these 2 elements, or no content between them e.g "WARNING1 blahblah ***", or "WARNING1 ***" are valid lines.

o    For all lines that match the specification above, print out the line number and the line content.
"""