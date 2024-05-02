#!/bin/bash

outputDir="./compiled"
filename="article"
openPDF=0
echo "Compiling article.tex"

# d -- Specify output directory(default -- ./compiled)
# f -- Specify input filename(default -- article.tex)
# o -- Open compiled pdf in edge
while getopts d:f:o flag
do
    case "${flag}" in
        d) outputDir=${OPTARG};;
        f) filename=${OPTARG};;
        o) openPDF=$(("$openPDF" ^ 1));;
    esac
done

#Compile two times to sort out all the references
output=$(pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory $outputDir "${filename}.tex" | grep ".*:[0-9]*:.*")
if (( ${#output} > 0 )) ; then
    echo $output
    exit 1
fi

pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory $outputDir "${filename}.tex" > "${outputDir}/compile.log"
cp "${outputDir}/${filename}.pdf" "./"

echo "Compilation succesfull, ${filename}.pdf was updated"
relativePath=$(realpath "./${filename}.pdf" | sed -r "s/\//\\\/g")

if [ "$openPDF" = 1 ] ; then
    msedge.exe "\\\\wsl.localhost\Ubuntu-22.04${relativePath}"
fi
