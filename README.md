# Naive Python Runner
## What does it do?
naivepyrunner is library to schedule a small amount of timed tasks that may need to perform repeatedly. It does not claim to always choose the right execution order of those tasks to minimize the overall delay if it is running under limited ressources, but it does try to do so.

## How does it work?
## Why is it naive?
The runner assumes that the list with yet to execute tasks does not change while calculating the optimal position for the task. This may lead to not optimal positioning

# Installation
Install it via `pip`:
``` bash
pip install naivepyrunner -U
```

Clone this repo and build it yourself:
``` bash
  pip install wheel -U

  # clone via https
  git clone https://github.com/henningjanssen/naivepyrunner.git
  # or via ssh
  git clone git@github.com:henningjanssen/naivepyrunner.git

  cd naivepyrunner

  # install via pip
  pip install .
  # or register as developed package
  python setup.py develop
  # or build the package and place it with your packages
  make
```

# Usage

# License
