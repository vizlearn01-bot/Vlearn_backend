import re
import json
from curriculum.models import LessonBlock

def clean_str(s):
    if not isinstance(s, str) or not s.strip():
        return s, False
    orig = s
    
    # 1. Double parentheses math: (( \Delta ... )) -> ($...$)
    s = re.sub(r'\(\((\s*\\[a-zA-Z]+[^\(\)]*?)\)\)', r'($\1$)', s)
    s = re.sub(r'\(\((\s*\^[0-9]+_[0-9]+[^\(\)]*?)\)\)', r'($\1$)', s)
    
    # 2. Corrupted 'eq \text' -> '\neq \text'
    s = re.sub(r'(?<![a-zA-Z0-9\\])eq\s+(\\text\{)', r'\\neq \1', s)
    s = re.sub(r'(?<![a-zA-Z0-9\\])eq\s+(\\[a-zA-Z]+)', r'\\neq \1', s)
    
    # 3. If string is an option starting with "A) ", "B) ", etc.
    m_opt = re.match(r'^([A-D][\)\.]\s*)(.*)$', s)
    if m_opt:
        prefix, body = m_opt.groups()
        body_clean = body.strip()
        if ('\\text{' in body_clean or '\\rightarrow' in body_clean or '\\beta' in body_clean or 
            '\\alpha' in body_clean or '\\gamma' in body_clean or '\\frac{' in body_clean or 
            re.search(r'\^[0-9]+_[0-9]+', body_clean)) and not body_clean.startswith('$'):
            s = f"{prefix}${body_clean}$"
    else:
        # Check if the entire string is a formula without $
        if not ('$' in s) and ('\n' not in s) and not s.startswith('#'):
            if ('\\text{' in s or '\\rightarrow' in s or '\\beta' in s or 
                '\\alpha' in s or '\\gamma' in s or '\\frac{' in s or 
                re.search(r'\^[0-9]+_[0-9]+', s)):
                s = f"${s.strip()}$"

    # 4. In-line chemical equations after bullet points
    # e.g. "*Reduction Half-Equation*: \text{Cl}_{2(g)} + 2e^- \rightarrow 2\text{Cl}^-_{(aq)}"
    def wrap_chemical_line(match):
        prefix = match.group(1)
        eq = match.group(2).strip()
        if not eq.startswith('$') and not eq.endswith('$'):
            return f"{prefix}${eq}$"
        return match.group(0)

    s = re.sub(r'(\*\s*:\s*)(\\text\{[^\n]+)', wrap_chemical_line, s)
    
    # 5. Fix unbalanced '$' if caused by (=mc^2^{1}_{0}\text{n}$)
    if '(=mc^2^{1}_{0}\\text{n}$)' in s:
        s = s.replace('(=mc^2^{1}_{0}\\text{n}$)', '($= mc^2 = ^{1}_{0}\\text{n}$)')
        
    return s, s != orig

def recursively_clean(content, block_type):
    changed = False
    if isinstance(content, str):
        return clean_str(content)
    elif isinstance(content, dict):
        new_dict = {}
        for k, v in content.items():
            if k == 'formula' and isinstance(v, str) and not ('$' in v):
                new_dict[k] = f"$${v.strip()}$$"
                changed = True
            elif isinstance(v, (dict, list, str)):
                new_v, ch = recursively_clean(v, block_type)
                new_dict[k] = new_v
                if ch: changed = True
            else:
                new_dict[k] = v
        return new_dict, changed
    elif isinstance(content, list):
        new_list = []
        for item in content:
            new_item, ch = recursively_clean(item, block_type)
            new_list.append(new_item)
            if ch: changed = True
        return new_list, changed
    return content, False

def run_sanitization():
    blocks = LessonBlock.objects.all()
    print(f"Total blocks in database: {blocks.count()}")
    
    sanitized_count = 0
    for b in blocks:
        new_content, ch1 = recursively_clean(b.content, b.block_type)
        new_title, ch2 = clean_str(b.title or '')
        
        if ch1 or ch2:
            sanitized_count += 1
            if ch1:
                b.content = new_content
            if ch2:
                b.title = new_title
            b.save()
            
    print(f"Successfully sanitized {sanitized_count} blocks in the database!")

if __name__ == "__main__":
    run_sanitization()
