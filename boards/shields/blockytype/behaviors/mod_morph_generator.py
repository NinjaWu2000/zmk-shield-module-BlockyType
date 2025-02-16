mod_list = []
normal_list = []
modified_list = []


while True:
    if mod_list == []:
        mod_list.append(input("mod? "))
        if mod_list[-1] == "":
            mod_list.pop()
            continue
    else:
        mod_list.append(mod_list[0])
        print(f"mod? {mod_list[0]}")
    normal_list.append(input("normal? "))
    if normal_list[-1] == "":
        mod_list.pop()
        normal_list.pop()
        continue
    modified_list.append(input("modified? "))
    if modified_list[-1] == "":
        mod_list.pop()
        normal_list.pop()
        modified_list.pop()
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
            print(f"    bindings = <&kp {normal.upper()}>, <&kp {modified.upper()}>;")
            print(f"    mods = <(MOD_L{mod.upper()} | MOD_R{mod.upper()})>;")
            print(f"{help[1]};")
        break
