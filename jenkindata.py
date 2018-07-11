import jenkinsapi
from jenkinsapi.jenkins import Jenkins
import logging
from datetime import datetime
import mysql.connector


class jenkinsjobstatus(object):
    """
    Automated script to extract the data from jenkins and upload the data in mysql database 
     
    """

    def jenkins_nxte_job(self):
        """
        Collect jenkins job status,date time,build number by using jenkins api and store it in the result.text file

        """
        logger.info('_init_jenkins_api')

        J = Jenkins('Give the jenkins website name')
        jenkins_job_name=['JOB1','JOB2','JOB3','JOB4','JOB5','JOB6',]
    
        for jobname in jenkins_job_name:
	    job = J[jobname]

            try:
	        lastbuild = job.get_last_completed_build()
            except Exception as e:
                print "lastbuild does not contain any value:", e
    
            lastbuild_data=str(lastbuild).split("#")

            try:	    
	        date_time=lastbuild.get_timestamp()
            except Exception as e:
                print "date_time does not contain any value:",e

            try:
                status=lastbuild.get_status()
            except Exception as e:
                print "status does not contain any value:",e

            finally:
	    	strdate=str(date_time)	    	    	        	    
	    	text_file=open("result.txt", "a")
	    	text_file.write(lastbuild_data[0]+" "+lastbuild_data[1]+ " " +status + "  " +strdate)
	    	text_file.write("\n")
            

    def insertdata(self):
        """
        Insert data to mysql database from the result.txt file

        """   
        for line in open("result.txt"):
            cnx=mysql.connector.connect(user='root', password='root',host='localhost',database='firstdatabase')
            line=format(line.rstrip())
            line_data=line.split()
            cursor=cnx.cursor()
            test=line_data[3]+ " "+ line_data[4]
            new_dt=test[:19]
            dt = datetime.strptime(new_dt,'%Y-%m-%d %H:%M:%S')

            if(line_data[0]=='JOB1'):
                logger.info('_inserting_JOB1_to_mysql')
                cursor.execute('SELECT COUNT(*) from buildstatus_jenkinsjobsinformation WHERE build = "%s"' % (line_data[1]))
                results=cursor.fetchone()        
                if(results[0]<1):
                    cursor.execute('INSERT INTO buildstatus_jenkinsjobsinformation(id,build,date,jobinformation_id,Sanity,Smoke,Status,System,JIRA_closed,JIRA_open,Releasecandidate) VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',\
                                                                                                                                            (line_data[1],dt,1,'SUCCESS','SUCCESS',line_data[2],'SUCCESS','NULL','NULL','YES'))
                    cnx.commit()

            elif(line_data[0]=='JOB2'):
                logger.info('_inserting_JOB2_to_mysql')
                cursor.execute('SELECT COUNT(*) from buildstatus_jenkinsjobsinformation WHERE build = "%s"' % (line_data[1]))
                results=cursor.fetchone()
                if(results[0]<1):
                    cursor.execute('INSERT INTO buildstatus_jenkinsjobsinformation(id,build,date,jobinformation_id,Sanity,Smoke,Status,System,JIRA_closed,JIRA_open,Releasecandidate) VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',\
                                                                                                                                            (line_data[1],dt,2,'SUCCESS','SUCCESS',line_data[2],'SUCCESS','NULL','NULL','YES'))
                    cnx.commit()

            elif(line_data[0]=='JOB3'):
                logger.info('_inserting_JOB3_to_mysql')
                cursor.execute('SELECT COUNT(*) from buildstatus_jenkinsjobsinformation WHERE build = "%s"' % (line_data[1]))
                results=cursor.fetchone()
                if(results[0]<1):
                    cursor.execute('INSERT INTO buildstatus_jenkinsjobsinformation(id,build,date,jobinformation_id,Sanity,Smoke,Status,System,JIRA_closed,JIRA_open,Releasecandidate) VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',\
                                                                                                                                            (line_data[1],dt,3,'SUCCESS','SUCCESS',line_data[2],'SUCCESS','NULL','NULL','YES'))
                    cnx.commit()

            elif(line_data[0]=='JOB4'):
                logger.info('_inserting_JOB4_to_mysql')
                cursor.execute('SELECT COUNT(*) from buildstatus_jenkinsjobsinformation WHERE build = "%s"' % (line_data[1]))
                results=cursor.fetchone()
                if(results[0]<1):
                    cursor.execute('INSERT INTO buildstatus_jenkinsjobsinformation(id,build,date,jobinformation_id,Sanity,Smoke,Status,System,JIRA_closed,JIRA_open,Releasecandidate) VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',\
                                                                                                                                            (line_data[1],dt,4,'SUCCESS','SUCCESS',line_data[2],'SUCCESS','NULL','NULL','YES'))
                    cnx.commit()

            elif(line_data[0]=='JOB5'):
                logger.info('_inserting_JOB5_to_mysql')
                cursor.execute('SELECT COUNT(*) from buildstatus_jenkinsjobsinformation WHERE build = "%s"' % (line_data[1]))
                results=cursor.fetchone()
                if(results[0]<1):
                    cursor.execute('INSERT INTO buildstatus_jenkinsjobsinformation(id,build,date,jobinformation_id,Sanity,Smoke,Status,System,JIRA_closed,JIRA_open,Releasecandidate) VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',\
                                                                                                                                            (line_data[1],dt,5,'SUCCESS','SUCCESS',line_data[2],'SUCCESS','NULL','NULL','YES'))
                    cnx.commit()

if __name__== "__main__":
    logging.basicConfig(level=logging.INFO)
    logger=logging.getLogger(__name__)
    jenkinstatus=jenkinsjobstatus()
    jenkinstatus.jenkins_nxte_job()
    jenkinstatus.insertdata()







