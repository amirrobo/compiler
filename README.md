# Installation prerequisite
+ Flex
+ Python 3.9
---

# How to Run Scanner (Flex)
for Arm:
```sh
$ flex scanner.l 
$ gcc -o result lex.yy.c -ll 
```
for x86_x64:
```sh
$ flex scanner.l 
$ gcc lex.yy.c -o result 
```

# How to Run Scanner And Parser (Python)
mac and linux :
```sh
$ python3 compiler.py
```
windows :
```sh
$ python compiler.py
```
---
## Update 2022/05/21
+ Add Files
+ Create Scanner And Parser (with python)
+ Create Scanner (witr Flex)