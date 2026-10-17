"""NVIDIA Inception membership: the unaltered badge and NVIDIA's own wording, in every page footer (2026-10-17)."""

BADGE = '/assets/brand/nvidia-inception-program-badge.svg'
LINE = 'Neurasoft is part of Eternities, a member of the NVIDIA Inception program.'
# NVIDIA's "Writing About the Program": wherever the logo appears, this legal line appears too, exactly
LEGAL = ('© 2026 NVIDIA, the NVIDIA logo, and NVIDIA Inception are trademarks and/or registered trademarks of NVIDIA '
         'Corporation in the U.S. and other countries.')
BLOCK = ('<div class="footer-inception"><div class="footer-inception-row"><img src="' + BADGE + '" alt="NVIDIA Inception program badge"'
         ' width="139" height="60" loading="lazy" decoding="async"><p>' + LINE + '</p></div>'
         '<p class="footer-inception-legal">' + LEGAL + '</p></div>')
MARKER = '<div class="footer-bottom">'


def install(b):
    previous_footer, previous_shell = b.footer, b.shell

    def footer():
        text = previous_footer()
        if text.count(MARKER) != 1:
            raise ValueError('Review the Inception badge placement: the footer-bottom marker changed')
        return text.replace(MARKER, BLOCK + MARKER, 1)

    def shell(route, title, description, body, active='', extra='', article=False):
        previous_shell(route, title, description, body, active, extra + '<link rel="stylesheet" href="/assets/inception.css">', article)

    b.footer, b.shell = footer, shell
