#! /usr/bin/env bash
# pandoc -t beamer liif.md --pdf-engine=xelatex -V theme:metropolis -o liif.pdf

# while inotifywait -e close_write liif.md; do ./compile.sh; done

pandoc \
    -t beamer pydesktop.md \
    --filter pandoc-beamer-block \
    -V themeoptions\:subsectionpage=progressbar,block=fill \
    -V theme:metropolis \
    -o pydesktop.pdf
