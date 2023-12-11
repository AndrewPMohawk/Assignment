import hashlib
import os

#Function for creation of hash based on filepath and hash argument
def create_hash(file_path, hash_type):
    #Filepath argument to be read as binary
    with open(file_path, "rb") as f:
        binary = f.read()
    #Creating new hash object with hash algorithm argument
    hash = hashlib.new(hash_type)
    #Applying algorithm to binary variable and saving it to hash variable
    hash.update(binary)
    #returning hash variable as hexadecimal value
    return hash.hexdigest()

#Function to save hash to file specified in Main script
def store_hash(file_path, hash_value, hashes_file):
    #Open file with writing option
    with open(hashes_file, "a") as f:
        f.write(f"{hash_value} {file_path}\n")

#Function to compare filepath argument hash with stored hashes in file 
def compare_hash(file_path, hash_value, hashes_file):
    #Opening hashes file with read option
    with open(hashes_file, "r") as f:
        #Loop to compare argument file hash with every line in hashes file and return true or false
        for line in f:
            if line.startswith(hash_value):
                return file_path == line.split()[1]
    return False
