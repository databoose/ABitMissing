import sys
import hashlib
import os
import pickle
import random
import string
import datetime
import array
from termcolor import colored

if __name__ == "__main__":
 try:
   pkl_file = open("timestamp.pkl", "rb")
   timestamp_stored = pickle.load(pkl_file)
   pkl_file.close()
 except FileNotFoundError:
   exit

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
 currentDT = datetime.datetime.now()

 try:
    print(colored("Date of latest hash generation :", 'green'), timestamp_stored)
    print (" ")
 except NameError:
    exit
    
 writeswitch = input("Write hash files in current directory? This will update the hashes if already stored (Y/N): ")
 randcounter = -1
 randreplacecounter = -1

 if writeswitch in ['Y','y']:
     randgenswitch = input("Make random file(s)? (Y/N): ")

 elif writeswitch in ['N','n']:
     randgenswitch = 'N'

 elif writeswitch not in ['Y','N','y','n']:
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
         randfilesize = int(input("Enter size of each random file (in kilobytes): "))
     for array_amount in range(array_amount):
            print(colored("-- Generating random data --", 'green'))
            if (randfilesize * 1000 > 30000):
                print(colored("Requested filesize detected above 30MB, this may take a while",'yellow'))
            elif (randfilesize * 1000 < 30000):
                exit

            rand_data = ''.join(random.choice(string.ascii_letters + string.digits + string.hexdigits) for _ in range(randfilesize * 1000))
            randstring_array.append(rand_data)
            randcounter = randcounter + 1
            output = open('randomfile'+str(randcounter), "wb")

            if randcounter == 0:
              print("Dumping randstring_array[0]")
              pickle.dump(randstring_array[0], output)
            elif randcounter == 1:
              print("Dumping randstring_array[1]")
              pickle.dump(randstring_array[1], output)
            elif randcounter == 2:
              print("Dumping randstring_array[2]")
              pickle.dump(randstring_array[2], output)
            elif randcounter == 3:
              print("Dumping randstring_array[3]")
              pickle.dump(randstring_array[3], output)
            elif randcounter == 4:
              print("Dumping randstring_array[4]")
              pickle.dump(randstring_array[4], output)
     output.close()
     exit

 elif randgenswitch in ['N','n']:
     exit

 elif randgenswitch not in ['Y','N','y','n']:
    print ("Invalid input, exiting...")
    os._exit(1)

# Change the file directory variables to files you know will not change, either by a program or by you.
 try:
   print ("-----------------------------------------------------------------------------")
   filedir1 = 'randomfile0'
   print ("Hash for ",filedir1,":",hashlib.sha256(open(filedir1,'rb').read()).hexdigest())
   ram_hash1 = hashlib.sha256(open(filedir1,'rb').read()).hexdigest()
   print ("-----------------------------------------------------------------------------")
 except FileNotFoundError as error:
     print ("File",filedir1,"not found")
     print (colored("Exiting due to error...", 'red'))
     print ("-----------------------------------------------------------------------------")
     os._exit(1)

 try:
   filedir2 = 'randomfile1'
   print ("Hash for ",filedir2,":",hashlib.sha256(open(filedir2,'rb').read()).hexdigest())
   ram_hash2 = hashlib.sha256(open(filedir2,'rb').read()).hexdigest()
   print ("-----------------------------------------------------------------------------")
 except FileNotFoundError as error:
     print ("File",filedir2,"not found")
     print (colored("Exiting due to error...", 'red'))
     print ("-----------------------------------------------------------------------------")
     os._exit(1)

 try:
   filedir3 = 'randomfile2'
   print ("Hash for ",filedir3,":",hashlib.sha256(open(filedir3,'rb').read()).hexdigest())
   ram_hash3 = hashlib.sha256(open(filedir3,'rb').read()).hexdigest()
   print ("-----------------------------------------------------------------------------")
 except FileNotFoundError as error:
     print ("File",filedir3,"not found")
     print (colored("Exiting due to error...", 'red'))
     print ("-----------------------------------------------------------------------------")
     os._exit(1)

 try:
   filedir4 = 'randomfile3'
   print ("Hash for ",filedir4,":",hashlib.sha256(open(filedir4,'rb').read()).hexdigest())
   ram_hash4 = hashlib.sha256(open(filedir4,'rb').read()).hexdigest()
   print ("-----------------------------------------------------------------------------")
 except FileNotFoundError as error:
     print ("File",filedir4,"not found")
     print (colored("Exiting due to error...", 'red'))
     print ("-----------------------------------------------------------------------------")
     os._exit(1)

 try:
   filedir5 = 'randomfile4'
   print ("Hash for ",filedir5,":",hashlib.sha256(open(filedir5,'rb').read()).hexdigest())
   ram_hash5 = hashlib.sha256(open(filedir5,'rb').read()).hexdigest()
   print ("-----------------------------------------------------------------------------")
 except FileNotFoundError as error:
     print ("File",filedir5,"not found")
     print (colored("Exiting due to error...", 'red'))
     print ("-----------------------------------------------------------------------------")
     os._exit(1)


# Writing values
 if writeswitch in ['Y','y']:
     print(colored('Dumping hash values from ram to storage (hashes.pkl and timestamp.pkl)...', 'cyan'))
     hashes = {
     1:ram_hash1,
     2:ram_hash2,
     3:ram_hash3,
     4:ram_hash4,
     5:ram_hash5
     }
     timestamp_stored = currentDT.strftime("%Y-%m-%d %H:%M:%S")
     output = open('hashes.pkl', "wb")
     pickle.dump(hashes, output)
     output.close()

     output = open ('timestamp.pkl', "wb")
     pickle.dump(timestamp_stored, output)
     output.close()

 elif writeswitch in ['N','n']:
     print (colored('User doesnt want to write to file, skipping', 'grey'))
     exit
# End of writing values

# Reading values
 pkl_file = open("hashes.pkl", "rb")
 hashes = pickle.load(pkl_file)
 pkl_file.close()
# End of reading values

 if ram_hash1 == hashes[1]:
     print (colored('Hashes matched on :', 'green'), filedir1)
 elif ram_hash1 != hashes[1]:
     print (colored("Hash mismatch on :", 'red'), filedir1)
     print (colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))

 if ram_hash2 == hashes[2]:
     print(colored('Hashes matched on :', 'green'), filedir2)
 elif ram_hash2 != hashes[2]:
     print(colored("Hash mismatch on :", 'red'), filedir2)
     print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))

 if ram_hash3 == hashes[3]:
     print(colored('Hashes matched on :', 'green'), filedir3)
 elif ram_hash3 != hashes[3]:
     print(colored("Hash mismatch on :", 'red'), filedir3)
     print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))

 if ram_hash4 == hashes[4]:
     print(colored('Hashes matched on :', 'green'),filedir4)
 elif ram_hash4 != hashes[4]:
     print(colored("Hash mismatch on :", 'red'), filedir4)
     print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))

 if ram_hash5 == hashes[5]:
     print(colored('Hashes matched on :', 'green'), filedir5)
 elif ram_hash5 != hashes[5]:
     print(colored("Hash mismatch on :", 'red'), filedir5)
     print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))
