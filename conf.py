from recommonmark.parser import CommonMarkParser
source_parsers = {
'.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
master_doc = 'index' 
project = u'Paperwork'
html_static_path = ['_static']


html_js_files = [
    'https://www.paperworkday.net/paper.generate.js',
]

