# The Sheng Programming Language

[![build](https://img.shields.io/github/workflow/status/sheng-lang/sheng/Upload%20Python%20Package?style=flat-square)](https://github.com/sheng-lang/sheng/actions/workflows/python-publish.yml)
[![python](https://img.shields.io/pypi/pyversions/sheng?style=flat-square)](https://pypi.org/project/sheng/)
[![pypi](https://img.shields.io/pypi/v/sheng?style=flat-square)](https://pypi.org/project/sheng/)
[![license](https://img.shields.io/pypi/l/sheng?style=flat-square)](https://pypi.org/project/sheng/)

> 结绳：在文字产生之前，古人们靠结绳记事、认事，此举起到了帮助人们记忆的作用。

Sheng is a Chinese programming language named after 结绳 (Jie Sheng), which means tying knots in ropes. In ancient China, before the creation of characters and words, the people remembered and recognized things by tying knots in ropes, which helped them memorize.

The philosophies of the Sheng grammar are interpretable, colloquial, and less punctuation marks. The compiler is implemented in Python with the [PLY (Python Lex-Yacc)](https://github.com/dabeaz/ply) package which processes lexing and parsing in the phases of the compilation.

---

## Usage

```
sheng [option] [file]
```

---

## Installing and Running

> Note: Sheng requires Python 3.9 or later

### PyPI [Recommended]

Install the Sheng compiler from [The Python Package Index (PyPI)](https://pypi.org/project/sheng/):
> Note: This method requires Internet access.
```
pip install sheng
```
Then, execute command `sheng [option] [file]` to run.

### Other install methods

#### Build and install

Build the code and install the Sheng compiler from the local builds:
> Note: This method does not require Internet access.
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
pip install ./dist/<.whl file> --force-reinstall
```
Then, execute command `sheng [option] [file]` to run.

#### Run the compiler module via Python

Run the compiler directly without building and installing in advance:
> Note: This method requires Python 3.9 or later in your environment.
```
python3 -m src [option] [file]
```

---

## Getting Started

This is the Sheng code in `example/helloworld.zh`:
```
甲 赋值 "你好，世界！"
打印(甲)
```
The first line is an assignment statement where `甲` is a variable name which is `赋值` (assign)ed a string value `你好，世界！` (Hello, World!) surrounded by `"` (double quotes). The second line is a function call statement which calls the built-in function `打印` (print) to output the value of the variable `甲`.

This is the Python equivalent of the above Sheng code:
```
x = "你好，世界！"
print(x)
```

Compile the `.zh` file via `sheng` executable:
```
sheng example/helloworld.zh
```

You should see the following output in `stdout`:
```
你好，世界！
```

---

## Contributing

I am excited to work alongside you to build and enhance the Sheng Programming Language\!

***BEFORE you start work on a feature/fix***, please read and follow the [Contributor's Guide](./CONTRIBUTING.md) to help avoid any wasted or duplicate effort.

---

## Code of Conduct

This project has adopted the [Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). For more information contact [luo@jiahai.co](mailto:luo@jiahai.co) with any additional questions or comments.
