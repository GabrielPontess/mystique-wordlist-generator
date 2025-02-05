<h1 align="center">
   Mystique Wordlist Generator 🐍
</h1>
<div align="center">
  <img src="../assets/mystique-logo.jpg" alt="Mystique Logo" />
</div>

<br/>

**A powerful wordlist generator** that creates customizable wordlists based on a given keyword. The generator includes features like character substitutions, uppercase/lowercase variations, special characters, and year combinations. Perfect for password cracking or security testing! 🔐💻



## Features 📖
- Character substitutions (e.g., "a" becomes "@", "4") 🔄
- Uppercase and lowercase variations 🔠🔡
- Special characters like `!`, `@`, `$`, `_` 🎉
- Combines years (e.g., 2024, 2025) with the keyword and patterns 📅
- Customizable and extensible to fit your needs 🛠️

## Installation ⚙️

### Requirements
- Python 3.* or higher 🐍

### Steps 
1. Clone this repository:
   ```bash
   git clone https://github.com/GabrielPontess/mystique-wordlist-generator.git
   cd mystique-wordlist-generator
   ```

2. Install the required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python src/main.py
   ```

## Usage 🖥️

1. Upon running the script, you will be prompted to enter a keyword. 📝
2. The program will generate a wordlist based on the keyword, applying various patterns such as character substitutions, case variations, special characters, and years. 🔑
3. The generated wordlist will be saved in a file named `<keyword>-wordlist.txt`. 📂

## Example Output 🎯

```bash
Enter the keyword: mystique

Generated wordlist:
- mystique2024!
- mystique$2024
- MYSTIQUE@2024
- MYSTIQUE_2025
- mYsTiQuE@2024
...
```

## Project Structure 📂

```
/mystique-gen
├── /src
│   ├── main.py
│   └── loading.py
├── /docs
│   └── README.md
└── requirements.txt  # Project dependencies
```

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing 🤝

Feel free to fork the repository, make changes, and create a pull request! Contributions are always welcome. 🌱
