




def latex_to_zhihu(latex_str):
    pass

def latex_to_codecogs(latex_str):
    pass

def latex_to_googleapis(latex_str):
    pass

raw_md_file = "test.md"

with open(raw_md_file, "r", encoding='UTF-8') as f:
    line_num = 0
    for line in f:
        line_num += 1
        # print(line_num)
        if 311 < line_num < 320:
            print(line_num)
            print(line, end='')
        if line.strip() == "$$" and True:
            print("$$")
