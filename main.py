import time
from tqdm import tqdm

for i in tqdm(range(100)):
    time.sleep(6)

print('Work done')