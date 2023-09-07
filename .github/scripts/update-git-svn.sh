#! /usr/bin/sh
if [ ! -d svn-repo ];
then
    svn checkout --username $SVN_USERNAME --password $SVN_PASSWORD $SVN_URL svn-repo
else
    cd svn-repo
    svn update --username $SVN_USERNAME --password $SVN_PASSWORD $SVN_URL
    cd ..
fi

dir