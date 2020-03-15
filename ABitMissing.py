import sys
import argparse
import hashlib
import os
import pickle
import random
import string
import datetime
import array
import multiprocessing
from multiprocessing import Process
from time import sleep
from termcolor import colored


if __name__ == "__main__":
    try:
        pkl_file = open("timestamp.pkl", "rb")
        timestamp_stored = pickle.load(pkl_file)
        pkl_file.close()
    except FileNotFoundError:
        exit

    arglist = sys.argv
    try:
        if arglist[1] == str('--wipe-data'):
            wipe_answer = input(colored("Are you sure you want to delete the random files, hashes and timestamp? (Y/N): ", 'red'))

            if wipe_answer in ['Y', 'y']:
                print("Deleting randomfile0...")
                try:
                    os.remove('randomfile0')
                except FileNotFoundError:
                    print(colored("File does not exist, continuing", 'yellow'))
                sleep(0.8)

                print("Deleting randomfile1...")
                try:
                    os.remove('randomfile1')
                except FileNotFoundError:
                    print(colored("File does not exist, continuing", 'yellow'))
                sleep(0.8)

                print("Deleting randomfile2...")
                try:
                    os.remove('randomfile2')
                except FileNotFoundError:
                    print(colored("File does not exist, continuing", 'yellow'))
                sleep(0.8)

                print("Deleting randomfile3...")
                try:
                    os.remove('randomfile3')
                except FileNotFoundError:
                    print(colored("File does not exist, continuing", 'yellow'))
                sleep(0.8)

                print("Deleting randomfile4...")
                try:
                    os.remove('randomfile4')
                except FileNotFoundError:
                    print(colored("File does not exist, continuing", 'yellow'))
                sleep(0.8)

                print("Deleting timestamp...")
                try:
                    os.remove('timestamp.pkl')
                except FileNotFoundError:
                    print(colored("File does not exist, continuing", 'yellow'))
                sleep(0.8)

                print("Deleting hashes...")
                try:
                    os.remove('hashes.pkl')
                except FileNotFoundError:
                    print(colored("File does not exist, continuing", 'yellow'))
                print("Process done, going to main part of script in 5 seconds")
                sleep(5)
                exit

            elif wipe_answer in ['N', 'n']:
                print("User answered no, going to main part of script in 5 seconds")
                sleep(5)
                exit
    except IndexError:
        exit
    
    def printborder():
        print("-----------------------------------------------------------------------------")

    banner = """\
     _    ____  _ _   __  __ _         _
    / \  | __ )(_) |_|  \/  (_)___ ___(_)_ __   __ _
   / _ \ |  _ \| | __| |\/| | / __/ __| | '_ \ / _` |
  / ___ \| |_) | | |_| |  | | \__ \__ \ | | | | (_| |
 /_/   \_\____/|_|\__|_|  |_|_|___/___/_|_| |_|\__, |
                                               |___/
 """

    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    currentDT = datetime.datetime.now()

    try:
        print(colored("Date of latest hash generation :", 'green'), timestamp_stored)
        print(" ")
    except NameError:
        exit

    writeswitch = input("Write hash files in current directory? This will update the hashes if already stored (Y/N): ")
    randcounter = -1
    randreplacecounter = -1
    notified_randgen = 0
    if writeswitch in ['Y', 'y']:
        randgenswitch = input("Make random file(s)? (Y/N): ")

    elif writeswitch in ['N', 'n']:
        randgenswitch = 'N'

    elif writeswitch not in ['Y', 'N', 'y', 'n']:
        print("Invalid input, exiting...")
        os._exit(1)

def GenRand1():
    print("Starting thread 1")
    rand_data = ''.join(random.choice(string.ascii_letters + string.digits + string.hexdigits) for _ in range(randfilesize * 1000))
    randstring = rand_data

    output = open('randomfile0', "wb")
    print("Thread 1 done, dumping to file")
    pickle.dump(randstring, output)
    output.close()


def GenRand2():
    print("Starting thread 2")
    rand_data = ''.join(random.choice(string.ascii_letters + string.digits + string.hexdigits) for _ in range(randfilesize * 1000))
    randstring = rand_data

    output = open('randomfile1', "wb")
    print("Thread 2 done, dumping to file")
    pickle.dump(randstring, output)
    output.close()


def GenRand3():
    print("Starting thread 3")
    rand_data = ''.join(random.choice(string.ascii_letters + string.digits + string.hexdigits) for _ in range(randfilesize * 1000))
    randstring = rand_data

    output = open('randomfile2', "wb")
    print("Thread 3 done, dumping to file")
    pickle.dump(randstring, output)
    output.close()


def GenRand4():
    print("Starting thread 4")
    rand_data = ''.join(random.choice(string.ascii_letters + string.digits + string.hexdigits) for _ in range(randfilesize * 1000))
    randstring = rand_data

    output = open('randomfile3', "wb")
    print("Thread 4 done, dumping to file")
    pickle.dump(randstring, output)
    output.close()

def GenRand5():
    print("Starting thread 5")
    rand_data = ''.join(random.choice(string.ascii_letters + string.digits + string.hexdigits) for _ in range(randfilesize * 1000))
    randstring = rand_data

    output = open('randomfile4', "wb")
    print("Thread 5 done, dumping to file")
    pickle.dump(randstring, output)
    output.close()

if randgenswitch in ['Y', 'y']:
    print(colored("-- Randomized files will be dropped in the current directory of this script --", 'yellow'))
    random.seed(input("Enter random seed for file generation: "))
    randfilesize = int(input("Enter size of each random file (in kilobytes): "))
    
    filedir1, filedir2, filedir3, filedir4, filedir5 = "","","","",""
    ram_hash1, ram_hash2, ram_hash3, ram_hash4, ram_hash5 = "","","","",""

    p1r1, p2r2, p3r3, p4r4, p5r5 = Process(target=GenRand1), Process(target=GenRand2), Process(target=GenRand3), Process(target=GenRand4), Process(target=GenRand5)
    # the 'r' in p1r1 etc stands for random, because these are the processes where we generate the ranom text
    p1r1.start() 
    p2r2.start()
    p3r3.start()
    p4r4.start()
    p5r5.start()

    p1r1.join()
    p2r2.join()
    p3r3.join()
    p4r4.join()
    p5r5.join()

    # -- Below is old, single core method --
    #
    # rand_data = ''.join(random.choice(string.ascii_letters + string.digits + string.hexdigits) for _ in range(randfilesize * 1000))
    # randstring_array.append(rand_data)
    # randcounter = randcounter + 1
    # output = open('randomfile'+str(randcounter), "wb")
    exit

elif randgenswitch not in ['Y', 'N', 'y', 'n']:
    print("Invalid input, exiting...")
    os._exit(1)

elif randgenswitch in ['N', 'n']:
    exit

def GenHash1():
    try:
        filedir1 = 'randomfile0'
        ram_hash1 = hashlib.sha256(open(filedir1, 'rb').read()).hexdigest()
        print("Hash for ", filedir1, ":", ram_hash1)

        if ram_hash1 == hashes[1]:
            print(colored('Hashes matched on :', 'green'), filedir1)
        elif ram_hash1 != hashes[1]:
            print(colored("Hash mismatch on :", 'red'), filedir1)
            print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))
        printborder()
    except FileNotFoundError as error:
        print("File", filedir1, "not found")
        print(colored("Exiting due to error...", 'red'))
        printborder()
        os._exit(1)

def GenHash2():
    try:
        filedir2 = 'randomfile1'
        ram_hash2 = hashlib.sha256(open(filedir2, 'rb').read()).hexdigest()
        print("Hash for ", filedir2, ":", ram_hash2)

        if ram_hash2 == hashes[2]:
            print(colored('Hashes matched on :', 'green'), filedir2)
        elif ram_hash2 != hashes[2]:
            print(colored("Hash mismatch on :", 'red'), filedir2)
            print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))
        
        printborder()
    except FileNotFoundError as error:
        print("File", filedir2, "not found")
        print(colored("Exiting due to error...", 'red'))
        printborder()
        os._exit(1)

def GenHash3():
    try:
        filedir3 = 'randomfile2'
        ram_hash3 = hashlib.sha256(open(filedir3, 'rb').read()).hexdigest()
        print("Hash for ", filedir3, ":", ram_hash3)

        if ram_hash3 == hashes[3]:
            print(colored('Hashes matched on :', 'green'), filedir3)
        elif ram_hash3 != hashes[3]:
            print(colored("Hash mismatch on :", 'red'), filedir3)
            print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))

        printborder()
    except FileNotFoundError as error:
        print("File", filedir3, "not found")
        print(colored("Exiting due to error...", 'red'))
        printborder()
        os._exit(1)

def GenHash4():
    try:
        filedir4 = 'randomfile3'
        ram_hash4 = hashlib.sha256(open(filedir4, 'rb').read()).hexdigest()
        print("Hash for ", filedir4, ":", ram_hash4)

        if ram_hash4 == hashes[4]:
            print(colored('Hashes matched on :', 'green'), filedir4)
        elif ram_hash4 != hashes[4]:
            print(colored("Hash mismatch on :", 'red'), filedir4)
            print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))
        
        printborder()
    except FileNotFoundError as error:
        print("File", filedir4, "not found")
        print(colored("Exiting due to error...", 'red'))
        printborder()
        os._exit(1)

def GenHash5():
    try:
        filedir5 = 'randomfile4'
        ram_hash5 = hashlib.sha256(open(filedir5, 'rb').read()).hexdigest()
        print("Hash for ", filedir5, ":", ram_hash5)

        if ram_hash5 == hashes[5]:
            print(colored('Hashes matched on :', 'green'), filedir5)
        elif ram_hash5 != hashes[5]:
            print(colored("Hash mismatch on :", 'red'), filedir5)
            print(colored("File has either changed naturally from user, or storage device has corrupted file", 'red'))

        printborder()
    except FileNotFoundError as error:
        print("File", filedir5, "not found")
        print(colored("Exiting due to error...", 'red'))
        printborder()
        os._exit(1)

# Writing values
if writeswitch in ['Y', 'y']:
    print(colored('Dumping hash values from ram to storage (hashes.pkl and timestamp.pkl)...', 'cyan'))
    hashes = {
        1: ram_hash1,
        2: ram_hash2,
        3: ram_hash3,
        4: ram_hash4,
        5: ram_hash5
    }
    timestamp_stored = currentDT.strftime("%Y-%m-%d %H:%M:%S")
    output = open('hashes.pkl', "wb")
    pickle.dump(hashes, output)
    output.close()

    output = open('timestamp.pkl', "wb")
    pickle.dump(timestamp_stored, output)
    output.close()

elif writeswitch in ['N', 'n']:
    print(colored('User doesn\'t want to write to file, skipping', 'grey'))
    exit
# End of writing values

# Reading values
pkl_file = open("hashes.pkl", "rb")
hashes = pickle.load(pkl_file)
pkl_file.close()

p1h1, p2h2, p3h3, p4h4, p5h5 = Process(target=GenHash1), Process(target=GenHash2), Process(target=GenHash3), Process(target=GenHash4), Process(target=GenHash5)
# the 'h' in p1h1 etc stands for hash (in this case obviously we are generating the hashes)
printborder()
p1h1.start()
p2h2.start()
p3h3.start()
p4h4.start()
p5h5.start()

p1h1.join()
p2h2.join()
p3h3.join()
p4h4.join()
p5h5.join()
# End of reading values
