import re

def info():
    print("welcome to Madlib game!,in this game you requrees to Enter adj,noun,......")


def prompts(lst):
    input_arr = []
    for element in lst:
        user_input = input(f"enter a {element}")
        input_arr.append(user_input)
    return input_arr

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

def new_file(merged_template):
    with open("./assets/new_file.txt", "w") as f:
        f.write(merged_template)


if __name__ == "__main__":
    info()
    returned_content = read_template("./assets/dark_and_stormy_night_template.txt")
    stripped, parts = parse_template(returned_content)
    user_prompts = prompts(parts)
    merged_txt = merge(stripped, user_prompts)
    print(merged_txt)
    new_file(merged_txt)
