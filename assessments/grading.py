def grade_from_score(score: float, max_score: float = 100) -> str:
    if max_score <= 0: return 'E'
    pct = (score / max_score) * 100
    if pct >= 80: return 'A'
    if pct >= 75: return 'A-'
    if pct >= 70: return 'B+'
    if pct >= 65: return 'B'
    if pct >= 60: return 'B-'
    if pct >= 55: return 'C+'
    if pct >= 50: return 'C'
    if pct >= 45: return 'C-'
    if pct >= 40: return 'D+'
    if pct >= 35: return 'D'
    if pct >= 30: return 'D-'
    return 'E'

def points_from_grade(grade: str) -> int:
    scale = {'A':12,'A-':11,'B+':10,'B':9,'B-':8,'C+':7,'C':6,'C-':5,'D+':4,'D':3,'D-':2,'E':1}
    return scale.get(grade, 0)
