# FearGreedIndexHunter

## About

This script will get the fear & greed index value from cnn website, make the plot and send to your email inbox if it is set up correctly

## Set up

After copying the code, make sure you do the following before running the script:

- Install these packages if you don't have them yet
    - bs4
    - urllib
    - re
    - datetime
    - matplotlib
    - pandas
    - smtplib
    - email

- Change the variables below in the script
    - fear_greed_index_dir
    - png_dir
    - sender_email
    - sender_password
    - recipient_email
    - email_server_addr
    - email_server_port

- Use the task scheduler to automate daily script run


## Future Steps

1. Generate monthly plot

2. Put it on the server if there are people interested in receiving the chart every day
