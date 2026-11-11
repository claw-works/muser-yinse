"""Check every instrument's meta.json and write index.json. 检查每件乐器的 meta.json，生成 index.json。

    uv run python scripts/index.py
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FAMILIES = {"strike", "pluck"}
# 允许再分发与衍生作品的录音许可证（SPDX）。
LICENSES = {"CC0-1.0", "CC-BY-3.0", "CC-BY-4.0", "CC-BY-SA-3.0", "CC-BY-SA-4.0", "MIT", "Apache-2.0", "PDDL-1.0", "public-domain"}


def main() -> int:
    errors, entries = [], []
    for family_dir in sorted((ROOT / "instruments").iterdir()):
        if not family_dir.is_dir():
            continue
        for d in sorted(p for p in family_dir.iterdir() if p.is_dir()):
            where = d.relative_to(ROOT)
            table, meta_file = d / f"{d.name}.yinse.json", d / "meta.json"
            if family_dir.name not in FAMILIES:
                errors.append(f"{where}: family must be one of {sorted(FAMILIES)}")
            if not table.is_file():
                errors.append(f"{where}: missing {table.name}")
                continue
            if not meta_file.is_file():
                errors.append(f"{where}: missing meta.json")
                continue
            meta = json.loads(meta_file.read_text())
            t = json.loads(table.read_text())
            if t.get("format") != "muser-yinse-modal":
                errors.append(f"{where}: {table.name} is not a muser yinse instrument")
            lic = meta.get("source", {}).get("license")
            if lic not in LICENSES:
                errors.append(f"{where}: source.license '{lic}' is not one that allows redistribution ({sorted(LICENSES)})")
            for key in ("name", "family", "source"):
                if key not in meta:
                    errors.append(f"{where}: meta.json lacks '{key}'")
            if meta.get("name") != d.name or meta.get("family") != family_dir.name:
                errors.append(f"{where}: meta.json name/family must match the folder ({family_dir.name}/{d.name})")
            articulations = sorted({n.get("articulation", "") for n in t.get("notes", [])} - {""} | set(t.get("gestures", {})))
            pitches = [n["pitch"] for n in t.get("notes", [])]
            entries.append({
                "spec": f"yinse:{family_dir.name}/{d.name}",
                "name": meta.get("name"),
                "zh": meta.get("zh"),
                "description": meta.get("description"),
                "license": lic,
                "range": [round(min(pitches)), round(max(pitches))] if pitches else None,
                "articulations": articulations,
                "kb": round(table.stat().st_size / 1024),
            })
    for e in errors:
        print("error:", e, file=sys.stderr)
    (ROOT / "index.json").write_text(json.dumps({"instruments": entries}, ensure_ascii=False, indent=2) + "\n")
    print(f"{len(entries)} instruments, {len(errors)} errors -> index.json")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
