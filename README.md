# leviathan
GitHub repository for Leviathan team. Used for managing GHA workflows and more extensive testing, building, and other time-sensitive processes.
Also contains other tools used for 

Notes:
- All of the files in executables were originally stored on the SVN, but were moved here for the sake of visibility. 
    - They were compiled with [pyinstaller](https://pyinstaller.org/en/stable/)
    - Source for them is visible in their corresponding .py files
- github_dispatch.exe
      - Triggers workflows based on repository dispatch
      - Can also be used to pass parameters to workflows
      - Will not work without a token, like repo_dispatch.token. For obvious reasons the repo_dispatch.token doesn't actually contain a token. You'll need to generate one yourself.
- run_tests.exe
      - Used within check_tests.yaml. Runs all tests in Unity project, then formats and archives results
- check_results.exe
      - Displays results of specified test, within range of specified revisions if provided
- For details on usage, use "(executable) --help"

