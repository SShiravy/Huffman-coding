def modify_cmp_content(content):
    # TODO: extract binary codes and char_n dict from content and return them
    pass

def open_file(file_dir):
    # open file and return the content
    with open(file_dir,"r") as file:
        content = file.read()
    return content

def write_file(content,dir,name):
    # write content in a file with given format and save it in given dir
    with open(dir+name,"w") as file:
        file.write(content)



