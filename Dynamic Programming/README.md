# Description

Bottom-up and top-down approaches to solving LCS.
The programs, given two character strings, finds the length of the longest common string alignment between them (non-continuous).

# How to run

You can run the program with the default arguments:

Defaults:

- Arg1: ['A', 'T', 'A', 'G', 'T', 'T', 'C', 'C', 'G', 'T', 'C', 'A', 'A', 'A']
- Arg2: ['G', 'T', 'G', 'T', 'T', 'C', 'C', 'C', 'G', 'T', 'C', 'A', 'A', 'A']

```bash
python main.py
```

Or the program can accept 2 arguments:

- Arg1: space separated list of chars
- Arg2: space separated list of chars

```bash
python main.py Arg1 Arg2
```

Example:

```bash
python main.py --list1 'A' 'T' 'A' 'G' 'T' 'T'  --list2 'G' 'T' 'G' 'T' 'T'
```
