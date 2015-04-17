#proper_file_open.py

'''
Example of the best way to deal with opening files.
Using the below syntax ensures that the file is automatically
closed even when we run into an exception within the with:
'''

filePath = './proper_file_open.py'

with open(filePath) as f:
    for line in f:
        print line

'''
Another interesting point to note is that file has an
iterator which enables us to do 'for line in f' above.
'''