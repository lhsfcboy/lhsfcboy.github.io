#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
echo "$BASEDIR"

cd $BASEDIR

## Core latex/pdflatex auxiliary files:
rm -f *.aux
rm -f *.lof
rm -f *.log
rm -f *.lot
rm -f *.fls
rm -f *.out
rm -f *.toc
rm -f *.fmt
rm -f *.fot
rm -f *.cb
rm -f *.cb2

## Intermediate documents:
rm -f  *.dvi
rm -f  *.xdv
rm -f  *-converted-to.*
# these rules might exclude image files for figures etc.
# *.ps
# *.eps
# *.pdf

## Generated if empty string is given at "Please type another file name for output:"
rm -f  .pdf

## Bibliography auxiliary files (bibtex/biblatex/biber):
rm -f *.bbl
rm -f *.bcf
rm -f *.blg
rm -f *-blx.aux
rm -f *-blx.bib
rm -f *.run.xml

## Build tool auxiliary files:
rm -f *.fdb_latexmk
rm -f *.synctex
rm -f *.synctex\(busy\)
rm -f *.synctex.gz
rm -f *.synctex.gz\(busy\)
rm -f *.pdfsync

## Auxiliary and intermediate files from other packages:
# algorithms
rm -f *.alg
rm -f *.loa

# achemso
rm -f acs-*.bib

# amsthm
rm -f *.thm

# beamer
rm -f *.nav
rm -f *.pre
rm -f *.snm
rm -f *.vrb

# changes
rm -f *.soc

# cprotect
rm -f *.cpt

# elsarticle (documentclass of Elsevier journals)
rm -f *.spl

# endnotes
rm -f *.ent

# fixme
rm -f *.lox

# feynmf/feynmp
rm -f *.mf
rm -f *.mp
rm -f *.t[1-9]
rm -f *.t[1-9][0-9]
rm -f *.tfm

#(r)(e)ledmac/(r)(e)ledpar
rm -f *.end
rm -f *.?end
rm -f *.[1-9]
rm -f *.[1-9][0-9]
rm -f *.[1-9][0-9][0-9]
rm -f *.[1-9]R
rm -f *.[1-9][0-9]R
rm -f *.[1-9][0-9][0-9]R
rm -f *.eledsec[1-9]
rm -f *.eledsec[1-9]R
rm -f *.eledsec[1-9][0-9]
rm -f *.eledsec[1-9][0-9]R
rm -f *.eledsec[1-9][0-9][0-9]
rm -f *.eledsec[1-9][0-9][0-9]R

# glossaries
rm -f *.acn
rm -f *.acr
rm -f *.glg
rm -f *.glo
rm -f *.gls
rm -f *.glsdefs

# gnuplottex
rm -f *-gnuplottex-*

# gregoriotex
rm -f *.gaux
rm -f *.gtex

# hyperref
rm -f *.brf

# knitr
rm -f *-concordance.tex
# TODO Comment the next line if you want to keep your tikz graphics files
rm -f *.tikz
rm -f *-tikzDictionary

# listings
rm -f *.lol

# makeidx
rm -f *.idx
rm -f *.ilg
rm -f *.ind
rm -f *.ist

# minitoc
rm -f *.maf
rm -f *.mlf
rm -f *.mlt
rm -f *.mtc[0-9]*
rm -f *.slf[0-9]*
rm -f *.slt[0-9]*
rm -f *.stc[0-9]*

# minted
rm -f *.pyg

# morewrites
rm -f *.mw

# nomencl
rm -f *.nlo

# pax
rm -f *.pax

# pdfpcnotes
rm -f *.pdfpc

# sagetex
rm -f *.sagetex.sage
rm -f *.sagetex.py
rm -f *.sagetex.scmd

# scrwfile
rm -f *.wrt

# sympy
rm -f *.sout
rm -f *.sympy

# pdfcomment
rm -f *.upa
rm -f *.upb

# pythontex
rm -f *.pytxcode
# thmtools
rm -f *.loe

# TikZ & PGF
rm -f *.dpth
rm -f *.md5
rm -f *.auxlock

# todonotes
rm -f *.tdo

# easy-todo
rm -f *.lod

# xindy
rm -f *.xdy

# xypic precompiled matrices
rm -f *.xyc

# endfloat
rm -f *.ttt
rm -f *.fff

## Editors:
# WinEdt
rm -f *.bak
rm -f *.sav

# Kile
rm -f *.backup

# KBibTeX
rm -f *~[0-9]*


# expex forward references with \gathertags
rm -f *-tags.tex

# read -n 1 -p "Press any key to continue..."
