import itertools
from datetime import datetime
import time
from loading import start_loading, stop_loading_animation

def show_header():
    header = r"""
 _______           _______ __________________ _______           _______ 
(       )|\     /|(  ____ \\__   __/\__   __/(  ___  )|\     /|(  ____ \
| () () |( \   / )| (    \/   ) (      ) (   | (   ) || )   ( || (    \/
| || || | \ (_) / | (_____    | |      | |   | |   | || |   | || (__    
| |(_)| |  \   /  (_____  )   | |      | |   | |   | || |   | ||  __)   
| |   | |   ) (         ) |   | |      | |   | | /\| || |   | || (      
| )   ( |   | |   /\____) |   | |   ___) (___| (_\ \ || (___) || (____/\
|/     \|   \_/   \_______)   )_(   \_______/(____\/_)(_______)(_______/
                                                                        

🐍 Wordlist Generator - Mystique 🐍

🦥 Developed by: Gabriel Pontes  
🌐 GitHub: https://github.com/GabrielPontess  
📜 Description: Advanced wordlist generator with character substitutions, 
uppercase/lowercase variations, special characters, and year combinations.
------------------------------------------------------------------------------"""
    
    print(header)
    time.sleep(1);

show_header();

keyword = input("Enter the keyword: ").strip()

substitutions = {
    "a": ["@", "4"],
    "o": ["0"],
    "e": ["3"],
    "i": ["1", "!"],
    "s": ["$", "5"],
    "c": ["(", "{"]
}

special_chars = ["!", "@", "#", "$", "_"]
years = [str(y) for y in range(1000, datetime.now().year + 1)]



def generate_case_combinations(word):
    return [''.join(comb) for comb in itertools.product(*[(char.upper(), char.lower()) for char in word])]


def generate_variations(word):
    variations = [word]

    variations.extend(generate_case_combinations(word))

    for original, subs in substitutions.items():
        new_variations = []
        for var in variations:
            if original in var:
                for sub in subs:
                    new_variations.append(var.replace(original, sub))
        variations.extend(new_variations)

    return list(set(variations))


def generate_patterns(variations):
    patterns = set()

    for var in variations:
        for char in special_chars:
            for year in years:
                patterns.add(var + char + year)  # Ex: h4ck@2024
                patterns.add(var + char + year + char + year)  # Ex: h4ck@2024@2024
                patterns.add(char + var + year)  # Ex: @h4ck2024
                patterns.add(year + char + var)  # Ex: 2024@h4ck

    return patterns

loading_thread = start_loading("Generating wordlist")

variations = generate_variations(keyword)
wordlist = set(variations)
wordlist.update(generate_patterns(variations))

with open(f"{keyword}-wordlist.txt", "w") as f:
    for word in sorted(wordlist):
        f.write(word + "\n")

stop_loading_animation(loading_thread);

print(f"📄 Wordlist generation completed! ({len(wordlist)} words)")
