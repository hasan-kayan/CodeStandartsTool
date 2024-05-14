import git

def git_connector (dynamic_path):
    repo = git.Repo(dynamic_path)
    return repo.git.status()



if __name__ == '__main__':
 git_connector()