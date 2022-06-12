
def read_file_content(filename):
    print (open(filename).read())
    #print (filename.count(""))
    return filename
    
    for x in filename:
        print (x)
    
text = read_file_content("./story.txt")

def count_words():
    myDict={
        text:text.count("")
    }
    print(myDict)
count_words()
    
   