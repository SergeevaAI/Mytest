from git import Repo
import os
os.chdir('/home/sergeeva/SergeevaAI.github.io')
PATH_OF_GIT_REPO = r'/home/sergeeva/SergeevaAI.github.io/.git'
COMMIT_MESSAGE = 'daily update'

def git_push():
  repo = Repo(PATH_OF_GIT_REPO)
  repo.git.add('--all')
  repo.index.commit(COMMIT_MESSAGE)
  origin = repo.remote(name='origin')
  origin.push()
git_push()


