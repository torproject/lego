#!/usr/bin/env bash

# TODO: add help text so the user knows what the script does
# TODO: add a dry-run option so the user can see what's happening without actually pushing
# TODO: cut down on script output so the user can actually read it without a wall of git output

set -eu

# list of directories to act on
# to make this script update a new lektor site, add its repo name here
LEGO_WEB_DIRECTORIES=(
    community
    dev
    donate-static
    gettor-web
    manual
    newsletter
    styleguide
    support
    template
    tpo
)

declare -a success_dirs  # list the directories that successfully updated at the end of the script
declare -a error_dirs  # list the directories that failed to update

# this is the parent of the directory the script resides in
web_repos_dir=$(readlink -f -- "$0" | rev | cut -f 3- -d / | rev)

latest_commit_hash=$(git -C "$web_repos_dir/lego" log --oneline -1 origin/main|awk '{print $1;}')

for web_dir in ${LEGO_WEB_DIRECTORIES[@]}; do
    repo_dir="$web_repos_dir/$web_dir"

    # HACK: if any of the statements in the parentheses fail, the directory is added to error_dirs
    # else, it's added to success_dirs

    # MICRO-OP: using `git -C` lets us set the git working directory without changing the *actual*
    # working directory, which can be error prone
    ( \
        git -C "$repo_dir" checkout -b update-lego-$latest_commit_hash origin/main && \
        git -C "$repo_dir/lego" pull origin main && \
        git -C "$repo_dir" add "$repo_dir/lego" && \
        git -C "$repo_dir" commit -m 'Update lego to latest commit `'$latest_commit_hash'`' && \
        git -C "$repo_dir" push origin update-lego-$latest_commit_hash && \
        success_dirs+=("$web_dir")
    ) || error_dirs+=("$web_dir")
done

# if $success_dirs and $error_dirs are empty, the end of the script exits abnormally
set +u

# BUG: this didn't fire during my testing for some reason
# so i'm commenting out the `if` in case the length check is the issue
#if [[ ${#success_dirs[@]} -gt 0 ]]; then
    echo -e '\033[0;mSucceeded:\033[0;32m'
    for dir_name in ${success_dirs[@]}; do
        printf "\t%s:\thttps://gitlab.torproject.org/tpo/web/%s/-/merge_requests/new?merge_request%5Bsource_branch%5D=%s\n" "$dir_name" "$dir_name" update-lego-$latest_commit_hash
    done
#fi


if [[ ${#error_dirs[@]} -gt 0 ]]; then
    echo -e '\033[1;31mERRORED:'
    for dir_name in ${error_dirs[@]}; do
        echo $dir_name
    done
    printf '\033[0m'
    exit 1
fi
