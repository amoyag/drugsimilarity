
import subprocess

def shellmysql(list):
    for a in list:
        # a = """ + str(a) + """
        subprocess.call(["/Users/aurelio/sandbox/drugDomain_map/drugsimilarity/getsdf2.sh", a])
        