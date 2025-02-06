from datetime import datetime
now = datetime.now()
current_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
with open(path,'a') as file:
  file.write(current_time_str)

print('/repo/version-control/docs/version.md') #datetime module from python found on google
