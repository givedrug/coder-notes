#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import re

note_name = 'coder-notes'
base_dir = './docs_copy/'
base_space = 0
uncheck_dir_list = ['.idea', 'src']


def changeFile(base, name):
    fullname = os.path.join(base, name)
    fr = open(fullname, 'r')
    lines = fr.readlines()
    fr.close()

    # 替换附件链接
    def complete(value):
        v1 = value.group(1)
        v2 = value.group(2)
        new_url = 'https://givedrug.github.io/' + note_name + '/' + base.lstrip(base_dir) + '/' + v2
        new_url = new_url.replace(' ', '%20')
        return '[' + v1 + '](' + new_url + ')'

    # 替换附件中的链接（仅替换附件，网址与图片无需处理）
    # 网址：[终于明白六大类UML类图关系了](https://segmentfault.com/a/1190000021317534)
    # 图片：![](assets/UML类图中的关系/image-20230228113838354.png)
    # 附件：[文件](assets/类型02-字符串/数独.rar)
    for idx, line in enumerate(lines):
        if 'http' not in lines[idx]:
            lines[idx] = re.sub(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', complete, line)

    # 添加文章标题（这样可以避免docsify中显示文内标题时，缺失第一个标题）
    lines.insert(0, '# ' + name.rstrip('.md') + '\n\n')

    fw = open(fullname, 'w')
    fw.writelines(lines)
    fw.close()


def checkAllFile(base, file, base_space):
    list = os.listdir(base)
    list.sort()
    for name in list:
        fullname = os.path.join(base, name)
        # 排除assets文件夹
        if 'assets' in name:
            continue

        # 文件夹
        if os.path.isdir(fullname) and name not in uncheck_dir_list:
            file.write(' ' * base_space + '- <font color="#42b983"><b>' + name + '</b></font>' + '\n')
            checkAllFile(fullname, file, base_space + 2)

        # 文件
        if os.path.isfile(fullname) and base != base_dir and name.endswith('.md'):
            file.write(' ' * base_space + '- [' + name.rstrip('.md') + '](' +
                       fullname.lstrip(base_dir).replace(' ', '%20') + ')' + '\n')
            changeFile(base, name)


def main():
    sidebar_file = open(base_dir + '_sidebar.md', 'w')
    # 侧边栏第一行是README
    sidebar_file.write('- [<b>README</b>](README.md)' + '\n')
    checkAllFile(base_dir, sidebar_file, base_space)
    sidebar_file.close()


if __name__ == '__main__':
    main()
