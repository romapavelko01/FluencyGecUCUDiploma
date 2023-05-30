from unlp_2023_shared_task.scripts.evaluate import tokenize_file
from pathlib import Path


tokenize_file(Path('sv_uk_backtranslated_train_source.txt'), Path('btr.source.tok'))
print("tokenized")