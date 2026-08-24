import re

with open("organizations/models.py", "r") as f:
    content = f.read()

# Only keep setup_wizard_step in School
lines = content.split('\n')
new_lines = []
in_school = False
for line in lines:
    if line.startswith('class School(models.Model):'):
        in_school = True
    elif line.startswith('class '):
        in_school = False
        
    if 'setup_wizard_step =' in line:
        if not in_school:
            continue
    new_lines.append(line)

content = '\n'.join(new_lines)

with open("organizations/models.py", "w") as f:
    f.write(content)

print("Fixed models.py")
