# colonial-invoices
use python selenium to download colonial invoices

This is for insurance agencies or other companies who have multiple Colonial Life accounts.  The program automates saving monthly invoices for clients.

You will need to update the dictionary with BCNs--used to look up the client on the billing portal--and short names to be included in the file names.

The program asks for user name and password from the user each time rather than saving that information for security reasons, but you can change that if you'd like.

The network at work is very tightly secured, so I can't save directly to the client directories.  
Instead, I'm saving to Downloads and moving manually--a bit of a pain but I'm still saving hours over a fully manual process.
You'll need to update the downloads folder name in the code with your user name, and you can experiment with saving the invoices elsewhere if you'd like.
I'm also not able to rename the saved invoices from the generic name the broser gives them due to security settings, so I make a copy with the proper name instead and delete the others at the end of the process.

If you are new to Python, after installing Python you have to open Windows Powershell and install each package you're using one time.
So you'd type "pip install selenium" without the quotes and hit Enter, and go through the list of packages at the beginning.

v2 8-18-2020:  I extended the sleep time between steps because it timed out several times when I ran it at the end of July.  I updated the code for scheduled payments, although I was interrupted before I could test it so it may still not work.  And I updated the naming convention - invoices are generated around the 26th and due around the 13th, and I had planned to pull them around the 1st so I was using the current month to name the files.  However, I was asked to pull them as soon as they are available, so I used the month for the date 2 weeks from the current date, which should get the correct date regardless of whether you run the code at the end of the month or the beginning of the next.
