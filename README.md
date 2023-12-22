## leviathan
GitHub repository for Leviathan team. Used for managing GHA workflows and more extensive testing, building, and other time-sensitive processes.
Also contains other tools used in the build/test pipeline.

# Usage
## Workflows
The server is intended to be run on a self-hosted runner. Workflows should check out, update, and delete directories as necessary. That said, make sure that your runner has enough disk space. It may also be helpful to delete the svn-repo folder from time to time to get rid of extraneous metadata files.

The runner structures its directories as follows:
- _work/
    - svn-repo/             | _The directory containing the Unity project._
    - svn-installer/        | _The directory containing everything needed to create an installer by running an Inno Script._
    - svn-build/            | _The directory weekly builds will be uploaded to._
    - svn-daily-build/      | _The directory daily builds will be uploaded to._
    - svn-tests/            | _The directory test results builds will be uploaded to._

The first two directories, svn-repo and svn-installer, should persist between workflow runs. 
The last three directories are sparsely checked out in order to upload build and/or test artifacts, and then are promptly deleted.

To run any tests you have written, create a folder in your Unity project called Hooks. The folder structure should look something like this:
- svn-repo/                 | _The directory containing the Unity project._
    - _Unity Folders_/      | _The folders containing the assets, packages, project settings, etc. for your project
    - Hooks/
        - test_artifacts/
        - run_tests.exe
        - hook_settings.json

## Executables
All of the files in executables were originally stored on the SVN, but were moved here for the sake of visibility. Only run_tests.exe is actually used in any of the workflows. This should be stored in "svn-repo/Hooks/", along with another folder called "test_artifacts". These paths can be modified in run-test.yaml.
- They were compiled with [pyinstaller](https://pyinstaller.org/en/stable/)
- For details on usage, use "(executable) --help"
- Source for them is visible in their corresponding .py files
- github_dispatch.exe
    - Triggers workflows based on repository dispatch
    - Can also be used to pass parameters to workflows
    - Will not work without a token, like repo_dispatch.token. For obvious reasons the repo_dispatch.token doesn't actually contain a token. You'll need to generate one yourself.
- run_tests.exe
    - Used within check_tests.yaml. Runs all tests in Unity project, then formats and archives results
- check_results.exe
    - Displays results of specified test, within range of specified revisions if provided
    

