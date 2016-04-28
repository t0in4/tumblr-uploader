#!/usr/bin/python

import pytumblr
import os
import time

client = pytumblr.TumblrRestClient(
    '',
      '',
      '',
      ''
)#write above secrets codes 
while True:
    path1='/home/uploads/pics'
    for filename in os.listdir(path1):
        filename = os.path.join(path1,filename)
        client.create_photo('<sitename>', state="queue",
                             tags=["#<tag_1>", "#<tag_2", "#tag_3"],
                             tweet="<some_moto>",
                              data=filename)

        time.sleep(5)
else:
    print "The loop is over."
print "Done"
