#!/usr/local/bin/python3
import random
import subprocess
import math
from colorama import Fore, Style

test_times = 100
num_size = 6
args = []

for i in range(test_times):
	numlist = random.sample(range(num_size), num_size)
	list_str = ' '.join([str(v) for v in numlist])
	print(f'testing {i + 1} / {test_times} \t{list_str}', end='')
	result = subprocess.run([f'./push_swap {list_str}'], capture_output=True, shell=True, text=True)
	c_result = subprocess.run([f'./checker {list_str}'], capture_output=True, shell=True, text=True, input=result.stdout).stdout
	if not (c_result == 'OK\n' or c_result == ''):
		print("")
		print(Fore.RED + Style.BRIGHT + '[ KO return exist ]' + Style.RESET_ALL + Fore.RESET)
		print(f'input: {list_str}')
		exit()
	else:
		print('\t' + Fore.GREEN + Style.BRIGHT + '[ OK ]' + Style.RESET_ALL + Fore.RESET)
	args.append(int(result.stdout.count('\n')))
print(Fore.GREEN + Style.BRIGHT + '[ ALL OK ]' + Fore.RESET + Style.RESET_ALL)
print(f'max: {max(args)}')
print(f'min: {min(args)}')
print(f'avr: {math.floor(sum(args) / len(args))}')