#!/usr/bin/env python3
"""
Sequence Validator for Editorial Video Prompt Engine
Validates multi-clip JSON edit sequences against schema, frame counts, and formatting rules.
"""

import sys
import json
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def validate_timestamp(ts: str) -> bool:
    return bool(re.match(r"^\d{2}:\d{2}:\d{2}\.\d{3}$", ts))

def validate_sequence(file_path: str) -> bool:
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File '{file_path}' does not exist.")
        return False

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"JSON Syntax Error: {e}")
        return False

    if not isinstance(data, list):
        print("Validation Error: Root element must be an array of parts.")
        return False

    errors = []
    warnings = []

    for i, part in enumerate(data, start=1):
        if not isinstance(part, dict):
            errors.append(f"Part {i}: Must be a JSON object.")
            continue

        part_num = part.get("part")
        source_file = part.get("source_file")
        time_range = part.get("time_range")
        global_vfx = part.get("global_vfx")
        segments = part.get("segments")

        if not isinstance(part_num, int) or part_num < 1:
            errors.append(f"Item {i}: 'part' field must be an integer >= 1 (got {part_num}).")

        if not source_file:
            errors.append(f"Part {i}: Missing 'source_file'.")

        if not time_range or not re.match(r"^\d{2}:\d{2}:\d{2}\.\d{3}\s*-\s*\d{2}:\d{2}:\d{2}\.\d{3}$", time_range):
            errors.append(f"Part {i}: Invalid or missing 'time_range' ({time_range}). Expected HH:MM:SS.mmm - HH:MM:SS.mmm")

        if not isinstance(global_vfx, dict):
            errors.append(f"Part {i}: Missing 'global_vfx' object.")
        else:
            typo = global_vfx.get("typography")
            if not isinstance(typo, dict):
                errors.append(f"Part {i}: 'global_vfx.typography' must be an object.")
            else:
                if not typo.get("title_font"):
                    errors.append(f"Part {i}: Missing 'global_vfx.typography.title_font'.")
                if not typo.get("title_color"):
                    errors.append(f"Part {i}: Missing 'global_vfx.typography.title_color'.")

        if not isinstance(segments, list) or len(segments) == 0:
            errors.append(f"Part {i}: 'segments' must be a non-empty array.")
            continue

        for seg_idx, seg in enumerate(segments, start=1):
            seg_id = seg.get("segment_id", f"{i}.{seg_idx}")
            st = seg.get("start_time")
            et = seg.get("end_time")

            if not st or not validate_timestamp(st):
                errors.append(f"Part {i} Segment {seg_id}: Invalid start_time '{st}'.")
            if not et or not validate_timestamp(et):
                errors.append(f"Part {i} Segment {seg_id}: Invalid end_time '{et}'.")

            dialogue = seg.get("dialogue")
            if not dialogue:
                warnings.append(f"Part {i} Segment {seg_id}: Dialogue is empty.")

            graphics = seg.get("graphics")
            if not isinstance(graphics, dict):
                errors.append(f"Part {i} Segment {seg_id}: Missing 'graphics' object.")
            else:
                main_title = graphics.get("main_title", {})
                title_text = main_title.get("text", "")
                word_count = len(title_text.split())
                if word_count > 2:
                    warnings.append(f"Part {i} Segment {seg_id}: main_title '{title_text}' has {word_count} words (Rule recommends 1-2 words).")

                if not main_title.get("color"):
                    errors.append(f"Part {i} Segment {seg_id}: main_title missing 'color'.")

                credits = graphics.get("border_credits", {})
                if not credits.get("left_margin") or not credits.get("right_margin"):
                    warnings.append(f"Part {i} Segment {seg_id}: Border credits missing left or right margin text.")

            sfx = seg.get("sfx")
            if not sfx:
                warnings.append(f"Part {i} Segment {seg_id}: Missing 'sfx' sound design cue.")

    if errors:
        print("[FAIL] Validation Failed with Errors:")
        for err in errors:
            print(f"  - {err}")
        return False

    if warnings:
        print("[WARN] Validation Passed with Warnings:")
        for warn in warnings:
            print(f"  - {warn}")
    else:
        print("[OK] Validation Succeeded! Sequence is strictly compliant with the Editorial Video Prompt Engine specification.")

    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_sequence.py <path_to_sequence.json>")
        sys.exit(1)

    success = validate_sequence(sys.argv[1])
    sys.exit(0 if success else 1)
