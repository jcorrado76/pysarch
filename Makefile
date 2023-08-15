code-maat-git-log:
	cd ../code-maat && git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat --before=2013-11-01

.PHONY: code-maat-git-log
