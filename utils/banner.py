# =====================================================
# PROJECT : DROPEE SN DESIGN
# MODULE  : banner.py
# VERSION : 1.1.0
# STATUS  : STABLE
# AUTHOR  : SN DESIGN STUDIO
#
# DESCRIPTION
# Console startup banner for Dropee Automation Engine
#
# CHANGELOG
# v1.1.0
# - Adapted from Hamster SN Design banner system
# - Updated system name to Dropee
# - Updated version reference
# - Maintained ANSI color / center alignment
# =====================================================

import os
import shutil


RED = "\033[91m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def center(text, width):
    return text.center(width)


def show_banner():

    os.system("clear")

    width = shutil.get_terminal_size((80, 20)).columns

    logo = [
        f"{RED}███████╗███╗   ██╗{RESET}",
        f"{RED}██╔════╝████╗  ██║{RESET}",
        f"{RED}███████╗██╔██╗ ██║{RESET}",
        f"{RED}╚════██║██║╚██╗██║{RESET}",
        f"{RED}███████║██║ ╚████║{RESET}",
        f"{RED}╚══════╝╚═╝  ╚═══╝{RESET}",
    ]

    title = [
        f"{CYAN}SN DESIGN STUDIO{RESET}",
        f"{GREEN}Automation Engine{RESET}",
        f"{YELLOW}Dropee Farming System{RESET}",
    ]

    info = [
        "",
        "Version   : SN-DROPEE 1.1.0",
        "Developer : SN DESIGN STUDIO",
        "Platform  : Termux / Linux",
        "",
        "Mode      : Personal Farming",
        "",
        "────────────────────────────────────────────",
        "",
        "CONTACT",
        "",
        "YouTube   : SN DESIGN STUDIO",
        "Facebook  : ต้องดีแค่ไหน โลกถึงจะจำ",
        "",
        "────────────────────────────────────────────",
    ]

    # LOGO
    for line in logo:
        print(center(line, width))

    print()

    # TITLE
    for line in title:
        print(center(line, width))

    print()

    # INFO
    for line in info:
        print(line)
