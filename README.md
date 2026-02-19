# Python Calculator

A simple Python calculator library.

## Available operations

| Function | Description |
|---|---|
| `subtract(a, b)` | Returns `a - b` |
| `multiply(a, b)` | Returns `a * b` |
| `divide(a, b)` | Returns `a / b` (raises `ValueError` on zero divisor) |

## Missing operations

- `add(a, b)` – not yet implemented. See [issue #1](../../issues/1).

## Usage

```python
from calculator import subtract, multiply, divide

print(subtract(10, 3))   # 7
print(multiply(4, 5))    # 20
print(divide(10, 2))     # 5.0
```
