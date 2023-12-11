import os
import argparse
import hashlib
#Import functions from hashfunctions.py file
from hashfunctions import create_hash, store_hash, compare_hash

#Creating arguments for use with script
parser=argparse.ArgumentParser(description="Create and compare hash files")
#Filepath argument to run against file
parser.add_argument("file_path",
                    help="Path to file.",)
#Hash type to use on file, required with default of md5
parser.add_argument("hash_type",
                    choices=hashlib.algorithms_available,
                    help="Hash type.")
#Argument to save has into hashes file
parser.add_argument("-s", "--save",
                    help="Save hash value to hashes file.",
                    action="store_true")
#Argument to compare generated hash of filepath to stored hashes file
parser.add_argument("-c", "--compare",
                    help="Compare hash value to hash value in hashes file.",
                    action="store_true")
#Argument to store hash into custom file if needed, with default set to hashes.txt
parser.add_argument("-hf", "--hashes_file",
                    help="Hashes file.",
                    default="hashes.txt")
args=parser.parse_args()

#Creating variables for arguments entered
file_path = args.file_path
hash_type = args.hash_type
hashes_file = args.hashes_file

#Creating hashes file if it does not exist
if not os.path.exists(hashes_file):
    with open(hashes_file, "w") as f:
        pass

#Script to be run if save argument used
if args.save:
    hash_value = create_hash(file_path, hash_type)
    store_hash(file_path, hash_value, hashes_file)
    print(f"Hash value: {hash_value}")
#Script to be run if compare argument used
elif args.compare:
    hash_value = create_hash(file_path, hash_type)
    #If return is True
    if compare_hash(file_path, hash_value, hashes_file):
        print("Hash values match.")
    #If return is False
    else:
        print("Hash values do not match.")
#Default script to be run if minimum file and hash algorithm provided
else:
    hash_value = create_hash(file_path, hash_type)
    print(f"Hash value: {hash_value}")




