---

## 🔁 Exercise 3: Control Flow with Loops

### 📌 Overview
In this exercise, you practice control flow using `for` loops, conditional logic (`if-else`), the `enumerate()` function, loop counters, and the `break` statement to search for specific values in a list of integers.

---

### 🎯 Objectives
* Iterate over a list of integers sequentially using a `for` loop.
* Apply conditional logic (`if-else`) to filter and print values based on conditions.
* Leverage `enumerate()` to access both the index and value during iteration.
* Track iteration counts using a counter variable.
* Optimize loop execution using the `break` statement upon finding a target value.

---

### 📝 Step-by-Step Instructions

1. **Basic Iteration:** Create a `for` loop to print each number in `num_list` sequentially.
2. **Filtering:** Add an `if` condition inside the loop to check for numbers greater than `45` and print only those numbers.
3. **Branching Logic:** Update the print statement to output `"Over 45"` for numbers greater than 45, and add an `else` branch to print `"Under 45"`.
4. **Index Tracking:** Update the loop to use `enumerate(num_list)`. Modify the condition to search for the number `36`, printing:  
   `"Number found at position: <index>"`
5. **Counter Initialization:** Declare a variable named `count` initialized to `0` outside and above the loop.
6. **Increment Counter:** Increment `count` by `1` inside the loop on each iteration.
7. **Display Total Iterations:** Print the final value of `count` outside and after the loop.
8. **Loop Interruption:** Add a `break` statement immediately after the print statement inside the `if` block (when number `36` is found) to stop further unnecessary iterations.

---

### 🧠 Key Concepts Covered
* Control flow with `for` loops and `if-else` branching.
* Accessing element indices using `enumerate()`.
* Manual loop counters and iteration tracking.
* Controlling loop execution flow with `break`.