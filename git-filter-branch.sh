git filter-branch --env-filter 'if [ "$GIT_AUTHOR_EMAIL" = "luis.vivero@slickdeals.net" ]; then
     GIT_AUTHOR_EMAIL="916632+luix@users.noreply.github.com";
     GIT_AUTHOR_NAME="LuiX";
     GIT_COMMITTER_EMAIL=$GIT_AUTHOR_EMAIL;
     GIT_COMMITTER_NAME="$GIT_AUTHOR_NAME"; fi' -- --all
