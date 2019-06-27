import sys
import hashlib
import os
import pickle
import random
import string
import array
from termcolor import colored


banner = """\
     _    ____  _ _   __  __ _         _             
    / \  | __ )(_) |_|  \/  (_)___ ___(_)_ __   __ _ 
   / _ \ |  _ \| | __| |\/| | / __/ __| | '_ \ / _` |
  / ___ \| |_) | | |_| |  | | \__ \__ \ | | | | (_| |
 /_/   \_\____/|_|\__|_|  |_|_|___/___/_|_| |_|\__, |
                                               |___/ 
"""

os.system('cls' if os.name == 'nt' else 'clear')
print (banner)

writeswitch = input("Write hash files in current directory? This will update the hashes if already stored (Y/N): ")
randcounter = -1
randreplacecounter = -1

if writeswitch not in ['Y','N','y','n']:
    print ("Invalid input, exiting...")
    os._exit(1)

randgenswitch = input("Make a random file? (300KB per file max) (Y/N): ")

if randgenswitch not in ['Y','N','y','n']:
   print ("Invalid input, exiting...")
   os._exit(1)

if randgenswitch in ['Y','y']:
    print(colored("-- Randomized files will be dropped in the current directory of this script --", 'yellow'))
    randstring_array = list()
    array_amount = int(input("Enter how many random files you want to generate (1-5): "))
    if array_amount not in [1,2,3,4,5]:
        print(colored("A number outside the range of 1 to 5 has been entered which is invalid, exiting.", 'red'))
        os._exit(1)
    elif array_amount in [1,2,3,4,5]:
        random.seed(input("Enter random seed for file generation: "))
        for array_amount in range(array_amount):
            n = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(300000))
            randstring_array.append(n)
            randcounter = randcounter + 1
            output = open('randomfile'+str(randcounter), "wb")

            if randcounter == 0:
               print("Array at randcounter[0], dumping to corresponding file")
               pickle.dump(randstring_array[0], output)
            elif randcounter == 1:
                print("Array at randcounter[1], dumping to corresponding file")
                pickle.dump(randstring_array[1], output)
            elif randcounter == 2:
                print("Array at randcounter[2], dumping to corresponding file")
                pickle.dump(randstring_array[2], output)
            elif randcounter == 3:
                print("Array at randcounter[3], dumping to corresponding file")
                pickle.dump(randstring_array[3], output)
            elif randcounter == 4:
                print("Array at randcounter[4], dumping to corresponding file")
                pickle.dump(randstring_array[4], output)
    output.close()
    exit

elif randgenswitch in ['N','n']:
    exit

# Change the file directory variables to files you know will not change, either by a program or by you.

print ("-----------------------------------------------------------------------------")
filedir1 = 'YOUR-FILE-PATH-HERE'
print ("Hash for ",filedir1,":",hashlib.sha256(open(filedir1,'rb').read()).hexdigest())
ram_hash1 = hashlib.sha256(open(filedir1,'rb').read()).hexdigest()
print ("-----------------------------------------------------------------------------")

filedir2 = 'YOUR-FILE-PATH-HERE'
print ("Hash for ",filedir2,":",hashlib.sha256(open(filedir2,'rb').read()).hexdigest())
ram_hash2 = hashlib.sha256(open(filedir2,'rb').read()).hexdigest()
print ("-----------------------------------------------------------------------------")

filedir3 = 'YOUR-FILE-PATH-HERE'
print ("Hash for ",filedir3,":",hashlib.sha256(open(filedir3,'rb').read()).hexdigest())
ram_hash3 = hashlib.sha256(open(filedir3,'rb').read()).hexdigest()
print ("-----------------------------------------------------------------------------")

filedir4 = 'YOUR-FILE-PATH-HERE'
print ("Hash for ",filedir4,":",hashlib.sha256(open(filedir4,'rb').read()).hexdigest())
ram_hash4 = hashlib.sha256(open(filedir4,'rb').read()).hexdigest()
print ("-----------------------------------------------------------------------------")

filedir5 = 'YOUR-FILE-PATH-HERE'
print ("Hash for ",filedir5,":",hashlib.sha256(open(filedir5,'rb').read()).hexdigest())
ram_hash5 = hashlib.sha256(open(filedir5,'rb').read()).hexdigest()
print ("-----------------------------------------------------------------------------")

filepath = 'hashes.txt'

# Writing values
if writeswitch in ['Y','y']:
    print(colored('Dumping hash values from ram to storage (dirnames.pkl and hashes.pkl)...', 'cyan'))
    dirnames = {1:filedir1,2:filedir2,3:filedir3,4:filedir4,5:filedir5}
    output = open('dirnames.pkl', "wb")
    pickle.dump(dirnames, output)
    output.close()
    
    hashes = {
    1:ram_hash1,
    2:ram_hash2,
    3:ram_hash3,
    4:ram_hash4,
    5:ram_hash5
    }
    output = open('hashes.pkl', "wb")
    pickle.dump(hashes, output)
    output.close()

elif writeswitch in ['N','n']:
    print (colored('User doesnt want to write to file, skipping', 'grey'))
    exit
# End of writing values

# Reading values
pkl_file = open("dirnames.pkl", "rb")
dirnames = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open("hashes.pkl", "rb")
hashes = pickle.load(pkl_file)
pkl_file.close()
# End of reading values

if ram_hash1 == hashes[1]:
    print (colored('Hashes matched on :', 'green'), dirnames[1])
elif ram_hash1 != hashes[1]:
    print (colored("Hash mismatch on :", 'red'), dirnames[1])
    print (colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))

if ram_hash2 == hashes[2]:
    print(colored('Hashes matched on :', 'green'), dirnames[2])
elif ram_hash2 != hashes[2]:
    print(colored("Hash mismatch on :", 'red'), dirnames[2])
    print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))

if ram_hash3 == hashes[3]:
    print(colored('Hashes matched on :', 'green'), dirnames[3])
elif ram_hash3 != hashes[3]:
    print(colored("Hash mismatch on :", 'red'), dirnames[3])
    print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))

if ram_hash4 == hashes[4]:
    print(colored('Hashes matched on :', 'green'), dirnames[4])
elif ram_hash4 != hashes[4]:
    print(colored("Hash mismatch on :", 'red'), dirnames[4])
    print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))

if ram_hash5 == hashes[5]:
    print(colored('Hashes matched on :', 'green'), dirnames[5])
elif ram_hash5 != hashes[5]:
    print(colored("Hash mismatch on :", 'red'), dirnames[5])
    print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))
