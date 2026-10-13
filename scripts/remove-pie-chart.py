# 3D 잔디 SVG에서 언어 원형 차트 그룹을 제거한다
import pathlib, re, sys

PIE_GROUP = '<g transform="translate(40, 520)">'

for path in pathlib.Path(sys.argv[1]).glob('*.svg'):
    svg = path.read_text()
    start = svg.find(PIE_GROUP)
    if start < 0:
        continue
    depth, pos = 0, start
    for m in re.finditer(r'<g[\s>]|</g>', svg[start:]):
        depth += -1 if m.group() == '</g>' else 1
        if depth == 0:
            pos = start + m.end()
            break
    path.write_text(svg[:start] + svg[pos:])
    print(f'removed pie chart: {path.name}')
