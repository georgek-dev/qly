
# qly

_"the programming language that gets things done **quickly**"_
qly (short for: "quickly") is a programming language designed for doing things quickly. Its syntax is simple to learn, it's powerful and quite fast.

## Installing

First you'll need Python and pdm. For documentation sphinx is also recommended.
Install these packages by: 
```bash
$ pip install --upgrade pip
$ pip install pdm sphinx
```

Next run: `pdm build` to build the package and `cd docs; make html` if you're on *NIX or `CD DOCS; MAKE.BAT html` on Windows (CMD.exe). The compiled documentation will be in build; the package in ../dist/. Install the package by `cd ..` and `pip install dist/*-.whl`. Now you should be able to run `qly`.

## Using qly

There is a file: `test.qls` located in the root of the repository. It is a good starting point for learning qly (as it intentionally contains errors - have fun fixing them!) and for getting a quick glimpse of its syntax. There is also a tutorial included in `docs/build/html/users/tutorial.html` for first time qly learners and programmers.

**HAVE FUN USING QLY! :grin:**
