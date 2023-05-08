import re

def read_template(x):
    print("welcome to Madlib game!,in this game you requrees to Enter adj,noun,......")
    try:
        with open(x,"r") as template:
            file = template.read()
            return(file)
    except FileNotFoundError:
        print("file not found, try another one !!")    
        raise

        
def parse_template(x):
    file = x
    stripped = re.sub("{\w*}","{}", file)
    parts = re.findall(r'{([^}]+)}',file)
    return (stripped,tuple(parts))



def merge(template, parts):
    return template.format(*parts)

read_template("assets/dark_and_stormy_night_template.txt")

