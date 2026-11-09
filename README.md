# Python Stack

Read the Abstract Data Types lecture (Stack section) before you start.
https://drive.google.com/file/d/1jXGQdSvuUYjGXl-PUuHMUzKWEBGQoARL/view?usp=sharing

**Rules for this assignment**

- The stack is an **array of 10 elements** and a **pointer** called `TopOfStack`.
- Do **not** use `.append()` or `.pop()` inside `Push()` and `Pop()`.
  Change `TopOfStack` yourself and use `Stack[TopOfStack]`. The tests check for this.
- Functions **return** their answer — do not print.
- Every function that changes `Stack` or `TopOfStack` needs this line at the top:
  `global Stack, TopOfStack`

**How the stack looks**

`TopOfStack` is the **index of the top item**. When the stack is empty there
is no top item, so `TopOfStack` is `-1`.

    After Push(15), Push(27), Push(40):

    index:   0    1    2    3    4    5    6    7    8    9
    Stack: [15,  27,  40,  -1,  -1,  -1,  -1,  -1,  -1,  -1]
                       ↑
                  TopOfStack = 2

---

## Exercise 1

**Problem:**

Set up the stack:

- `Stack` → a global array of **10** elements, all set to `-1`
- `TopOfStack` → a global integer, set to `-1`

Then write two functions:

`IsEmpty()`

- Return `True` if the stack is empty (`TopOfStack` is `-1`), otherwise `False`

`IsFull()`

- Return `True` if the stack is full, otherwise `False`
- The last index of a 10-element array is **9** — so the stack is full when
  `TopOfStack` is `9`

**Example:**

    Input:
      print(Stack)
      print(TopOfStack)
      print(IsEmpty())
      print(IsFull())

    Output:
      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
      -1
      True
      False

*Hint:* do **not** use `len(Stack)` — the array always has 10 elements, even
when the stack is empty. Only `TopOfStack` tells you how full it is.

---

## Exercise 2

**Problem:**

`Push(Item)`

Add `Item` to the **top** of the stack.

1. If the stack is full, return `False` (you can use `IsFull()`)
2. Otherwise add 1 to `TopOfStack`
3. Store `Item` at `Stack[TopOfStack]`
4. Return `True`

**Example:**

    Input:
      print(Push(15))
      print(Push(27))
      print(Stack[0], Stack[1])
      print(TopOfStack)

    Output:
      True
      True
      15 27
      1

What happens step by step:

    Push(15):  TopOfStack -1 → 0    Stack[0] = 15
    Push(27):  TopOfStack  0 → 1    Stack[1] = 27

**Careful with the order:** move `TopOfStack` up **first**, then store.
If you store first, you write into `Stack[-1]` — the wrong place!

---

## Exercise 3

**Problem:**

`Pop()`

Remove the **top** item and return it.

1. If the stack is empty, return `-1` (you can use `IsEmpty()`)
2. Otherwise read the item at `Stack[TopOfStack]` and keep it in a variable
3. Take 1 off `TopOfStack`
4. Return the item

**Example:**

    Stack before:  [10, 20, 30, -1, ...]    TopOfStack = 2

    Input:
      print(Pop())
      print(TopOfStack)
      print(Pop())
      print(Pop())
      print(Pop())

    Output:
      30
      1
      20
      10
      -1

The last `Pop()` returns `-1` because the stack is empty.

**Careful with the order:** read the item **first**, then move
`TopOfStack` down. If you move first, you return the wrong item.

---

## Exercise 4

**Problem:**

Write two small functions.

`Peek()`

- Return the top item **without removing it** — `TopOfStack` must not change
- If the stack is empty, return `-1`

`Size()`

- Return how many items are in the stack

**Example:**

    Stack:  [8, 3, -1, ...]    TopOfStack = 1

    Input:
      print(Peek())
      print(Peek())
      print(Size())

    Output:
      3
      3
      2

*Hint:* if `TopOfStack` is 1, there are **2** items (index 0 and index 1).
Is there a simple sum that turns `TopOfStack` into the size?

---

## Exercise 5

**Problem:**

`ReverseWord(Word)`

Use **your stack** to reverse a word. `Word` has at most 10 letters.

1. **Empty the stack first:** set `TopOfStack` to `-1`
2. Push every letter of `Word` onto the stack
3. Pop the letters one by one — joining them into a new string —
   until the stack is empty
4. Return the new string

Do **not** use `[::-1]` or `reversed()`. The point is to use the stack!

**Example:**

    Input:                       Output:
      ReverseWord("HELLO")         "OLLEH"
      ReverseWord("Python")        "nohtyP"
      ReverseWord("a")             "a"
      ReverseWord("")              ""

How it works for `"CAT"`:

    Push C, Push A, Push T      Stack:  C  A  T   ← T is on top

    Pop → T                     Result: "T"
    Pop → A                     Result: "TA"
    Pop → C                     Result: "TAC"

The **last** letter in is the **first** letter out — that is why a stack
turns the word around.

---
