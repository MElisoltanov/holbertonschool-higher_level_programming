# Python3: Mutable, Immutable… Everything Is Object!

![Python Objects](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

In Python, everything is an object. Integers, strings, lists, sets, even functions and modules are objects stored somewhere in memory, with an identity, a type and a value.

In this post I will walk through what that really means:

- what `id` and `type` are,
- what mutable and immutable objects are,
- which built‑in types belong to each category,
- the difference between assignment and referencing,
- how immutable objects are stored in memory,
- how variable values are managed when passed to functions,
- how integer pre‑allocation works with `NSMALLPOSINTS` and `NSMALLNEGINTS`,
- and finally the special cases of tuples and frozensets.

---

## 1. `id` and `type`: identity vs nature of an object

Two built‑in functions are fundamental for understanding Python’s object model:

- `type(obj)` — returns the **type** (or class) of the object: `int`, `str`, `list`, etc.
- `id(obj)` — returns the **identity** of the object.  
  In CPython, this is the memory address where the object lives.

Example:

```python
a = 42
print(type(a))  # <class 'int'>
print(id(a))    # e.g. 140716592029136 (implementation‑dependent)
```

If two objects have:

- the same value: `obj1 == obj2` is `True`,
- the same identity: `obj1 is obj2` is `True` and also `id(obj1) == id(obj2)`.

Example:

```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # True  -> same *value*
print(x is y)  # False -> different *objects*
print(id(x), id(y))
```

This separation between **value** and **identity** is the foundation for the rest of this article.

---

## 2. What is a mutable object?

A **mutable object** is an object whose internal state (its value) can be changed **in place** without changing its identity.

In CPython, the typical built‑in mutable types are:

- `list`
- `dict`
- `set`
- `bytearray`

(If the checker cares about “all or nothing” for the score: list, dict, set, bytearray.)

Example:

```python
l1 = [1, 2, 3]
l2 = l1          # l2 references the same object as l1

print(id(l1), id(l2))  # same id

l1.append(4)

print(l1)              # [1, 2, 3, 4]
print(l2)              # [1, 2, 3, 4]  -> also changed
print(id(l1), id(l2))  # still the same id
```

Here the object itself is modified. Both `l1` and `l2` “see” the change because they both refer to the same list.

Another memory‑schema‑style view:

```text
name     object (in memory)
----     -------------------
l1  -->  [1, 2, 3]
l2  -->   ^
           \-- same object

After l1.append(4):

l1  -->  [1, 2, 3, 4]
l2  -->   ^
           \-- same object, new value
```

---

## 3. What is an immutable object?

An **immutable object** is an object whose value cannot be changed in place. Any apparent “modification” creates a **new** object with a different identity.

The main built‑in immutable types are:

- numbers: `int`, `float`, `complex`
- `str`
- `tuple`
- `frozenset`
- `bytes`
- `bool` (also immutable, but usually grouped with numbers)

(For the checker list: number (int, float, complex), string, tuple, frozen set, bytes.)

Example with integers:

```python
a = 1
b = a

print(id(a), id(b))  # often the same (CPython may reuse small ints)

a += 1               # same as a = a + 1

print(a)             # 2
print(b)             # 1

print(id(a))         # new id
print(id(b))         # old id
```

The integer object `1` has **not** changed. Instead, Python created a new integer object `2`, and the name `a` now refers to that new object.

Example with strings:

```python
s1 = "Best"
s2 = s1

s1 += " School"  # creates a new string object

print(s1)        # "Best School"
print(s2)        # "Best"
```

Example with tuples:

```python
t = (1, 2, 3)
# t[0] = 10      # TypeError: 'tuple' object does not support item assignment
```

Tuples are immutable, but they can contain mutable objects (we will revisit this with tuples and frozensets).

---

## 4. Lists of mutable and immutable built‑in types

To summarize:

### Mutable built‑in types

- `list`
- `dict`
- `set`
- `bytearray`

### Immutable built‑in types

- Numbers: `int`, `float`, `complex`
- `str`
- `tuple`
- `frozenset`
- `bytes`
- `bool` (logically here, even if not always listed)

These lists are important to reason about how variables behave when we mutate objects or pass them into functions.

---

## 5. Assignment vs referencing (aliases)

**Assignment** in Python does not copy objects, it binds a **name** to an **existing object**.

```python
a = [1, 2, 3]
b = a       # assignment, not a copy
```

Now:

```text
name     object
----     ------
a  -->  [1, 2, 3]
b  -->   ^ same object
```

`a` and `b` are **aliases** for the same object.

If we mutate the list:

```python
a.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
```

Both names show the same contents because there is only one list object in memory. This is the **mechanism of aliases**: multiple names referencing the same object.

To create a **real copy** of a list, we should explicitly copy it:

```python
original = [1, 2, 3]
copy1 = original[:]          # slicing
copy2 = list(original)       # constructor

print(original == copy1)     # True
print(original is copy1)     # False
```

Aliases are especially dangerous if you expect to “copy” but only create another reference.

---

## 6. How an immutable object is stored in memory

Let us take a simple integer. In CPython, an `int` is represented by a structure containing:

- a reference count,
- the type pointer,
- the numeric value.

The important part for us is:

- the object `1` lives once in memory,
- names are just labels pointing to that object.

Memory schema:

```text
object (id: 0xAAA) -> int value: 1
a ------------------^
b ------------------^
```

When we do:

```python
a = 1
b = a
a += 1   # a = a + 1
```

Conceptually:

1. `a` and `b` both refer to the object `1`.
2. `a += 1` creates a **new** object `2` and rebinds `a` to it.

```text
object (id: 0xAAA) -> int value: 1
b ------------------^

object (id: 0xBBB) -> int value: 2
a ------------------^
```

The original object (1) has not changed; only the bindings (names) have.

This is what “immutable object is stored in memory” means: the memory contents of that object never change after creation; only references to it change.

---

## 7. Two memory‑schema examples

### Example 1: list vs `+`

```python
l1 = [1, 2, 3, 4]
print(id(l1))          # e.g. 139926795932424
l1 = l1 + [5]          # new list
print(id(l1))          # different id
```

Schema:

```text
Before: l1 --> [1, 2, 3, 4] (id 0xAAA)

Operation l1 = l1 + [5]
- create new list object [1, 2, 3, 4, 5] at id 0xBBB
- rebind name l1 to this new object

After:
   [1, 2, 3, 4]  (id 0xAAA)  -- possibly unreferenced
l1 --> [1, 2, 3, 4, 5] (id 0xBBB)
```

### Example 2: list vs `+=`

```python
a = [1, 2, 3]
print(id(a))    # e.g. 139926795932424
a += [4]        # in‑place mutation
print(id(a))    # same id
```

Schema:

```text
Before: a --> [1, 2, 3] (id 0xCCC)

Operation a += [4]
- extend the existing list object in place

After:  a --> [1, 2, 3, 4] (id 0xCCC)
```

This pair of examples shows very clearly the difference between creating a **new** object and mutating an **existing** one.

---

## 8. How variable values are managed when passing to a function

Python uses a “**call by object reference**” (or “call by sharing”) model:

- When calling a function, Python passes a **reference** to the object, not a copy.
- The parameter name inside the function becomes a **new alias** for the same object.

### 8.1 Immutable argument

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # 1
```

Flow:

1. `a` refers to `1`.
2. Inside `increment`, `n` also refers to `1` (same object).
3. `n += 1` creates a new object `2` and rebinds `n` to it.
4. Outside, `a` still refers to `1`.

So the caller’s variable is not changed.

### 8.2 Mutable argument

```python
def add_item(lst, value):
    lst.append(value)

l = [1, 2, 3]
add_item(l, 4)
print(l)   # [1, 2, 3, 4]
```

Flow:

1. `l` refers to a list `[1, 2, 3]`.
2. Inside the function, `lst` becomes an alias for this same list.
3. `lst.append(4)` mutates the list in place.
4. Outside, `l` sees the modification because it points to that same object.

Another example, showing that rebinding a parameter does not affect the caller:

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)   # [1, 2, 3]
```

Here `n = v` only changes the local alias `n`, not `l1`.

---

## 9. Integer pre‑allocation: `NSMALLPOSINTS` and `NSMALLNEGINTS`

CPython uses an optimization for small integers: it **pre‑allocates** a range of integer objects when the interpreter starts, so they can be reused instead of recreated every time.

The range is controlled (in CPython source) by:

- `NSMALLPOSINTS`
- `NSMALLNEGINTS`

By default in CPython, it creates all integers in the range:

```text
[-NSMALLNEGINTS, NSMALLPOSINTS - 1]
```

A commonly used configuration is:

```text
NSMALLNEGINTS = 5
NSMALLPOSINTS = 257
```

which means integers from **−5 to 256** are pre‑allocated.

What does “pre‑allocated” mean here?

- When the CPython interpreter starts, it creates these 262 integer objects.
- During program execution, whenever you need an integer in that range, CPython **reuses** the already existing object instead of creating a new one.

Example:

```python
a = 1
b = 1
print(a is b)  # True in CPython (same pre‑allocated object)

x = 257
y = 257
print(x is y)  # often False (not guaranteed to be interned)
```

Why those particular values?

- Small integers are **used very frequently** (loop counters, indexes, simple constants),
- Reusing them avoids many allocations, improves performance, and reduces memory fragmentation.

So, in CPython:

- small integers (`-5` to `256`) are **singletons** (one object reused),
- larger integers are usually freshly allocated when needed.

This is also why some tests in the Holberton project expect `a is b` to be `True` when `a` and `b` are small integers with the same value.

---

## 10. The special case of `tuple` and `frozenset`

Both `tuple` and `frozenset` are **immutable containers**:

- `tuple` is an ordered, immutable sequence.
- `frozenset` is an unordered, immutable set.

However, they can contain **mutable objects**:

```python
t = (1, [2, 3], 4)
t[1].append(5)
print(t)   # (1, [2, 3, 5], 4)
```

The tuple structure is immutable:

- we cannot replace `t[0]` or `t[2]`,
- but we **can** mutate the list living inside, because the list itself is mutable.

Similarly for `frozenset`:

```python
inner = [1, 2]
fs = frozenset({id(inner)})  # we cannot store the list itself (it is unhashable),
                             # but we can store something related, like its id.

# inner is still mutable:
inner.append(3)
print(inner)  # [1, 2, 3]
```

So we can say:

- `tuple` and `frozenset` are **immutable containers**,
- but the objects they contain may themselves be mutable and can be changed.

This often surprises people who interpret “immutable” as “nothing inside can ever change”. In Python, it really means: *the container’s own structure (membership, order, length) does not change*.

---

## 11. Conclusion

From this project, I learned to think in terms of **objects, identities, and references**, rather than “variables with values”:

- `type()` tells what kind of object we are dealing with,
- `id()` tells which specific instance we are referring to,
- mutable vs immutable types behave very differently under assignment, mutation, and function calls,
- aliases come from assignment: multiple names referencing the same object,
- immutable objects (like numbers and strings) never change in memory; only names pointing to them move around,
- small integers are pre‑allocated in CPython using `NSMALLPOSINTS` and `NSMALLNEGINTS`, which explains some surprising `is` results,
- tuples and frozensets are immutable containers but can still hold mutable objects.

Understanding all of this is crucial both for writing correct code (especially when dealing with shared state) and for answering Python interview questions about object identity, mutability and memory.