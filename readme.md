#I, Andrew Prodan/000281525, hereby state that this assignment is solely my work and no other student helped or did my work for me.
Code copied or learned from materials beyond this course is to be referenced and credited as such at the end.

Script consisting of stored functions to create, store, and compare hashes to those stored in a file based on a file and algorithm used as an argument.

How to use:

usage: workshoptest.py [-h] [-s] [-c] [-hf HASHES_FILE]
                       file_path
                       {blake2s,sha256,sha3_384,sha512_224,sha384,shake_128,md4,shake_256,md5,mdc2,sha512,sha3_224,sha3_512,whirlpool,ripemd160,sha224,md5-sha1,sha512_256,sm3,sha1,blake2b,sha3_256}

example: 

python main.py examplefile md5 -c -s -hf hashed_storage.txt

Create and compare hash files

positional arguments:
  file_path             Path to file.
  {blake2s,sha256,sha3_384,sha512_224,sha384,shake_128,md4,shake_256,md5,mdc2,sha512,sha3_224,sha3_512,whirlpool,ripemd160,sha224,md5-sha1,sha512_256,sm3,sha1,blake2b,sha3_256}
                        Hash type.

options:
  -h, --help            show this help message and exit
  -s, --save            Save hash value to hashes file.
  -c, --compare         Compare hash value to hash value in hashes file.
  -hf HASHES_FILE, --hashes_file HASHES_FILE
                        Hashes file.



Resources used:
https://bobbyhadz.com/blog/python-calculate-md5-hash-checksum-of-file
https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
https://docs.python.org/3/library/hashlib.html
https://docs.python.org/3/library/functions.html?highlight=open#open
https://www.geeksforgeeks.org/hashlib-module-in-python/
https://documentation.help/Python-3.7/hashlib.html
https://chat.openai.com/ -ChatGPT

