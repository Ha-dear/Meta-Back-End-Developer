# Lab Instructions: Functions, Loops, and Data Structures

In this lab, you will complete a menu ordering system that allows users to input three choices from a select menu. Your task is to complete the menu system so that it calculates and returns the final bill for the user.

---

## 💡 Tips Before You Begin

### To view your code and instructions side-by-side in VS Code:
* Select **View** -> **Editor Layout** -> **Two Columns**.
* Right-click this `README.md` file and select **Open Preview**.
* Select your Python file in the file tree to open it.
* Drag your Python file tab over to the second column.

### To run your Python code:
* Right-click the file inside the file tree and select **Run Python File in Terminal**.
* Alternatively, click the **Play button** in the upper right-hand corner of VS Code.
* You can also use the standard `python3` command directly in your terminal.

---

## 🎯 Activity Objectives
1. **Create** new functions to solve specific problems.
2. **Iterate** over different data collections using `for` loops.
3. **Utilize** data structures to store, retrieve, and loop over data.

---

## 📝 Exercise Instructions

1. **Open** the `ordering_system.py` file located under the project folder.
2. **Run** the script and enter three products of your choice based on the menu (e.g., `1 = espresso`, `2 = coffee`, etc.).
3. **Open** a new terminal (**Terminal > New Terminal**) and execute the following command to run the script:
   ```bash
   python3 ordering_system.py
   ```
4. **Implement** a new function called `calculate_subtotal`:
   * It must accept **one argument** (the order list).
   * It must return the **sum of the prices** of the items in that list.
5. **Implement** a function called `calculate_tax`:
   * It must calculate the tax based on the subtotal.
   * The tax rate is **15%** of the overall bill.
6. **Implement** a function called `summarize_order`:
   * It must return a **list of names** of the items ordered and the **total amount** (including tax).
   * The final output should display both the **name and price** of each ordered item.

---

## 🚀 Final Step: Submit Your Code

* Save your file (**File -> Save**).
* Click the **Submit Assignment** button in your Lab toolbar.
* Your code will be autograded, and you can check your feedback in the **Grades** or **My Submission** tab.
