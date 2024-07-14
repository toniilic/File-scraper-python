import os
import yaml

def scrape_files_and_store(paths, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for path in paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(f"Contents of {file_path}:\n")
                            outfile.write(infile.read())
                            outfile.write("\n\n")
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

def load_paths_from_yaml(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config['paths']

if __name__ == "__main__":
    yaml_file = 'paths.yml'
    output_file = 'output.txt'
    
    paths = load_paths_from_yaml(yaml_file)
    scrape_files_and_store(paths, output_file)
    print(f"Contents from all files have been stored in {output_file}")
