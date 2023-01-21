### self
Experimental repository to test out efficiency of 
using a version control system for self improvement.  

#### Idea
Define a yaml file with weekly goals using the following template:
```yaml
# self v0.4.0
# status memo
# * --> task complete
# @ --> current task
# _ --> task incomplete
#       used for tasks with planned days
# ^ --> task skipped, but marked complete
#       for example skip task on vacation,
#       or completed on the day different from the plan
Exercise:
  - name: "Gym"
    time:
      - "Monday"
      - "Tuesday"
      - "Thursday"
      - "Friday"
    status: "_**_"

Education:
  - name: "Reading"
    time: 7
    status: "_******"

  - name: "Python"
    time: 2
    details: ">= 1h"
    status: "^*"
```
If the plan above will be completed 2 weeks straight (or any other subjective time period), 
then the version can be upgraded from v0.4.0 to v0.4.1 and settings can be tweaked a little.  

The completion rate can  be verified with `reader.py`:
```bash
# install dependencies
python -m venv venv
source venv/bin/activate
python -m install pip --upgrade
python -m install -r requirements.txt

# run script
python reader.py
```

When the goals are reached, just push a new version (tag) to the repository, 
clear the configuration file and do it all again!
To push a tag:
```bash
git tag -a v0.1.1 -m 'brief description of an upgrade'
git push origin v0.1.1
```
