import time
from tqdm import tqdm

for i in tqdm(range(20*60)):
    time.sleep(1)

with open('file.txt', 'w') as f:
    f.write('TESTFILE ver3')

print('Work done')
