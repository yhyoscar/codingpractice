import os

def print_all_directory(path):
    if os.path.isdir(path):
        child = os.listdir(path)
        if len(child) > 0:
            for x in child:
                print_all_directory(os.path.join(path, x))
        else:
            print(path)
    else:
        print(path)

print_all_directory('../algo/tensorfow-rbm/')

