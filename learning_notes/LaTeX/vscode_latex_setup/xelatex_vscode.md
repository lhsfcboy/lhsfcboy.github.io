# XeLaTeX on VSCode

## 

```json
{
    "window.zoomLevel": 1,
    "latex-workshop.latex.clean.enabled": true,
    "latex-workshop.latex.recipes": [
        {
          "name": "xelatex",
          "tools": [
            "xelatex"
          ]
        },
      ],
    "latex-workshop.latex.tools": [
        {
          "name": "xelatex",
          "command": "xelatex",
          "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-pdf",
            "%DOC%"
          ]
        }
      ]
}
```

```tex
\documentclass[12pt,UTF8]{ctexart}
    %ctexrep - report ; ctexbook - book ; ctexart - article
\usepackage{xeCJK}

\setCJKmainfont{NotoSerifCJKsc-Bold}

\author{匿名}
\title{诗经}

\begin{document}
\maketitle
\begin{center}
\begin{Large}
    \begin{verse}
    关关雎鸠，在河之洲。窈窕淑女，君子好逑。\\
    参差荇菜，左右流之。窈窕淑女，寤寐求之。\\
    求之不得，寤寐思服。悠哉悠哉，辗转反侧。\\
    参差荇菜，左右采之。窈窕淑女，琴瑟友之。\\
    参差荇菜，左右芼之。窈窕淑女，钟鼓乐之。\\
    \end{verse}
\end{Large}
\end{center}
\end{document}
```