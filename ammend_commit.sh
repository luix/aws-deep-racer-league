#!/bin/sh

git filter-branch --env-filter '

OLD_EMAIL="vivero@llb-imac-02.library.unlv.edu"
CORRECT_NAME="LuiX"
CORRECT_EMAIL="916632+luix@users.noreply.github.com"

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags

# https://help.github.com/en/articles/changing-author-info
