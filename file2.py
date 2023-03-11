import sys

a = 100
b = dict()
c = None

ls = [1,2,3,4]
s = {1,2,3,4}
dc = {i:i for i in range(5)}


'''
git diff - axirinci commitden sonra neler (unstaged changes) deyisilib in directory. Eger stage/add olsa, hec ne gotermeyecek
git commit -am  'message'- stage all/add and commit, bir command ile
HEAD - last commit
git diff HEAD - every change since last commit, staged olunmus ve olunmamis
git diff --staged or --cached: shows changes only if staged
git diff file1.py:narrow down for one file

'''