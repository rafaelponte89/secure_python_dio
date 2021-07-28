import hashlib

# files defined in tuples
tuple_files =('a.txt','b.txt')

# two objects hashes created in type specified
tuple_hashes = (hashlib.new('ripemd160'),hashlib.new('ripemd160'))

# reading of files in bits and update with objects hashes created previously
tuple_hashes[0].update(open(tuple_files[0],'rb').read())
tuple_hashes[1].update(open(tuple_files[1],'rb').read())

# summary of hash file and comparison
if tuple_hashes[0].digest() == tuple_hashes[1].digest():
    print('The files are equals')

else:
    print('The files are different')

print(f'File {tuple_files[0]} | Hash {tuple_hashes[0].hexdigest()}')
print(f'File {tuple_files[1]} | Hash {tuple_hashes[1].hexdigest()}')

# tip
# note Hash works in bit level
