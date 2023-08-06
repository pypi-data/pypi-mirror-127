[![Python application](https://github.com/paterit/omz_theme_ignore_py/actions/workflows/python-app.yml/badge.svg)](https://github.com/paterit/omz_theme_ignore_py/actions/workflows/python-app.yml)

# omz_theme_ignore_py

Add current RANDOM_THEME from [oh-my-zsh](https://ohmyz.sh) to the .zshrc file to the ZSH_RANDOM_IGNORE_THEME section. Use as a zsh alias via python script:

`alias it="python3 omz_theme_ignore/main.py $RANDOM_THEME"`

or via package:

`python3 -m pip install omz_theme_ignore`

`alias it="omz_theme_ignore $RANDOM_THEME"`
