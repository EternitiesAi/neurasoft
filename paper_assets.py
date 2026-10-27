"""Keep manifest-bound public research attachments byte-identical after site formatting."""
from hashlib import sha256
from pathlib import PurePosixPath
import shutil

def finish(build):
    paper=build.ROOT/'assets/papers/when-history-changes-the-agent'
    manifest=paper/'manifest.sha256'
    if not manifest.exists():
        raise ValueError('Missing methods-paper manifest')
    names=[]
    for row in manifest.read_text(encoding='utf-8').splitlines():
        digest,name=row.split('  ',1)
        if PurePosixPath(name).name != name or '\\' in name or name in ('.','..'):
            raise ValueError('Paper manifest must contain plain file names')
        source=paper/name
        if source.is_symlink() or sha256(source.read_bytes()).hexdigest()!=digest:
            raise ValueError('Paper artifact differs from its reviewed manifest: '+name)
        names.append(name)
    if len(names)!=len(set(names)):
        raise ValueError('Duplicate paper manifest entry')
    destination=build.OUT/'assets/papers/when-history-changes-the-agent'
    destination.mkdir(parents=True,exist_ok=True)
    for name in names+['manifest.sha256','research-bundle.zip']:
        shutil.copyfile(paper/name,destination/name)
    print('Research attachments preserved byte-for-byte against their manifest.')
