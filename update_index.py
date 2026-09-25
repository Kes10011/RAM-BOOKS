path = r'C:\Users\Sessi\Desktop\ANTIGRAVITY\RAMSURESH\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old welcome overlay styles (from #welcome-grid to before #stage)
old_styles_start = '    #welcome-grid {'
old_styles_end = '    #stage{position:absolute;inset:0;cursor:pointer}'

start_idx = content.find(old_styles_start)
end_idx = content.find(old_styles_end)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done. New length:', len(content))
