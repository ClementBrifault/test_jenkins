import time
from tqdm import tqdm

for i in tqdm(range(5*60)):
    time.sleep(1)

print('2nd run')
