#File objects

#Read operations
with open('test.txt','r') as rf:
    #print(rf.name) #gives name of the file
    #print(rf.mode) #gives access mode of the file
    #print(rf.closed) #tells whether file is closed or not
    #f_contents = rf.read() #reads the entire file all at once leading to more memory usage.
    #f_contents = rf.readlines() #read the entire lines and returns as a list
    #f_contents = rf.readline() #reads the first line and when used again, reads the next line and so on.
    #print(f_contents, end ='') #end = '' is used to remove default new line printed while using readline()
    #f_contents = rf.read(10) #reads upto 10 positions
    """for line in rf:
        print (line, end ='')""" #it is efficient as it does not read entire document.
    """size_to_read = 10
    f_contents = rf.read(size_to_read)
    while len(f_contents) > 0:          #it reads upto 10 sizes at time and when used in loop it prints entire document.
        print(f_contents,end = '')
        f_contents = rf.read(size_to_read)"""
    pass

#Write Operations

with open('test.txt','r') as rf:
    with open('test2.txt' , 'w') as wf:
        """for line in rf:
            wf.write(line)""" #Copies entire file and writes into new file test2
        """chunk_size = 10
        f_contents = rf.read(chunk_size)
        wf.write(f_contents)"""
        f_contents = rf.read(10) #reads upto 10 positions and file pointer will be at 10th position
        wf.write(f_contents)
        #rf.seek(0) #places the file pointer at 0th position
        wf.seek(0)
        f_contents = rf.read(10)  # reads upto next 10 positions and file pointer will be at 20th position
        wf.write(f_contents)

#Working jpg file: we need to use binary format instead of string format for that add 'b' to access mode

with open('/home/soliton/Desktop/Sreeram/sreeram.jpg' , 'rb') as sf:
    with open('/home/soliton/Desktop/Sreeram/sree_copy.jpg' , 'wb') as sw:
        pixel_size = 4096
        f_contents = sf.read(pixel_size)
        while len(f_contents) > 0:
            sw.write(f_contents)
            f_contents = sf.read(pixel_size)
