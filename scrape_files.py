import os
import yaml

def is_text_file(file_path):
    # List of text file extensions
    text_extensions = ['.txt', '.md', '.py', '.js', '.html', '.css', '.php', '.yml', '.yaml', '.json', '.xml', '.csv', '.twig', '.rb', '.erb']
    # List of image file extensions to explicitly exclude
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico', '.webp']
    
    file_ext = os.path.splitext(file_path)[1].lower()
    return file_ext in text_extensions and file_ext not in image_extensions

def scrape_files_and_store(paths, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for path in paths:
            if path.strip().startswith('!'):
                print(f"Skipping path: {path}")
                continue  # Skip this path if it starts with '!'
            
            path = path.strip()
            print(f"Processing path: {path}")
            
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if is_text_file(file_path):
                        try:
                            with open(file_path, 'r', encoding='utf-8') as infile:
                                outfile.write(f"Contents of {file_path}:\n")
                                outfile.write(infile.read())
                                outfile.write("\n\n")
                        except Exception as e:
                            print(f"Error reading {file_path}: {e}")
                    else:
                        print(f"Skipping non-text file: {file_path}")

def load_paths_from_yaml(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config['paths']

if __name__ == "__main__":
    yaml_file = 'paths.yml'
    output_file = 'output.txt'
    
    paths = load_paths_from_yaml(yaml_file)
    scrape_files_and_store(paths, output_file)
    print(f"Contents from all text files have been stored in {output_file}")

