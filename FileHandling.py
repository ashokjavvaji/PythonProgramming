print('+---------------------------+')
print('| FILE OPERATIONS IN PYTHON |')
print('+---------------------------+')

'''
file operations
open-read/write-close
when file is opened it is locked for access for others
file=open(<path to file>,<mode>)
file.read() -> to read file
file.write(<content>) -> to write data
file.seek(0) -> move file pointer to start
file.close() -> to close the file
there are 12 differnet modes to open a file
r/w/r+(read and write)/w+(read and write)/a(append)
'''
fp=open('file1.txt','w+')#create if does not exist and open
fp.write('line 1\n')#content will be overwritten
fp.write('line 2\n')
fp.seek(0)
print(fp.read())
fp.close()
