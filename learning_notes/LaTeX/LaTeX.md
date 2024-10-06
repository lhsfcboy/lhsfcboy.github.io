# LaTeX

- TeX
高德纳教授开发的排版引擎,
同时也是该引擎使用的标记语言(Markup Lang)的名称.
TeX引擎则输出 dvi 格式的文档.

- LaTeX
L.Lamport教授开发的基于TeX的排版系统

## 编译套装

- TexLive
大而全, 体积上G. 
内置了可以处理中文的XeLaTeX.

- MiKTeX
MiKTeX体积小, 会在需要时自动下载配置缺少的包. 
内置了可以处理中文的XeLaTeX.
[https://miktex.org/](https://miktex.org/).
安装完成有运行"Miktex console"进行配置(选择"以管理员身份运行").
点击"Packages"标签,然后依次安装ctex和CJK包, 以便支持中文.

- pdfTeX/pdfLaTeX

Hàn Thế Thành 博士在他的博士论文中提出了 pdfTeX 这个对 TeX 引擎的扩展.
pdfTeX 直接输出 pdf 格式文档.

- XeTeX/XeLaTeX

XeTeX 引擎直接支持 Unicode 字符.
使用 XeTeX 引擎需要使用 UTF-8 编码.
中文环境最常用的LaTex版本.

- bibtex

- TinyTeX 是基于 TeX Live 的瘦身版本,覆盖了大多数常用包,安装下来占用大概 150 MB 空间,比起原 TeX Live 动辄上 GB 的身躯实在要小不少.
TinyTeX 支持 Linux,macOS 及 Windows.
[https://yihui.name/tinytex/](https://yihui.name/tinytex/)

默认没有中文支持的相关包.还要安装ctex等一堆包.
装完大概是230M.texdoc这种命令自然也是没有了的.

## 常用的云端环境

- Overleaf
  - overleaf.com
- CloudLaTex
  - cloudlatex.io


## Windows下的环境搭建

[Installing TeX Live over the Internet](https://www.tug.org/texlive/acquire-netinstall.html)

```bat
rem to delete temp files before the generating work done
del *.bib *.blg *.bbl *.aux *.log *.brf *.nlo *.out *.dvi *.ps *.lof *.toc *.fls *.fdb_latexmk *.pdfsync *.synctex*.gz *.ind *.ilg *.idx

rem to generate PDF with Refs
pdflatex *.tex
bibtex *.aux
pdflatex *.tex
pdflatex *.tex

rem to delete temp files after the generating work done
del *.bib *.blg *.bbl *.aux *.log *.brf *.nlo *.out *.dvi *.ps *.lof *.toc *.fls *.fdb_latexmk *.pdfsync *.synctex*.gz *.ind *.ilg *.idx
```



### 基本的排版流程
第一步Latex编译,可以获得.aux文件,.dvi文件,.log文件以及.gz文件;

第二步Bibtex编译,可以获得.blg(性能监视器文件)和.bbl文件;

第三步Latex编译,获得新的.aux文件,.dvi文件,.log文件以及.gz文件;

第四步再次Latex编译.

.tex --(latex)--> .dvi --(dvipdfmx)--> .pdf

.tex --(xelatex/pdf/atex) --> .pdf


### 一个编译的例子
```
latex -interaction=nonstopmode %.tex|(編譯 latex 檔案)
bibtex %.aux|(編譯論文引用的資料)
latex -interaction=nonstopmode %.tex|(再編譯一次)
latex -interaction=nonstopmode %.tex|(再編譯一次)
xdvi %.dvi(產生 pdf 檔)
```

使用XeLaTeX且没有参考文献时:
```
xelatex -interaction=nonstopmode %.tex|
xelatex -interaction=nonstopmode %.tex|
xelatex -interaction=nonstopmode %.tex|
xdvi %.dvi
```
省去了bibtex以避免无谓的编译警告

## 中文文档
LaTeX 中文文档的排版有各种方式,例如CCT,CJK,xeCJK 等等.
目前最优秀的方式是用ctex 文档类来排版中文文档,它在其它各种方式的基础上以一致的方式解决了中文排版的问题.
> \documentclass[UTF8]{ctexart}
使用这种方式,只需要将文档类从英文的article 改成ctexart,所有中文环境和章节编号等等都已经按照中文习惯设置好了,简单易行.另外,对于book 和report 文档类,也有对应的ctexbook 和ctexrep 中文文档类,其用法类似.

例子中的UTF8 这个可选参数指明了中文文档的编码.编码主要有这两种:GBK 和UTF8,而不同的LaTeX 编辑器对中文文档的默认编码不同.

## 附录

### LaTex常见的文件类型汇总


LaTex常见的文件类型汇总

| 扩展名 | 详情                                                                                                            |
| ------ | --------------------------------------------------------------------------------------------------------------- |
| .tex   | LaTeX和TeX源文件,进行编译处理.                                                                                |
| .dvi   | 一种不依赖设备的文件..dvi文件是latex编译运行后的主要结果.用户可以使用DVI预览软件查看.dvi内容.                |
| .pdf   | PDF文件,文件是pdflatex编译运行后的主要结果.                                                                   |
| .aux   | 存放交叉引用信息                                                                                                |
| .bbl   | 由BiBTeX 生成,会被LaTeX使用的参考文献列表                                                                      |
| .bib   | 参考文献数据库,以便引用                                                                                        |
| .toc   | 存储对于章节目录,TEX 程序第一次编译文档时会生成 .toc 临时文件,下一次编译时将读取.toc 文件内容并生成新的目录. |
| .lof   | 类似于.toc,不过是用来存储插图目录.                                                                            |
| .lot   | 类似于.toc,不过是用来存储表格目录.                                                                            |

其他的文件类型汇总

| 扩展名 | 详情                                                                                                                                                              |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .blg   | 存储BiBTeX日志                                                                                                                                                    |
| .bst   | 指定BiBTeX样式文件,即BiBTeX将.bib生成.bbl的格式,不同的期刊有不同的参考文献样式                                                                                  |
| .cls   | 定义文章的排版布局,即定义.tex稿件类型格式,使用\documentclass{article} 命令进行指定                                                                              |
| .dtx   | 程序说明文件的源文件,含有类包程序*.cls,宏包程序*.sty,说明或格式程序*.tex和配置程序*.cfg等多种程序.                                                            |
| .ins   | 用来解压和重建.dtx文件.用户下载了一个LaTeX包后,通常会获取一个.dtx和一个.ins文件,使用*.ins安装文件的好处就在于它能够一次性自动地完成对*.dtx文件的分类重建工作. |
| .fd    | 新添加的字体描述文件,用来告知LaTeX新添加的字体                                                                                                                   |
| .log   | 记录上一次编译器运行的日志.                                                                                                                                      |
| .idx   | 存储索引内容的文件,可用makeindex排序后创建索引文件.ind.                                                                                                         |
| .ind   | 处理.idx文件得到的索引文件,下一次编译时将读取.ind文件内容并生成新的索引文件.                                                                                    |
| .ilg   | makeindex的日志文件.                                                                                                                                             |
| .sty   | LaTeX宏包文件,使用\usepackage将.sty加载到LaTeX中.                                                                                                               |
