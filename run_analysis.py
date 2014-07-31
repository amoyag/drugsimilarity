


import numpy
import map2dict
import bipartg
import fingerprints



###
# This chunk is unnecessary as the mysql query is performed by a shell script to chembl_19
####

# if __name__ == '__main__':
#     import sys
#
#     if len(sys.argv) < 5:  # the program name and the two arguments
#
#         sys.exit("Must specify release, user, pword, host, port")
#
#
#     release = sys.argv[1]
#     user = sys.argv[2]
#     pword = sys.argv[3]
#     host = sys.argv[4]
#     port = int(sys.argv[5])


comp_target = map2dict.map2dict('../mapChEMBLPfam/data/map_pfam.txt')
edges = bipartg.bipartg(comp_target)

fingerprints.fingerp(edges)

