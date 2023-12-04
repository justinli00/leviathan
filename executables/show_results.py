#looks up named keyword and prints results
import argparse
from run_tests import run_cmd, check_svn_clt
import pandas as pd
from os import remove
from colorama import init
from termcolor import colored

if __name__ == "__main__":
    init() #colorama module

    parser = argparse.ArgumentParser(description='Looks up results of individual tests across multiple revisions and prints them to command line.' + 
                                                'Must be run from inside an svn repository.')
    parser.add_argument('--test', type=str, required=True,
        help='The name of the test to look up')
    parser.add_argument('--start', type=int,
        help='The revision number to start on. If not supplied, starts with earliest revision.')
    parser.add_argument('--end', type=int,
        help='The revision number to end on. If not supplied, goes to until HEAD revision.')
    args = parser.parse_args()

    #make sure that svn is installed
    check_svn_clt()

    test = args.test    
    start = args.start if args.start is not None else 0

    #clamp the end to the head
    head = int(run_cmd(['svn','info','-r','HEAD','--show-item','revision'])[0]) 
    end = min(args.end, head) if args.end is not None else head

    #get the names of the test logs to look through; do not include any past end
    test_logs = run_cmd(['svn','ls','-r','HEAD','https://svn.digipen.edu/projects/leviathan/trunk/TEST_LOGS'])
    test_logs = [ test_log for test_log in test_logs if
                    len(test_log) > 0 and
                    int(test_log[8:12]) <= end and 
                    int(test_log[8:12]) >= start]

    for test_log in test_logs:
        log_url = f'https://svn.digipen.edu/projects/leviathan/trunk/TEST_LOGS/{test_log}'
        raw_test = run_cmd(['svn','cat',log_url], raw=True)
        try:
            raw_test.stdout.decode()
        except UnicodeDecodeError:
            pass
        else:
            #successful parsing means that the output wasn't binary
            #it's an error message
            continue 

        #save the file under some random name, then open it
        with open('tempExcel.xlsx', 'wb') as f:
            f.write(raw_test.stdout)
        file_df = pd.read_excel('tempExcel.xlsx')
        
        #get the row, based on the test name column (which is unnamed)
        test_row = file_df.loc[file_df['Unnamed: 0'] == test]

        #check that test is included
        try:
            test_row['result'].iloc[0]
        except IndexError as e:
            #test isn't in here
            continue
        print(f'Revision {test_log[8:12]}:')
        
        test_output = '\n'.join([f'    > {output_row}' for output_row in test_row['output'].iloc[0].split('\n')])
        test_color = 'green' if test_row['result'].iloc[0] == 'Passed' else 'red'
        print('  > RESULT: {}'.format(colored(test_row['result'].iloc[0], test_color)))
        print('  > DURATION: {}'.format(test_row['duration'].iloc[0]))
        print('  > OUTPUT:\n{}'.format(test_output))
        print('----------------------------------------------------')
        
    #delete the excel spreadsheet        
    remove('tempExcel.xlsx')
