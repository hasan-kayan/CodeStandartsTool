import jenkins

# Connect to Jenkins server
def connect_to_jenkins_server(jenkins_url, jenkins_user, jenkins_password):
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_password)
    return server

# Get Jenkins job details
def get_jenkins_job_details(server, job_name):
    job_details = server.get_job_info(job_name)
    return job_details

# Get Jenkins job build details
def get_jenkins_job_build_details(server, job_name, build_number):
    build_details = server.get_build_info(job_name, build_number)
    return build_details

# Get Jenkins job last build number
def get_jenkins_job_last_build_number(server, job_name):
    last_build_number = server.get_job_info(job_name)['lastBuild']['number']
    return last_build_number

## if main 
if __name__ == "__main__":
