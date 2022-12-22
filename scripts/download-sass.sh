#!/bin/bash

set -e

# install the dart sass binary for x86_64 linux

# change to the desired release tag and sha256 checksum
# <https://github.com/sass/dart-sass/releases/>
dart_release_tag=${dart_release_tag:-1.56.1}
dart_tarball_checksum=${dart_tarball_checksum:-a5cf9e1f5db9456faffa440779a21a49cee65755c21617b75d1367d11448c59b}

dart_tarball_filename=dart-sass-"$dart_release_tag"-linux-x64.tar.gz
dart_tarball_url=https://github.com/sass/dart-sass/releases/download/"$dart_release_tag"/"$dart_tarball_filename"

curl -sSL -o "$dart_tarball_filename" "$dart_tarball_url"

if ! sha256sum -c <(echo "$dart_tarball_checksum $dart_tarball_filename"); then
    echo "bad checksum for $dart_tarball_filename"
    echo "make sure you you set the right checksum in this script"
    exit 1
fi

user_bin_dir=$HOME/.local/bin

mkdir -p "$user_bin_dir"

tempdir=$(mktemp -d)

tar -x -f "$dart_tarball_filename" -C "$tempdir" dart-sass/sass
mv "$tempdir"/dart-sass/sass "$user_bin_dir"
rm -r "$tempdir" "$dart_tarball_filename"

echo "sass was successfully installed! make sure $user_bin_dir is in your PATH"
echo "run this command to add it to your path now:"
# shellcheck disable=SC2016
echo 'echo PATH='"$user_bin_dir"':"$PATH" >> ' "$HOME/.bashrc && source $HOME/.bashrc"
