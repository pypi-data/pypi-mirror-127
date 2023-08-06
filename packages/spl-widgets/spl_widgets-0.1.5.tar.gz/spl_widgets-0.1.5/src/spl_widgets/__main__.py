from sys import argv; import os
from . import gorilla_clean, stk_swx, widgets_help, tuner

modules_to_alias=[
    "update_widgets",
    "widgets_help",
    "gorilla_clean",
    "stk_swx",
    "tuner"
]

cmd = argv[1:]

if cmd[0] == "gorilla_clean":
    gorilla_clean.main()

elif cmd[0] == "stk_swx":
    stk_swx.main()

elif cmd[0] == "widgets_help":
    widgets_help.main()

elif cmd[0] == "tuner":
    tuner.main()

elif cmd[0] == "update_widgets":
    os.system("pip -qq install spl_widgets --upgrade")
    zprofile = f"{os.getenv('HOME')}/.zprofile"
    with open(zprofile,"r") as reader:
        lines = reader.readlines()

        for module in modules_to_alias:
            alias_str = f'alias {module}="python3 -m spl_widgets {module}"\n'
            for i, line in enumerate(lines):
                if line == alias_str: break
                elif "spl_widgets" in line and not any([module in line for module in modules_to_alias]):
                    print(f"Removed old alias: {line[:-1]}")
                    lines[i]="KILL"+line
            else: lines.append(alias_str)

    with open(zprofile, "w") as writer:
        writer.writelines([line for line in lines if not line.startswith("KILL")])

else: print("Bad command")