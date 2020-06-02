import os
import csv

path = '/Users/iosdev1/youtube/exportFilePath/dummyData'

with open('YOUR_OUTPUT_FILE_xlsx.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile)
  for root, dirs, files in os.walk(path):
    for filename in files:
        fname, file_extension = os.path.splitext(os.path.join(root,filename))
        writer.writerow([(os.path.splitext(filename)[0]), file_extension, os.path.join(root,filename)])
