from datetime import datetime
def write_time(path):
  current_time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #datetime module from python found on google
  with open(path,'a') as file:
    file.write(current_time_str)
write_time('/repo/version-control/docs/version.md')
