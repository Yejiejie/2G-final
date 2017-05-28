# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, escape
import os

app = Flask(__name__)
os.getcwd()

dict_hero_skill = dict()
dict_hero_story = dict()
file_names = [x for x in os.listdir('skill')]
for f in file_names:
    with open('skill/{fn}'.format(fn = f),'r') as file_object:
        dict_hero_skill[f.strip('.txt')] = file_object.read().splitlines()
for f in file_names:
    with open('story/{fn}'.format(fn = f),'r') as file_object:
        dict_hero_story[f.strip('.txt')] = file_object.read().splitlines()

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    name = request.form['name']
    return render_template('results.html',
                           the_name = name,
                           the_skill = dict_hero_skill['{sn}'.format(sn = name)],
                           the_story = dict_hero_story['{sn}'.format(sn = name)],
                           )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='欢迎来到王者荣耀')

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('表单内容', '访问者IP', '浏览器', '运行结果')
    return render_template('viewlog.html',
                           the_title='查看日志',
                           the_row_titles=titles,
                           the_data=contents,)

if __name__ == '__main__':
    app.run(debug=True)
