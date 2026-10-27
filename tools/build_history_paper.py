"""Render the authored methods preprint to PDF and accessible HTML; no network."""
from pathlib import Path
from html import escape
import re
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Preformatted
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/papers/when-history-changes-the-agent'
source=(OUT/'when-history-changes-the-agent.md').read_text(encoding='utf-8')
fonts=Path('C:/Windows/Fonts')
for name,file in [('HistoryBody','georgia.ttf'),('HistoryBold','georgiab.ttf'),('HistoryItalic','georgiai.ttf'),('HistoryUI','calibri.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
pdfmetrics.registerFontFamily('HistoryBody',normal='HistoryBody',bold='HistoryBold',italic='HistoryItalic',boldItalic='HistoryBold')
ink=colors.HexColor('#263e35')
styles={
 'body':ParagraphStyle('body',fontName='HistoryBody',fontSize=10.1,leading=15.3,spaceAfter=9,textColor=ink),
 'h3':ParagraphStyle('h3',fontName='HistoryBold',fontSize=14,leading=19,spaceBefore=17,spaceAfter=9,keepWithNext=True,textColor=ink),
 'h4':ParagraphStyle('h4',fontName='HistoryBold',fontSize=11.5,leading=16,spaceBefore=10,spaceAfter=7,keepWithNext=True,textColor=ink),
 'title':ParagraphStyle('title',fontName='HistoryBody',fontSize=31,leading=36,spaceAfter=14,textColor=ink),
 'sub':ParagraphStyle('sub',fontName='HistoryBody',fontSize=17,leading=23,spaceAfter=15,textColor=ink),
 'small':ParagraphStyle('small',fontName='HistoryUI',fontSize=8.5,leading=12,spaceAfter=9,textColor=colors.HexColor('#52685b')),
 'code':ParagraphStyle('code',fontName='Courier',fontSize=8.3,leading=12,spaceBefore=6,spaceAfter=12,textColor=ink),
 'ref':ParagraphStyle('ref',fontName='HistoryUI',fontSize=8.5,leading=12,spaceAfter=10,textColor=ink)
}
def inline(text):
    text=escape(text)
    return re.sub(r'(https://[^\s<]+)',r'<a href="\1" color="#31575f">\1</a>',text)

story=[];html=[];refs=False
for block in re.split(r'\n\s*\n',source.strip()):
    if block.startswith('    '):
        code='\n'.join(line[4:] if line.startswith('    ') else line for line in block.splitlines())
        story.append(Preformatted(code,styles['code']))
        html.append('<pre>'+escape(code)+'</pre>')
    elif block.startswith('# '):
        story.append(Paragraph(inline(block[2:]),styles['title']));html.append('<h1>'+inline(block[2:])+'</h1>')
    elif block.startswith('## '):
        story.append(Paragraph(inline(block[3:]),styles['sub']));html.append('<p class="subtitle">'+inline(block[3:])+'</p>')
    elif block.startswith('### '):
        title=block[4:];refs=title=='References'
        story.append(Paragraph(inline(title),styles['h3']));html.append('<h2>'+inline(title)+'</h2>')
    elif block.startswith('#### '):
        story.append(Paragraph(inline(block[5:]),styles['h4']));html.append('<h3>'+inline(block[5:])+'</h3>')
    else:
        text=' '.join(block.splitlines())
        style=styles['ref'] if refs else styles['small'] if text.startswith(('Neurasoft research','Methods preprint','Commissioned by')) else styles['body']
        story.append(Paragraph(inline(text),style));html.append('<p>'+inline(text)+'</p>')

def footer(canvas,doc):
    canvas.saveState();w,h=A4
    canvas.setStrokeColor(colors.HexColor('#b3c2b7'));canvas.line(52,43,w-52,43)
    canvas.setFillColor(colors.HexColor('#52685b'));canvas.setFont('HistoryUI',8)
    canvas.drawString(52,29,'Neurasoft research | Methods preprint v1.0 | 27 October 2026')
    canvas.drawRightString(w-52,29,str(doc.page));canvas.restoreState()

pdf=OUT/'when-history-changes-the-agent.pdf'
SimpleDocTemplate(str(pdf),pagesize=A4,leftMargin=52,rightMargin=52,topMargin=48,bottomMargin=60,title='When History Changes the Agent',author='Neurasoft research / Eternities Inc.',subject='A causal protocol for developmental continuity, appraisal, and prospective self-knowledge').build(story,onFirstPage=footer,onLaterPages=footer)
head='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>When History Changes the Agent | Neurasoft</title><meta name="description" content="A prospective methods preprint on developmental continuity, appraisal and useful self-knowledge in persistent artificial agents."><link rel="canonical" href="https://neurasoft.us/assets/papers/when-history-changes-the-agent/"><link rel="stylesheet" href="paper.css"></head><body><main><nav><a href="/">Neurasoft</a> / <a href="/articles/the-shape-of-someone/">Read the essay</a></nav>'''
links='''<p class="downloads"><a href="when-history-changes-the-agent.pdf">Download PDF</a> <a href="when-history-changes-the-agent.md">Manuscript</a> <a href="research-bundle.zip">Research bundle</a> <a href="analytic-checks.json">Analytical checks</a></p>'''
(OUT/'index.html').write_text(head+links+''.join(html)+'<footer>Prospective protocol; no new subject results. <a href="DEPOSIT.md">Zenodo preparation notes</a>.</footer></main></body></html>',encoding='utf-8')
print('Rendered manuscript to PDF and HTML: '+str(len(source.split()))+' words.')
