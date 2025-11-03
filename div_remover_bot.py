import os
import sys
from bs4 import BeautifulSoup

def process_html_file(file_path, class_to_remove):
    """
    Opens an HTML file, removes all divs with the specified class,
    and overwrites the original file with the cleaned content.
    """
    try:
        # Read the file
        # Use 'utf-8' encoding, as it's standard for HTML
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse the HTML
        soup = BeautifulSoup(content, 'html.parser')

        # Find all <div> elements with the specified class
        # soup.find_all() will find tags even if they have multiple classes
        # e.g., <div class="abcde otherclass"> will be found
        divs_to_remove = soup.find_all('div', class_=class_to_remove)

        if not divs_to_remove:
            # No matching divs found, no need to rewrite the file
            print(f"--- No matching divs in: {file_path}")
            return 0 # Return 0 for no changes

        num_removed = len(divs_to_remove)
        print(f"+++ Found and removed {num_removed} div(s) in: {file_path}")

        # Remove each found div from the parse tree
        for div in divs_to_remove:
            div.decompose() # .decompose() removes the tag and all its contents

        # Write the modified HTML back to the original file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        return num_removed

    except Exception as e:
        print(f"[ERROR] Could not process file {file_path}: {e}")
        return 0

def main():
    # 1. Check for command-line argument
    if len(sys.argv) < 2:
        print("Error: You must provide the class name to remove.")
        print("Usage: python3 bot.py \"<class_name>\" [optional_directory]")
        sys.exit(1) # Exit the script with an error code

    class_name = sys.argv[1]
    
    # 2. Define the starting directory
    # If a second argument is given, use it as the path.
    # Otherwise, default to the current directory ('.').
    start_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
    
    # Get the absolute path for clearer output
    start_dir = os.path.abspath(start_dir)
    
    print(f"Starting bot...")
    print(f"Target directory: {start_dir}")
    print(f"Looking for all <div> elements with class='{class_name}'")
    print("-" * 30)

    total_files_processed = 0
    total_divs_removed = 0

    # 3. Walk through all directories and sub-directories
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            # 4. Check if the file is an HTML file
            if file.endswith(('.html', '.htm')):
                file_path = os.path.join(root, file)
                total_files_processed += 1
                
                # 5. Process the file
                num_removed = process_html_file(file_path, class_name)
                total_divs_removed += num_removed

    print("-" * 30)
    print("Scan complete.")
    print(f"Total HTML files found: {total_files_processed}")
    print(f"Total <div> elements removed: {total_divs_removed}")

if __name__ == "__main__":
    main()