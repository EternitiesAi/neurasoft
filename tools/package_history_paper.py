"""Reproducible bundle of the public manuscript and analytical examples."""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
root=Path(__file__).resolve().parents[1]/'assets/papers/when-history-changes-the-agent'
names=['when-history-changes-the-agent.pdf','when-history-changes-the-agent.md','verify_analytic_examples.py','analytic-checks.json','zenodo-metadata.json','DEPOSIT.md','index.html','paper.css']
manifest=''.join(sha256((root/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in names)
(root/'manifest.sha256').write_text(manifest,encoding='utf-8',newline='\n')
with ZipFile(root/'research-bundle.zip','w',compression=ZIP_DEFLATED) as bundle:
    for name in names+['manifest.sha256']:
        info=ZipInfo(name,date_time=(2026,10,27,0,0,0))
        info.compress_type=ZIP_DEFLATED
        bundle.writestr(info,(root/name).read_bytes())
print('Packaged public manuscript and analytical examples; '+str(len(names))+' hashed files.')
