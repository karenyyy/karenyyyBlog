git config credential.helper store
git add .
git commit -m 'update'
git push -u origin master
git push -f heroku master
