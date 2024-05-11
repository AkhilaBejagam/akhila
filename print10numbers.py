import argparse
c = argparse.ArgumentParser(description='process some integers')

c.add_argument('current_number', type=int)
c.add_argument('previous_number', type=int)
args = c.parse_args()
current_num = args.current_number
previous_num = args.previous_number

for i in range(10):
    sum = previous_num + i
    print(f'Current number {i} Previous Number {previous_num} is {sum}')
    previous_num = i