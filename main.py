import time
from tqdm import tqdm

for i in tqdm(range(5*60)):
    time.sleep(1)

with open('file.txt', 'w') as f:
    f.write('TESTFILE')

print('Work done')