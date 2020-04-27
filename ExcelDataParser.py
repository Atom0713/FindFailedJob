import csv


class ParseData:
    def __init__(self, file_path):
        self.filePath = file_path

    def read_data(self):
        f = open(self.filePath)

        failed = []  # will hold all failed jobs
        other = []  # will hold all, but failed jobs
        for x in f:

            x = x.strip()

            bracket_index = x.find("]")  # Find ending square bracket
            x = x[bracket_index + 1:len(x)-7]  # copy everything after square bracket
            x = x.strip()

            job_name_end_index = x.find(":")  # find the colon
            job_name = x[0:job_name_end_index]  # copy job name that comes before the colon
            job_name = job_name.strip()  # clean white spaces

            x = x[job_name_end_index + 1:len(x)]  # copy everything after the colon
            x = x.strip()  # clean white spaces

            job_status_end_index = x.find(",")  # find comma after the status
            job_status = x[0:job_status_end_index]  # copy job status that comes before the comma

            x = x[job_status_end_index+1:len(x)]  # copy everything after the status comma
            x = x.replace("T", " ")  # replace T with " "(space) that is in the middle of the date

            if x[0] == " ":  # if there is a white space means job has runid, NONE otherwise
                job_runid_index =  x.find(",")  # find the comma after runid
                job_runid = x[0:job_runid_index]  # copy job runid that is before the comma
                job_runid = job_runid.strip()  # clean white spaces
                x = x[job_runid_index+1:len(x)]  # copy everything after the runid comma
                x = x.strip()  # clean white spaces
                job_date = x  # date is all that is left in the line, copy to job_date variable
            else:
                job_runid = "NONE"  # no job runid exists
                x = x.strip()  # clean white spaces
                job_date = x  # date is all that is left in the line, copy to job_date variable

            if job_status.upper() == "FAILED": # if job has failed put into failed[]
                failed.append({'Name': job_name, 'Status': job_status, 'Runid': job_runid, 'Date': job_date})
            else: # put into other[] otherwise
                other.append({'Name': job_name, 'Status': job_status, 'Runid': job_runid, 'Date': job_date})

        f.close()  # close "input.csv" file

        fnames = ['Name', 'Status', 'Runid', 'Date']  # headers for the output csv file. Data send to the file
		
        # will be ordered according to the fnames order!
        with open('failed.csv', 'wb') as failed_jobs:  # create a fill failedjobs file

            writer_failed = csv.DictWriter(failed_jobs, fieldnames=fnames, delimiter=',')  # creates file with order
			
            # given by fnames and a data separator (the delimiter -- can be whatever you want)
            writer_failed.writeheader()  # writes headers
            writer_failed.writerows(failed)  # writes the data

        with open('other.csv', 'wb') as other_jobs:  # create and fill other than failed jobs file

            writer_other = csv.DictWriter(other_jobs, fieldnames=fnames, delimiter=',')   # creates file with order
			
            # given by fnames and a data separator (the delimiter -- can be whatever you want)
            writer_other.writeheader()  # writes headers
            writer_other.writerows(other)  # writes headers


p1 = ParseData("test_data.csv")   # create ParseData class object, calling the constructor of the class and pass the file path

p1.read_data()  # call the read_data() function from ParseData object
