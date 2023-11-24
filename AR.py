import tkinter as tk


def calculate_operation():
  # Retrieve fuzzy sets A and B from entry fields
  fuzzy_set_a = [float(x) for x in entry_set_a.get().split(",")]
  fuzzy_set_b = [float(x) for x in entry_set_b.get().split(",")]

  # Perform the selected fuzzy set operation
  operation = operation_var.get()
  result = []

  if operation == "Sum (A+B)":
    result = [max(a, b) for a, b in zip(fuzzy_set_a, fuzzy_set_b)]
  elif operation == "Difference (A-B)":
    result = [max(0, a - b) for a, b in zip(fuzzy_set_a, fuzzy_set_b)]
  elif operation == "Cartesian Product":
    result = [(a, b) for a in fuzzy_set_a for b in fuzzy_set_b]
  elif operation == "Union (AUB)":
    result = [max(a, b) for a, b in zip(fuzzy_set_a, fuzzy_set_b)]
  elif operation == "Intersection of A and B":
    result = [min(a, b) for a, b in zip(fuzzy_set_a, fuzzy_set_b)]
  elif operation == "Complement of A":
    result = [1 - a for a in fuzzy_set_a]

  # Display the result
  result_label.config(text=f"Result: {result}")


# GUI setup
root = tk.Tk()
root.title("Fuzzy Logic System")

# Entry fields for fuzzy sets A and B
entry_set_a = tk.Entry(root, width=30)
entry_set_a.grid(row=0, column=0, padx=10, pady=10)
label_set_a = tk.Label(root, text="Fuzzy Set A (comma-separated values):")
label_set_a.grid(row=0, column=1, padx=10, pady=10)

entry_set_b = tk.Entry(root, width=30)
entry_set_b.grid(row=1, column=0, padx=10, pady=10)
label_set_b = tk.Label(root, text="Fuzzy Set B (comma-separated values):")
label_set_b.grid(row=1, column=1, padx=10, pady=10)

# Dropdown for selecting the fuzzy set operation
operations = [
    "Sum (A+B)", "Difference (A-B)", "Cartesian Product", "Union (AUB)",
    "Intersection of A and B", "Complement of A"
]
operation_var = tk.StringVar(value=operations[0])
operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

# Button to calculate the selected fuzzy set operation
calculate_button = tk.Button(root,
                             text="Calculate",
                             command=calculate_operation)
calculate_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

# Label to display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

# Run the GUI
root.mainloop()
