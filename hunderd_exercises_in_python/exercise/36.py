'''
Question: Please download the words1.txt file from the attachment and 
then create a Python function that takes a text file as input 
and returns the number of words contained in the text file.

Expected output:
10 
'''



file_open = open(r"words.txt",'r')
def file_to_read(file_open):
    for i in file_open:
        ls = i.split(' ')
        print(len(ls))
    
    file_open.close()



file_to_read(file_open)