import os

file_dir = ['./_site']
file_dir = ['./_data', './_includes', './_layouts', './_projects', './_website_2014', './assets']
# './libs'
keyword = """.*be at ACL.*"""

for dir_ in file_dir:
	print('\n','-'*25,dir_,'-'*25,'\n')
	os.system('wsl -e sh -c "grep -worne \'' + keyword + '\' ' + dir_ + '"')
	print('\n','*-'*25,'\n')
os.system('wsl -e sh -c "grep -wone \'' + keyword + '\' ' + '* .*"')