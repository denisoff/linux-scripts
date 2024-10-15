# automation script for taking tasks to work for jira
from jira import JIRA 
login = ""
api_key = ""
jira_options = {'server': ''}
jira = JIRA(options=jira_options, basic_auth=(login, api_key))
issues = jira.search_issues('status="" AND assignee = currentUser()') # find all user tasks with the desired status
for issues_work in issues:
    jira.transition_issue(issues_work, transition='') # take tasks to work
    print(issues_work)