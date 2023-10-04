import sys
from colorama import Fore, Style

malloc_funcs = [
	"alloc",
	"strjoin",
	"substr",
	"strdup",
	"lstnew",
]

show_all = True
ng_count = 0

def using_malloc_func(line):
	for func in malloc_funcs:
		if func in line:
			return True
	return False

def read_flie(filename):
	lines = []
	lines.append(filename)
	for line in open(filename, 'r'):
		line = line.strip(' \t\r')
		lines.append(line)
	return lines

def checker(lines):
	global ng_count
	malloced_value = None
	for i, line in enumerate(lines[1:]):
		if line[0] == '#' or line[0] == '\n' or (len(line) > 2 and (line[0] == '/' and line[1] == '*') or (line[0] == '/' and line[1] == '/')):
			continue
		if malloced_value != None:
			if (not ("!" + malloced_value in line or "== NULL" in line)):
				print(f' {lines[0]}: {Fore.RED}{Style.BRIGHT}NG{Fore.RESET}{Style.RESET_ALL} at line {i + 1}: value {Style.BRIGHT}{malloced_value}{Style.RESET_ALL} is not NULL checked')
				ng_count += 1
			elif show_all:
				print(f' {lines[0]}: {Fore.GREEN}{Style.BRIGHT}OK{Fore.RESET}{Style.RESET_ALL} at line {i + 1}: value {Style.BRIGHT}{malloced_value}{Style.RESET_ALL} is NULL checked')
			malloced_value = None
		if (using_malloc_func(line)):
			malloced_value = line.split(' ')[0]

args = sys.argv
if len(args) < 2:
	print('Usage: python3 NULLCheckChecker.py [file1] [file2] ...')
	exit(0)
for arg in args[1:]:
	if ("-h" in arg or "--help" in arg):
		print("This script checks if malloced value is NULL checked or not.")
		print("Usage: python3 NULLCheckChecker.py [file1] [file2] ...")
		print("Options:")
		print("  -h, --help: show this help message and exit")
		print("  -n: do not show OK messages")
		print("if you want to add more malloc functions, please edit malloc_funcs in this script."
		)
		exit(0)
	if ("-n" in arg):
		show_all = False
		continue
	lines = read_flie(arg)
	checker(lines)
if not ng_count:
	print(f'{Fore.GREEN}{Style.BRIGHT}[ ALL OK ]{Fore.RESET}{Style.RESET_ALL}')
else:
	print(f'{Fore.RED}{Style.BRIGHT}[ {ng_count} NG detected ]{Fore.RESET}{Style.RESET_ALL}')