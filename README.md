# otf2ttf

This is a simple command=line script that can be installed and used to
convert OTF (OpenType Font) and TTF (TrueType Font) file formats.

How to use it:

    $ pip install otf2ttf
    $ otf2ttf MyFont.ttf


## Background

Currently these 2 PDF libraries, require TTF fonts, which is why this script
was packaged up for ease of use:

- [ReportLab](https://www.reportlab.com/)
- [FPDF](https://github.com/reingart/pyfpdf)

This package was built using a sample script from the `fonttools` project.

Below is a link to the original script:

- [otf2ttf.py](https://github.com/fonttools/fonttools/blob/master/Snippets/otf2ttf.py)

This package was created to ease the use of non-programmers looking to 
convert their files.

More information about this script can be found in
[Issue #1283](https://github.com/fonttools/fonttools/issues/1283).


