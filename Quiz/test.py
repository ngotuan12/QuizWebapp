'''
Created on Feb 6, 2024

@author: Ngo Anh Tuan
'''
from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_DIRS = [
    Path(BASE_DIR).joinpath(BASE_DIR,'Quiz','static'),
    os.path.join(BASE_DIR, 'Quiz','static'),
    BASE_DIR / "Quiz" /"static",
]
print(STATICFILES_DIRS)