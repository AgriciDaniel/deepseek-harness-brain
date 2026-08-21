from __future__ import annotations

import hashlib
import os
from datetime import date, datetime, timezone
from pathlib import Path


def parse_as_of(value: str | None) -> date:
    """Return an explicit date, SOURCE_DATE_EPOCH in UTC, or today's date."""
    if value is None or not value.strip():
        epoch = os.environ.get("SOURCE_DATE_EPOCH", "").strip()
        if epoch:
            try:
                return datetime.fromtimestamp(int(epoch), tz=timezone.utc).date()
            except (OverflowError, OSError, ValueError) as exc:
                raise ValueError(f"invalid SOURCE_DATE_EPOCH: {epoch!r}") from exc
        return date.today()
    try:
        return date.fromisoformat(value.strip())
    except ValueError as exc:
        raise ValueError(f"invalid --as-of date: {value!r}") from exc


def tree_sha256(root: Path) -> str:
    """Hash a directory from sorted relative paths and file-content hashes."""
    root = root.resolve()
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        if path.is_symlink():
            raise ValueError(f"sample tree contains a symlink: {path.relative_to(root).as_posix()}")
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        file_digest = hashlib.sha256(path.read_bytes()).hexdigest()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_digest.encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def read_tree_fixture(path: Path) -> str:
    """Read the first SHA-256 token from a deterministic-tree fixture."""
    value = path.read_text(encoding="utf-8").strip().split(maxsplit=1)[0]
    if len(value) != 64 or any(char not in "0123456789abcdef" for char in value):
        raise ValueError(f"invalid tree hash fixture: {path}")
    return value
