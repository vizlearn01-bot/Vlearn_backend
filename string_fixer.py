import tokenize
from io import BytesIO
import re

def fix_bullets(s_val):
    if '•' not in s_val:
        return s_val
    parts = s_val.split('•')
    out = []
    if parts[0].strip():
        out.append(parts[0].strip())
    for part in parts[1:]:
        part = part.strip()
        if not part: continue
        colon_idx = part.find(':')
        if colon_idx != -1 and colon_idx < 40:
            key = part[:colon_idx].strip()
            if not key.startswith('**'):
                key = f"**{key}**"
            val = part[colon_idx+1:].strip()
            out.append(f"- {key}: {val}")
        else:
            out.append(f"- {part}")
    res = "\\n".join(out).replace('\\n\\n', '\\n')
    return res

def process_file(filepath):
    with open(filepath, 'rb') as f:
        tokens = list(tokenize.tokenize(f.readline))
    
    out = []
    last_pos = (1, 0)
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for tok in tokens:
        if tok.type == tokenize.STRING:
            # We only modify strings that contain the bullet point
            if '•' in tok.string:
                # The token string includes quotes
                quote = tok.string[0]
                if tok.string.startswith('"""') or tok.string.startswith("'''"):
                    quote = tok.string[:3]
                
                inner = tok.string[len(quote):-len(quote)]
                # apply fix
                fixed_inner = fix_bullets(inner)
                new_str = quote + fixed_inner + quote
                # We need to replace it in the text.
                # Actually, tokenize module gives exact positions. But let's just use string replace for safety.
                pass

if __name__ == '__main__':
    pass
