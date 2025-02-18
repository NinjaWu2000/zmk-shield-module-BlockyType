mod_list = []
normal_list = []
modified_list = []
normal_behavior = ""
modified_behavior = ""


def clear_last_entry():
    global normal_behavior, modified_behavior
    lists = [mod_list, normal_list, modified_list]
    lenght = len(lists[0])
    for l in lists:
        if len(l) == lenght:
            l.pop()
    if lenght == 1:
        normal_behavior = ""
        modified_behavior = ""


while True:
    if mod_list == []:
        normal_behavior = input("normal behavior? ").lower()
        modified_behavior = input("modified behavior? ").lower()
        mod_list.append(input("mod? "))
        if mod_list[-1] == "" or normal_behavior == "" or modified_behavior == "":
            clear_last_entry()
            continue
    else:
        mod_list.append(mod_list[0])
        print(f"mod? {mod_list[0]}")
    normal_list.append(input("normal key? "))
    if normal_list[-1] == "":
        clear_last_entry()
        continue
    modified_list.append(input("modified key? "))
    if modified_list[-1] == "":
        clear_last_entry()
        continue
    stop = input("[continue]/print? ")
    if stop == "" or stop == "continue":
        continue
    else:
        help = ["{", "}"]
        print()
        for i in range(len(modified_list)):
            mod = mod_list[i]
            normal_split = normal_list[i].split(" ", 1)
            modified_split = modified_list[i].split(" ", 1)
            normal = normal_split[0]
            modified = modified_split[0]
            if len(normal_split) >= 2 and len(modified_split) >= 2:
                print(f"/* {normal_split[1]}  ¦  {modified_split[1]} */")
            else:
                print(f"/*   ¦   */")
            print(
                f"{mod[0]}_{normal.upper()}_{modified.upper()}: {mod[0]}_{normal.upper()}_{modified.upper()} {help[0]}"
            )
            print(f'    compatible = "zmk,behavior-mod-morph";')
            print(f"    #binding-cells = <0>;")
            print(
                f"    bindings = <&{normal_behavior} {normal.upper()}>, <&{modified_behavior} {modified.upper()}>;"
            )
            print(f"    mods = <(MOD_L{mod.upper()} | MOD_R{mod.upper()})>;")
            print(f"{help[1]};")
        break
