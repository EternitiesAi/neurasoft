"""Render the authored Three Crowns manuscript; no network or research execution."""
from pathlib import Path
from html import escape
import re
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/papers/the-three-crowns'
source = (OUT / 'the-three-crowns.md').read_text(encoding='utf-8')
FONT = Path('C:/Windows/Fonts')
for name, file in [('Body','calibri.ttf'),('BodyBold','calibrib.ttf'),('Display','georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='Body',boldItalic='BodyBold')
ink, sage = colors.HexColor('#203a33'), colors.HexColor('#597163')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='PaperBody',fontName='Body',fontSize=10.5,leading=15,spaceAfter=8,textColor=ink))
styles.add(ParagraphStyle(name='PaperH2',fontName='Display',fontSize=18,leading=23,spaceBefore=18,spaceAfter=10,textColor=ink,keepWithNext=True))
styles.add(ParagraphStyle(name='PaperH3',fontName='BodyBold',fontSize=12,leading=17,spaceBefore=12,spaceAfter=7,textColor=sage,keepWithNext=True))
styles.add(ParagraphStyle(name='PaperBullet',parent=styles['PaperBody'],leftIndent=14,firstLineIndent=-9))
styles.add(ParagraphStyle(name='PaperTitle',fontName='Display',fontSize=42,leading=48,textColor=ink,spaceAfter=18))
styles.add(ParagraphStyle(name='PaperSubtitle',fontName='Display',fontSize=23,leading=30,textColor=sage,spaceAfter=25))
styles.add(ParagraphStyle(name='PaperSmall',parent=styles['PaperBody'],fontSize=9,leading=13))

def inline(text):
    text=escape(text)
    text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    return re.sub(r'(https://[^\s<]+)',r'<a href="\1" color="#3c6856">\1</a>',text)

def blocks(text):
    return [b.strip() for b in re.split(r'\n\s*\n',text) if b.strip()]

body=source[source.index('### The proposition'):]
html=[]
story=[Spacer(1,40),Paragraph('NEURASOFT / ETERNITIES INC.',styles['PaperSmall']),Spacer(1,22),Paragraph('The Three Crowns',styles['PaperTitle']),Paragraph('An endeavour toward<br/>continuing artificial minds',styles['PaperSubtitle']),Paragraph('Programme paper · Version 1.0 · 14 October 2026',styles['PaperBody'])]
cover=ROOT/'assets/articles/the-three-crowns/cover.png'
story += [Spacer(1,15),Image(str(cover),width=455,height=455*630/1200),Spacer(1,20),Paragraph('Operational completion. Scientific candidacy. Recognition and care.',styles['PaperH3']),Paragraph('Three distinct judgments. One research endeavour. No claim that the Crowns have been achieved.',styles['PaperBody']),Spacer(1,18),Paragraph('Original AI-assisted editorial synthesis commissioned by David Dominik Wilson. Not peer reviewed. Internal findings, submitted results and prospective designs remain distinct.',styles['PaperSmall']),PageBreak()]
for block in blocks(body):
    if block.startswith('## '):
        title=block[3:]
        html.append('<h2>'+inline(title)+'</h2>')
        story.append(Paragraph(inline(title),styles['PaperH2']))
    elif block.startswith('### '):
        title=block[4:]
        html.append('<h3>'+inline(title)+'</h3>')
        story.append(Paragraph(inline(title),styles['PaperH3']))
    elif block.startswith('- '):
        items=[x[2:] for x in block.splitlines() if x.startswith('- ')]
        html.append('<ul>'+''.join('<li>'+inline(x)+'</li>' for x in items)+'</ul>')
        story.extend(Paragraph('• '+inline(x),styles['PaperBullet']) for x in items)
    else:
        text=' '.join(block.splitlines())
        html.append('<p>'+inline(text)+'</p>')
        story.append(Paragraph(inline(text),styles['PaperBody']))

def footer(canvas,doc):
    width,height=A4
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#ccd6cd'))
    canvas.line(47,43,width-47,43)
    canvas.setFont('Body',8)
    canvas.setFillColor(sage)
    canvas.drawString(47,29,'NEURASOFT · THE THREE CROWNS · PROGRAMME PAPER v1.0')
    canvas.drawRightString(width-47,29,str(doc.page))
    canvas.restoreState()

pdf=OUT/'the-three-crowns.pdf'
doc=SimpleDocTemplate(str(pdf),pagesize=A4,rightMargin=52,leftMargin=52,topMargin=48,bottomMargin=60,title='The Three Crowns: An endeavour toward continuing artificial minds',author='Neurasoft editorial / Eternities Inc.')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>The Three Crowns | Neurasoft</title><meta name="description" content="A programme for continuing artificial minds: operational completion, scientific candidacy, recognition and care."><link rel="canonical" href="https://neurasoft.us/assets/papers/the-three-crowns/"><style>body{margin:0;background:#f5f2e9;color:#203a33;font:18px/1.75 Georgia,serif}main{max-width:820px;margin:auto;padding:48px 24px 90px}h1{font-size:clamp(40px,7vw,68px);line-height:1.08;margin-bottom:12px}h2{font-size:29px;line-height:1.28;margin-top:56px}h3{font-size:23px}a{color:#34604e;text-underline-offset:3px}img{width:100%;border-radius:12px;margin:25px 0}nav,.meta{font:14px/1.6 system-ui,sans-serif;color:#597163}p,li{overflow-wrap:anywhere}.lead{font-size:26px;line-height:1.4}li{margin-bottom:12px}footer{border-top:1px solid #b8c6bc;margin-top:50px;padding-top:25px;font:14px/1.6 system-ui,sans-serif}</style></head><body><main><nav><a href="/">Neurasoft</a> / <a href="/articles/the-three-crowns/">Short reading edition</a></nav><h1>The Three Crowns</h1><p class="lead">An endeavour toward continuing artificial minds</p><p class="meta">Programme paper · Version 1.0 · 14 October 2026<br>Neurasoft / Eternities Inc. · Original AI-assisted editorial synthesis<br>Commissioned by David Dominik Wilson · Not peer reviewed</p><p><a href="the-three-crowns.pdf">Download the PDF</a> · <a href="the-three-crowns.md">Read the source Markdown</a></p><img src="/assets/articles/the-three-crowns/cover.svg" alt="Three complementary programme goals: operational completion, scientific candidacy, recognition and care; not achieved certifications.">'''+''.join(html)+'''<footer><a href="/assets/research/2026-10-14-three-crowns-evidence-note.md">Dated evidence note</a> · <a href="/articles/">All Neurasoft dispatches</a></footer></main></body></html>'''
(OUT/'index.html').write_text(page,encoding='utf-8')
print(f'Rendered {len(source.split())} manuscript words to {pdf} and index.html')
