import os
import subprocess

# Get the name of the current script file (without the .py extension)
current_script = os.path.basename(__file__).replace('.py', '')

# Traverse the current directory and its subdirectories
for root, _, files in os.walk("."):
    for file in files:
        # Only consider Python files, excluding the current script
        if file.endswith(".py") and file[:-3] != current_script:
            module_name = file[:-3]  # Remove .py extension
            print(f"Generating documentation for {module_name} in {root}")
            try:
                # Run pydoc to generate documentation
                subprocess.run(["python", "-m", "pydoc", "-w", module_name], cwd=root)
                print(f"Documentation generated for {module_name}.html in {root}")
            except Exception as e:
                print(f"Failed to generate documentation for {module_name}: {e}")
