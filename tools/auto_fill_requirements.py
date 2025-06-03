import os

IGNORED_DIRS = {'tools', '.git', '__pycache__', 'lcal'}

def read_requirements(file_path):
    """Read and return a set of requirements from the given file path."""
    if not os.path.isfile(file_path):
        return set()
    with open(file_path, 'r') as f:
        return set(line.strip() for line in f if line.strip() and not line.startswith('#'))

def main(): 
    base_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    base_req_path = os.path.join(base_dir, 'requirements.txt')

    all_requirements = read_requirements(base_req_path)

    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path) and item not in IGNORED_DIRS:
            req_file = os.path.join(item_path, 'requirements.txt')
            all_requirements.update(read_requirements(req_file))

    with open(base_req_path, 'w') as f:
        for requirement in sorted(all_requirements):
            f.write(requirement + '\n')

if __name__ == '__main__':
    main()
