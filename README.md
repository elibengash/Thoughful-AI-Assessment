# Package Sorting System
This Python project categorizes packages based on their dimensions (width, height, length) and mass. The system helps determine how packages should be dispatched—whether they are standard, special, or rejected based on specific size and weight criteria.

## Functionality
The program classifies packages into three categories:

1. **Bulky Package:**
   - A package is considered **bulky** if:
     - Its volume (calculated as `width * height * length`) is greater than or equal to **1,000,000 cm³**.
     - Or, if any of its dimensions (width, height, or length) is greater than or equal to **150 cm**.

2. **Heavy Package:**
   - A package is considered **heavy** if its mass is greater than or equal to **20 kg**.

3. **Dispatch Categories:**
   - **REJECTED**: If the package is both **bulky** and **heavy**, it will be rejected.
   - **SPECIAL**: If the package is either **bulky** or **heavy**, it will be categorized for special handling.
   - **STANDARD**: If the package is neither bulky nor heavy, it is considered standard and can be dispatched normally.

## Usage

### 1. Running the Program:
- To use the package sorting system, run the Python script.
- The program will prompt you to enter the package details: **width**, **height**, **length**, and **mass**.

### 2. Input Format:
- Enter the **width**, **height**, **length**, and **mass** of the package as positive integers, separated by comma.
- Example input: `200,150,100,25`
  - This represents a package with:
    - Width: 200 cm
    - Height: 150 cm
    - Length: 100 cm
    - Mass: 25 kg

### 3. Output:
- After entering the package details, the program will classify the package into one of the following categories:
  - **REJECTED**: If the package is both **bulky** (volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm) **and** **heavy** (mass ≥ 20 kg).
  - **SPECIAL**: If the package is **either** bulky or heavy.
  - **STANDARD**: If the package is **neither** bulky nor heavy.

