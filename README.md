# Highlambder - there can be only one... lambda to rule them all

Syntactic sugar for Python lambda expressions.
Make your anonymous functions shorter, more expressive, and (let's be honest) just more fun.
<p align="center"><img src="media/highlambder.png" alt="there can be only one" width="400"/></p>

>Image used under fair use, for illustrative and non-commercial purposes. All rights to the character and image belong to their respective owners.

## What is Highlambder?

**Highlambder** is an experimental library that lets you write more elegant and compact code by replacing Python’s `lambda` syntax with something shorter: a symbolic placeholder that behaves like a function.

In practice, `lambda x: x + 1` can be written simply as `λ + 1`.

## Installation

```bash
pip install highlambder
```

## Quick Examples

```python
from highlambder import L as λ

λ (10)  # -> 10

(λ + 5) (10)  # -> 15

(λ * 5) (10)  # -> 50

(3 + λ * 2) (10)  # -> 23

(40 / λ / 5) (2)  # -> 4

(10 * λ[1]) ([1, 2, 3])  # -> 20

(-1 + λ * 5 / λ + 1) (13)  # -> 5

(λ * 2 + λ * 4 + λ) (10)  # -> 70

(λ['A'] + λ['B']) ({'A': 3, 'B': 4})  # -> 7

(λ + λ) (2)  # -> 4

map(λ * 2, range(5)) # -> [0, 2, 4, 6, 8]

("It's a Me, " + λ) ('Mario!') # ->  'It's a Me, Mario!'
```

## pandas and NumPy support (partially supported, work-in-progress)

```python
import pandas as pd
import numpy as np
from highlambder import L as λ

# pandas:
s = pd.Series([1, 2, 3, 4])
assert pd.Series.equals(
    2 * s,
    s.map(2 * λ),
)

df = pd.DataFrame({
    'A': [1, 1, 2, 2],
    'B': [5, 6, 7, 8],
    'C': ['banana', 'apple', 'kiwi', 'orange'],
})

assert pd.DataFrame.equals(
    df.assign(D=lambda d: d.A + 20),
    df.assign(D=λ.A + 20),
)

# String operations
assert pd.DataFrame.equals(
    df.assign(D=lambda d: d['C'].str.len() * 2),
    df.assign(D=λ['C'].str.len * 2),
)

# NumPy:
assert (λ + 2)(np.int64(2)) == 4

assert (λ.max)(np.array([3, 4, 5, 6, 7, 8])) == 8

```

## Limitations (for now)

- Only single-argument functions are supported.
- Calling a function passing λ as an arument usually doesn't work. For example: `len(λ)`.

These limitations may be lifted in future versions.

## License

[MIT](LICENSE)
