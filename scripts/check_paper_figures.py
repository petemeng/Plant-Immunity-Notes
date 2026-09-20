"""Check provenance and integrity of the new methods chapter paper figures."""
from pathlib import Path
from urllib.parse import urlparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs/assets/images/papers"


def main():
    records = json.loads((ASSETS / "methods-sources.json").read_text(encoding="utf-8"))["figures"]
    required = ("file", "article_title", "authors", "year", "doi", "article_url",
                "figure", "source_url", "license", "license_url", "license_evidence_url",
                "sha256", "chapter", "modifications")
    seen = set()
    for record in records:
        assert all(record.get(key) for key in required), f"Incomplete record: {record}"
        file = ASSETS / record["file"]
        assert file.resolve().parent == ASSETS.resolve(), f"Invalid asset path: {file}"
        assert file.name not in seen, f"Duplicate file: {file.name}"
        seen.add(file.name)
        assert file.is_file(), f"Missing image: {file}"
        assert hashlib.sha256(file.read_bytes()).hexdigest() == record["sha256"], f"Image changed: {file}"
        for field in ("article_url", "source_url", "license_url", "license_evidence_url"):
            assert urlparse(record[field]).scheme == "https", f"Invalid {field}: {record[field]}"
        chapter = ROOT / "docs" / record["chapter"]
        source = chapter.read_text(encoding="utf-8")
        assert f"../assets/images/papers/{file.name}" in source, f"Unused figure: {file.name}"
        assert record["doi"] in source, f"Missing article DOI in {chapter.name}"
    used = set()
    for chapter in (ROOT / "docs/part7-研究技术与实验逻辑").glob("ch*.md"):
        used.update(re.findall(r"!\[[^\]]*\]\(\.\./assets/images/papers/([^\)]+)\)", chapter.read_text(encoding="utf-8")))
    assert seen == used, f"Manifest and chapter images differ: {seen ^ used}"
    print(f"Verified {len(records)} paper figures: complete provenance, unchanged bytes, chapter references.")


if __name__ == "__main__":
    main()
