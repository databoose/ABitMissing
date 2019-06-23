import sys
import hashlib
import os
import pickle
import random
import string
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
print banner

writeswitch = raw_input("Write hashes to files? (Y/N):")

if writeswitch not in ['Y','N','y','n']:
    print "Invalid input, exiting..."
    os._exit(1)

# Change the file directory variables to files you know will not change, either by a program or by you.

print "-----------------------------------------------------------------------------"
filedir1 = '/home/databoose/Desktop/Scripts/Winetricks.sh'
print "Hash for ",filedir1,":",hashlib.sha256(open(filedir1,'rb').read()).hexdigest()
ram_hash1 = hashlib.sha256(open(filedir1,'rb').read()).hexdigest()
print "-----------------------------------------------------------------------------"

filedir2 = '/home/databoose/Desktop/WOW Wotlk 3.3.5a/Data/patch.MPQ'
print "Hash for ",filedir2,":",hashlib.sha256(open(filedir2,'rb').read()).hexdigest()
ram_hash2 = hashlib.sha256(open(filedir2,'rb').read()).hexdigest()
print "-----------------------------------------------------------------------------"

filedir3 = '/home/databoose/Desktop/WOW Wotlk 3.3.5a/Data/expansion.MPQ'
print "Hash for ",filedir3,":",hashlib.sha256(open(filedir3,'rb').read()).hexdigest()
ram_hash3 = hashlib.sha256(open(filedir3,'rb').read()).hexdigest()
print "-----------------------------------------------------------------------------"

filedir4 = '/home/databoose/Desktop/League/wine-staging-i386_lol-patched_x86_64-bionic.AppImage'
print "Hash for ",filedir4,":",hashlib.sha256(open(filedir4,'rb').read()).hexdigest()
ram_hash4 = hashlib.sha256(open(filedir4,'rb').read()).hexdigest()
print "-----------------------------------------------------------------------------"

filedir5 = '/home/databoose/Desktop/shotcut.AppImage'
print "Hash for ",filedir5,":",hashlib.sha256(open(filedir5,'rb').read()).hexdigest()
ram_hash5 = hashlib.sha256(open(filedir5,'rb').read()).hexdigest()
print "-----------------------------------------------------------------------------"

filepath = 'hashes.txt'

# Writing values
if writeswitch in ['Y','y']:
    print colored ('Dumping hash values from ram to storage (dirnames.pkl and hashes.pkl)...', 'cyan')
    dirnames = {1:filedir1,2:filedir2,3:filedir3,4:filedir4,5:filedir5}
    output = open('dirnames.pkl', "wb")
    pickle.dump(dirnames, output)
    output.close()
    
    hashes = {
    1:hashlib.sha256(open(filedir1,'rb').read()).hexdigest(),
    2:hashlib.sha256(open(filedir2,'rb').read()).hexdigest(),
    3:hashlib.sha256(open(filedir3,'rb').read()).hexdigest(),
    4:hashlib.sha256(open(filedir4,'rb').read()).hexdigest(),
    5:hashlib.sha256(open(filedir5,'rb').read()).hexdigest()
    }
    output = open('hashes.pkl', "wb")
    pickle.dump(hashes, output)
    output.close()
elif writeswitch not in ['Y','y']:
    print colored ('User doesnt want to write to file, skipping', 'grey')
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
    print colored('Hashes matched on :', 'green'), dirnames[1]
elif ram_hash1 != hashes[1]:
    print colored("Hash mismatch on :", 'red'), dirnames[1]
    print colored("File has either changed naturally from user, or storage device has corrupted file", 'red')

if ram_hash2 == hashes[2]:
    print colored('Hashes matched on :', 'green'), dirnames[2]
elif ram_hash2 != hashes[2]:
    print colored("Hash mismatch on :", 'red'), dirnames[2]
    print colored("File has either changed naturally from user, or storage device has corrupted file", 'red')

if ram_hash3 == hashes[3]:
    print colored('Hashes matched on :', 'green'), dirnames[3]
elif ram_hash3 != hashes[3]:
    print colored("Hash mismatch on :", 'red'), dirnames[3]
    print colored("File has either changed naturally from user, or storage device has corrupted file", 'red')

if ram_hash4 == hashes[4]:
    print colored('Hashes matched on :', 'green'), dirnames[4]
elif ram_hash4 != hashes[4]:
    print colored("Hash mismatch on :", 'red'), dirnames[4]
    print colored("File has either changed naturally from user, or storage device has corrupted file", 'red')

if ram_hash5 == hashes[5]:
    print colored('Hashes matched on :', 'green'), dirnames[5]
elif ram_hash5 != hashes[5]:
    print colored("Hash mismatch on :", 'red'), dirnames[5]
    print colored("File has either changed naturally from user, or storage device has corrupted file", 'red')