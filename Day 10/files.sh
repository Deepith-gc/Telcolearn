# Display options to the user
echo "Enter task to be performed:"
echo "1) File creation"
echo "2) Delete file"
echo "3) Move file"

# Read the user's choice
read -p "Enter your choice (1/2/3): " ch

# Perform actions based on the user's choice
case $ch in
1)
  # Option 1: Create a new file
  read -p "Enter filename (without extension): " name
  touch "$name.txt"
  echo "File '$name.txt' created successfully."
  ;;
2)
  # Option 2: Delete a file (first check if it exists)
  ls -a
  read -p "Enter the name of the file you want to delete (including extension): " name
  if [ -f "$name" ]; then
    rm "$name"
    echo "File '$name' deleted successfully."
  else
    echo "Error: File '$name' does not exist."
  fi
  ;;
3)
  # Option 3: Move a file to a different directory
  ls -a
  read -p "Enter the name of the file you want to move (including extension): " name
  if [ -f "$name" ]; then
    read -p "Enter the target directory where you want to move the file: " target_dir
    if [ -d "$target_dir" ]; then
      mv "$name" "$target_dir"
      echo "File '$name' moved to '$target_dir'."
    else
      echo "Error: Directory '$target_dir' does not exist."
    fi
  else
    echo "Error: File '$name' does not exist."
  fi
  ;;
*)
  echo "Invalid choice. Please enter 1, 2, or 3."
  ;;
esac

