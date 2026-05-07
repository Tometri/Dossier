git init == initializes a new local repo.
git remote add origin <repo_url> == ['git remote' = manages connections, 'add' = add new remote connection, 'origin' = give nickname for remote repo's url (origin is common)]
git branch -M main == rename the branch to main. [-M flag means 'move/rename']
git add  == git add tells git which changes to include in the next commit. [a single file can be added by naming it with 'git add example.ext'. 'git add .' adds all changed files. To add only specified extensions use 'git add *.ext'.]
git commit -m 'commit message' == commits staged files with a message using the -m (message) flag.
git status == used to check the status of files.
git push -u origin main == used for the first time pushing to a branch.
git push == sends locally committed changes to remote repo.
git clone https://github.com/username/example_repo.git == Clones a repository.
#forks == copies of code made outside the repository.
#branches == copies of code made inside the repository.
git branch == creates a new branch from the branch you're in currently [git branch new-branch-name]
git switch == switches to a branch [git switch new-branch-name]
git checkout -b <new-branch-name> == create and switch to a branch in a single command.
git pull == updates the branch currently being worked on. 
git merge <branch-name> == brings changes from one branch to another.
#pull requests allow you to suggest changes to the repository and create edits from one branch to another.Pull requests are like merges but allow you to merge branches across repositories rather than only in the same repo.

