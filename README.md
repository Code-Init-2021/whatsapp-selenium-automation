# Whatsapp-selenium-automation
<br>

## Steps to use:
<br>
1. Add a source.csv file containing the rows in  `phno, msg`  format.<br>
2. Run python testautomate.py<br>
3. Scan whatsapp barcode<br>
4. Wait for the script to send the message to each of the number<br>
<br><br>

## FAQ:
1. Does this need the scan part for sure?<br>
Yea
<br><br>
2. Can it send to unsaved numbers?<br>
No, since whatsapp discontinued that feature via whatsapp web. You can save the contacts using contacts.google.com then sync whatsapp contacts and send the messages but do it at your own risk since this project is in no way related to the google contacts feature.
<br><br>
3. If condition in the looping?<br>
Well, the intended purpose required that simultaneous cells having messages that needs to be formatted and sent to a single number and for that matter, the feature is set. Feel free to play around and change that part.
<br><br>
4. How to add head and foot?<br>
The first row in the sheet needs to be  `head, foot`  before extracting to csv.<br>
<br><br>
Enjoy the script and raise any issues if you find any bug or improvement for the automation
