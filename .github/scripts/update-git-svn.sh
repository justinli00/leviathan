if [ ! -d svn-repo ];
then
    svn checkout --username $env:SVN_USERNAME --password $env:SVN_PASSWORD $env:SVN_URL svn-repo
else
    cd svn-repo
    svn update --username $env:SVN_USERNAME --password $env:SVN_PASSWORD $env:SVN_URL
    cd ..
fi