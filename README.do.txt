## This file is the source of README.rst

======= pygments-doconce =======

-----------------------------------------
Syntax coloring for DocOnce fils
-----------------------------------------

===== Overview =====

This package provides a "Pygments": "http://pygments.org/" lexer for
"DocOnce": "http://hplgit.github.io/doconce" files.
The lexer is published as an entry point and, once installed, Pygments will
pick it up automatically.

You can then use the ``doconce`` language with Pygments:

!bc sys
$ pygmentize -l doconce test.do.txt
!ec
In "Sphinx": "http://sphinx-doc.org/" documents the lexer is selected with
the `highlight` directive:

!bc
.. highlight:: doconce
!ec

Thanks to pygments-openssl project for providing a template https://github.com/stefanholek/pygments-openssl


===== Installation =====

Use your favorite installer to install `pygments-doconce` into the same
Python you have installed Pygments.
Constructing an egg from repository:

!bc sys
$ git clone https://github.com/hplgit/pygments-doconce.git
$ cd pygments-doconce
$ sudo python setup.py install
!ec
DocOnce is needed for the lexer to work,

!bc sys
$ sudo pip install -e git+https://github.com/hplgit/doconce#egg=doconce
!ec

To verify the installation of `pygments-doconce` run:

!bc sys
$ pygmentize -L lexer | grep -i doconce
* doconce:
DocOnce
!ec
