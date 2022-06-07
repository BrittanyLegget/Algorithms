import argparse
from bottomUp import lcs_bottomup
from topDown import lcs_topdown_helper

# Default testing input Strings
charString1 = ['A', 'T', 'A', 'G', 'T', 'T',
               'C', 'C', 'G', 'T', 'C', 'A', 'A', 'A']
charString2 = ['G', 'T', 'G', 'T', 'T', 'C',
               'C', 'C', 'G', 'T', 'C', 'A', 'A', 'A']

CLI = argparse.ArgumentParser()
CLI.add_argument(
    "--list1",
    nargs="*",
    type=str,
    default=charString1,  # default if nothing is provided
)
CLI.add_argument(
    "--list2",
    nargs="*",
    type=str,
    default=charString2,
)

args = CLI.parse_args()
charList1 = args.list1
charList2 = args.list2

print('Bottom-up Length of longest common subsequence: ',
      lcs_bottomup(charList1, charList2))
print("Top-Down Length of longest common subsequence:",
      lcs_topdown_helper(charList1, charList2))
