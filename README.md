# Highlambder - there can be only one... lambda to rule them all

Syntactic sugar for Python lambda expressions.
Make your anonymous functions shorter, more expressive, and (let's be honest) just more fun.
<p align="center"><img src="media/highlambder.png" alt="there can be only one" width="400"/></p>

>Image used under fair use, for illustrative and non-commercial purposes. All rights to the character and image belong to their respective owners.

## What is Highlambder?

**Highlambder** lets you write more elegant and compact code by replacing Python’s `lambda` keyword with something cleaner and more intuitive: a symbolic placeholder that behaves like a function.

You get concise, readable lambdas with operator overloading — no more `lambda x:` boilerplate.

## Installation

```bash
pip install highlambder
```

## Quick Examples

```python
from highlambder import L as λ

assert λ(10) == 10
assert (λ + 5)(10) == 15
assert (λ * 5)(10) == 50
assert (3 + λ * 2)(10) == 23
assert (40 / λ / 5)(2) == 4
assert (10 * λ[1])([1, 2, 3]) == 20

assert (-1 + λ * 5 / λ + 1)(13) == 5
assert (λ * 2 + λ * 4 + λ)(10) == 70
assert (λ['A'] + λ['B'])({'A': 3, 'B': 4}) == 7
assert (λ + λ)(2) == 4
```

## Works great with Pandas

```python
import pandas as pd
from highlambder import L as λ

df = pd.DataFrame({
    'A': [1, 1, 2, 2],
    'B': [5, 6, 7, 8],
    'C': ['banana', 'apple', 'kiwi', 'orange'],
})

# Traditional lambda
assert pd.DataFrame.equals(
    df.assign(D=lambda d: d.A + 20),
    df.assign(D=λ.A + 20)
)

# String operations
assert pd.DataFrame.equals(
    df.assign(D=lambda d: d['C'].str.len() * 2),
    df.assign(D=λ['C'].str.len * 2)
)
```

## Why use Highlambder?

- No need for lambda x: — just use λ as a placeholder.
- Composable — use math, indexing, or even method chaining.
- Readable — especially useful in one-liners and pandas pipelines.
- Fun — because code should bring you joy.

## License

[MIT](LICENSE)
