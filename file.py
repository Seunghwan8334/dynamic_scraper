import csv

def save_to_file(file_name, jobs):

    file_name = file_name+"_jobs.csv"
    file = open(file_name,"w", encoding="utf-8")
    writer = csv.writer(file)

    writer.writerow(["Title","Company","Reward","Link"])

    for job in jobs:
        writer.writerow(job.values())
    file.close()