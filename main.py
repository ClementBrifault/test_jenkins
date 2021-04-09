import time
from tqdm import tqdm

for i in tqdm(range(25*60)):
    time.sleep(1)

with open('file.txt', 'w') as f:
    f.write('TESTFILE attente3')

print('Work done')
