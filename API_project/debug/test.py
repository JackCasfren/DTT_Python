import sys
import os

# Get the path to the API_project directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Append the path to the interactions directory
interactions_path = os.path.join(project_root, 'interactions')
sys.path.append(interactions_path)

#print(f"Interactions path: {interactions_path}")
#print(f"System path: {sys.path}")

# Now try to import
from full_pantry import get_pantry_data

# Use the function
print(get_pantry_data())