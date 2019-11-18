import os

# Create directory path (If not exist)


def create_project_directory(directory):
    if not os.path.exists(directory):
        print("Creating project directory \"{}\"".format(directory))
        os.makedirs(directory)
    else:
        print("Already exist this \"{}\" directory.Please try another name.".format(directory))
        return directory

# Create queue and crawled files [(If not exist)]


def created_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name , 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Create new files


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)

# Add data on the existing file


def append_data(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete content path


def clear_file_contents(path):
    with open(path, 'w') as f:
        f.close()

# Read a file and convert it into a index/content list


def file_to_index(filename):
    result = set()
    with open(filename, 'rt') as lines:
        for line in lines:
            result.add(line.replace('\n', ''))
    return result
# Save index data on a file through iteration set


def set_to_file(file, links):
    with open(file,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")
    
