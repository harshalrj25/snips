import os
import csv

# path format is for windows
path = 'D:\\foldername\\subfoldername'
  
# if you are on using macOS uncomment and use below path format, and comment out the above one
#path = '/Users/iosdev1/youtube/exportFilePath/dummyData'

with open('YOUR_OUTPUT_FILE_xlsx.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)
  for root, dirs, files in os.walk(path):
    for filename in files:
        fname, file_extension = os.path.splitext(os.path.join(root,filename))
        writer.writerow([(os.path.splitext(filename)[0]), file_extension, os.path.join(root,filename)])
