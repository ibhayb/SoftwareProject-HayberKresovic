# Task Variables Creation Tool for JACK3

This tool simplifies the process of creating and managing variables for JACK3 tasks. Instead of manually adding variables through the web interface, which can be time-consuming and error-prone, this tool allows you to generate and format variables programmatically, then inject them into the task's XML file. This is especially useful for algorithm-related tasks, where variables often depend on each other.

## Overview

### Requirements

- Python 3.10>=

### Key Features

1. **Automated Variable Generation**: Generate variables dynamically for different subtasks using Python functions.
2. **Custom Formatting**: Convert Python data structures into JACK3-compatible formats (e.g., lists of numbers, strings, or intervals).
3. **XML Integration**: Add variables directly to an XML file representing the task, which can be uploaded back into JACK3.

### Components

- **`formatter_for_copy_paste_export_to_jack3.py`**: Provides utility functions to convert Python lists, arrays, or intervals into JACK3-compatible string formats.
- **`formatter_to_xml.py`**: Handles XML manipulation, including:
  - Adding new variables (`format_to_xml`).
  - Clearing existing variables (`clear_variable_declarations`).
- **Task-specific files (e.g., `binary_search_tasks.py`)**: Contain task-specific logic for generating variables and serve as examples of how the above components can be used.

---

## How It Works

### 1. Task-Specific Variable Generation

Each subtask is implemented as a function in a task-specific file (e.g., `binary_search_tasks.py`). These functions return an array of tuples, where each tuple contains:

1. The name of the variable list.
2. The name of the single variable.
3. A formatted string of variable values compatible with JACK3.

#### Example

A function generating variables for a binary search task might return:

```python
[
    ("arrays", "array", "list('[1, 2, 3]', '[4, 5, 6]')"),
    ("ks", "k", "list('1', '4')")
]
```

---

### 2. Custom Formatting

This section handles converting Python data into JACK3-compatible strings using utility functions from `formatter_for_copy_paste_export_to_jack3.py`.

#### Key Formatting Functions

- **`format_list_of_arrays`**: Converts a list of Python lists into a JACK3-compatible list of arrays.

  - **Input**: `[[1, 2, 3], [4, 5, 6]]`
  - **Output**: `"list('[1, 2, 3]', '[4, 5, 6]')"`

- **`format_list_of_strings`**: Converts a list of strings into a JACK3-compatible list.

  - **Input**: `["apple", "banana", "cherry"]`
  - **Output**: `"list('apple', 'banana', 'cherry')"`

- **`format_list_of_intervals`**: Converts a list of intervals into a JACK3-compatible interval format.
  - **Input**: `[(1, 3), (4, 6)]`
  - **Output**: `"intervals('[1, 3]', '[4, 6]')"`

---

### 3. Injecting Variables into XML

To insert the formatted variables into a JACK3 task XML file, use functions from `formatter_to_xml.py`.

#### Adding Variables

The `format_to_xml` function appends generated variables to an XML file. The XML file to which this will be appended should be downloaded from the JACK3 website. Either you can use an empty new created task to add the variables or you can use an already existing task which already has variables. Be aware there are no checks if the variables name already exists. The formatter will simply add as XML what you provide through the name_input_array.

```python
format_to_xml(folder_path, name_input_array, question_number, question_amount)
```

- **Parameters**:
  - `folder_path`: Path to the XML file.
  - `name_input_array`: Array of tuples containing the variable data.
  - `question_number`: The specific question number to modify.
  - `question_amount`: Number of questions to generate variables for.

#### Clearing Variables

To clear all existing variables in the XML, use:

```python
clear_variable_declarations(folder_path)
```

---

## Example: Binary Search Task

The `binary_search_tasks.py` file demonstrates how to create subtasks for a binary search algorithm. Each subtask generates a specific set of variables required for testing or teaching binary search concepts.

### Subtask Functions

- **Second Recursive Call**: Generates variables related to a specific recursive call.
- **Interval Tracking**: Tracks intervals checked during binary search.
- **Mid Values**: Captures values at specific midpoints.
- **Mid Value Comparison Count**: Tracks the number of mid-value comparisons.

### Usage

1. Generate variables for a subtask:

```python
folder_path = "/SomePath/BinarySearchTask"
clear_variable_declarations(folder_path)
num_calls = 50
question_number = 1

result = generate_task_for_second_recursive_call(question_number, num_calls)
format_to_xml(folder_path, result, question_number, num_calls)
```
