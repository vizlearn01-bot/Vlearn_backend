file_path = "curriculum/ingest_cbc_grade10_home_science_topic3_3.py"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_block = False
for line in lines:
    if '"definition": {' in line or '"practical": {' in line:
        in_block = True
    if in_block and line.strip() == '),' and len(new_lines) > 0 and (']' in new_lines[-1] or '}' in new_lines[-1]):
        new_lines.append('        },\n')
        in_block = False
    else:
        if in_block and ('"youtube_id"' in line or '"deep_explanation"' in line or '"mcq"' in line):
            in_block = False
        new_lines.append(line)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Replacement complete.")
