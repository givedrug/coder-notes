#!/bin/bash
doc_path=docs_copy/

function deal_file(){
    for element in `ls -1 $1 | sed "s/[ ]/\\\ /g"`
    do
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ] ;
        then
            if [ "$element" != "assets" ];then
                deal_file $dir_or_file
            fi
        else
            if [[ "$element" == *"md" ]]; then
              # md文档开头位置增加一个标题，这样docsify显示内部标题的时候就不会忽略原本的第一个标题了
              sed -i '1i\#\n' $dir_or_file
            fi
        fi
    done
}

# -d 只列出目录
root_dir=`ls -d docs_copy/*/`

for dir in $root_dir
do
    if [ "$dir" = "." ]
    then
        continue
    else
        # 去掉最后一个字符/
        deal_file `echo $dir | sed 's/.$//'`
    fi
done