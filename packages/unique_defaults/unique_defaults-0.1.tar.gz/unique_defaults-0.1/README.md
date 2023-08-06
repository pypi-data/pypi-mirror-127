# unique_defaults

Replace a function's default values with objects unique to each function call.
This allows writing signatures with mutable defaults *without* sharing the
underlying object between funciton calls.

```python
from unique_defaults import unique_lists

def classic(a=[]):
    a.append("again")
    return " ".join(a)

classic() == "again"
classic() == "again again"

@unique_lists
def unique(a=[]):
    a.append("again")
    return " ".join(a)

unique() == "again"
unique() == "again"
```

Using the mutable object directly in the function signature leads to shorter and
more accurate annotations, as well as simplifying the function's logic.

```python
from typing import List, Optional
from unique_defaults import unique_lists

def classic(a: Optional[List] = None):
    if a is None:
        a = []
    a.append("again")
    return " ".join(a)

classic() == again
classic() == again

@unique_lists
def unique(a: List = []):
    a.append("again")
    return " ".join(a)

unique() == again
unique() == again
```
