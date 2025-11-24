my_name = "\n\n本文由 01357005 蔡侑洆 所完成\n"

with open('./three_pigs.txt', 'r', encoding='utf-8') as in_file:
    three_pig = in_file.read()

three_pig = three_pig.replace("豬大哥","懶羊羊")
three_pig = three_pig.replace("豬二哥","沸羊羊")
three_pig = three_pig.replace("豬小弟","喜羊羊")
three_pig = three_pig.replace("豬","羊")
three_pig += my_name

with open('./three_sheep.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(three_pig)