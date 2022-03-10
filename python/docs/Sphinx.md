install sphinx  
`pip install sphinx`  
setup sphinx (usually within a docs folder)  
`sphinx-quickstart`  
update `conf.py` with a directory pointer and `index.rst` with modules  
create modules  
`sphinx-apidoc -o . ../mypkg`  
generate documentation  
`make html`