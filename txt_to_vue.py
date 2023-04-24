# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def txt_to_vue(txt_file, output_file):
    out_obj = []

    # 读取文本
    with open(txt_file) as file:
        lines = file.readlines()
        for l in lines:
            l_obj = format_line(l)
            if l_obj is None:
                continue

            out_obj.append(l_obj)

    # 写入文本
    with open(output_file, 'w') as f:
        for o in out_obj:
            o_line = format_out_obj(o)
            f.write(o_line + ',\n')

    print(out_obj)


def format_line(line: str):
    # print(line)
    ls = line.split("\t")
    if len(ls) < 2:
        print("行格式错误：%s" % line)
        return None

    print(ls)

    # { prop: 'goodsName', label: '商品名称' }
    pv = ls[0]
    if len(ls) > 2:
        lv = ls[1]
    else:
        lv = ls[0]

    if lv == '':
        lv = pv

    pk = 'prop'
    lk = 'label'

    obj = {pk: pv, lk: lv}
    return obj


def format_out_obj(o_obj):
    o_str = o_obj.__str__()
    pk = 'prop'
    pk_j = "'%s'" % (pk)

    lk = 'label'
    lk_j = "'%s'" % (lk)

    o_str = o_str.replace(pk_j, pk).replace(lk_j, lk)

    return o_str


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    txt_to_vue('/Users/yun/Downloads/f.txt', '/Users/yun/Downloads/o.txt')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
