import argparse
from fragalysis_preproc.data import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
                                     "Get apo pdbs and molecule sdfs in csv format for an input target"
                                     " from https://fragalyysis.diamond.ac.uk")
    parser.add_argument('-t', '--target', help='Name of target on Fragalysis')
    parser.add_argument('-o', '--output', help='Output csv file')

    args = parser.parse_args()

    if args.target:
        target = args.target
    else:
        raise Exception('No target input provided - please see help! (--help)')

    if args.output:
        output = args.output
    else:
        raise Exception('No output csv provided - please see help! (--help)')

    search = GetMoleculesData()
    search.get_target_ids(target)
    search.get_all_mol_responses()
    dct = search.convert_mols_to_dict()
    dct.to_csv(output)