# built-in
from hashlib import md5
from pathlib import Path


def make_baseline(path: str, context: str, code: str, line: int) -> str:
    path = Path(path).absolute().relative_to(Path.cwd()).as_posix().lstrip('./')
    context = (context or str(line)).strip().replace("\n", "\\n")
    digest = md5()
    digest.update(code.encode())
    return f"{path}\t{context}\t{digest.hexdigest()}"
