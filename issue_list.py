import csv
from collections import defaultdict

users = set()
team_issues = defaultdict(list)

# Process CSV file and store users, and issues per team 
with open('issues.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Users is a set so dupes are eliminated
        users.add(row['ASSIGNEE'])
        team_issues[row['TEAM']].append(row['ISSUE'])

# Print "To" list
print "To:",
for user in users:
    user_email = "%s@atlassian.com," % user
    print user_email,

print "\nSubject: Mission control bug report"

# Print issues per team
for team in team_issues.keys():
    print "\n%s has %s open issues" % (team.capitalize(), len(team_issues[team]))
    for issue in team_issues[team]:
        print " %s" % issue
