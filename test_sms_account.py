from com.sms_account import SmsAccount
from time import  sleep

sms = SmsAccount()

""" Amount before sending message """
cash_credit = float(sms.get_account_details()["cash_credits"])
print "Cash credit of main account before sending the message : ", cash_credit

""" Sending message and receiving the details of message """
src, dst, text = '+13238318440', '+13252210570', 'Hello World'
sentSms = sms.sms_send(src, dst, text)
messageId = (sentSms['message_uuid'][0]).encode('utf-8')

""" Message status check """
messageDetails = sms.sms_details(messageId)
smsStatus = (messageDetails['message_state']).encode('utf-8')
i = 0
while i<20 and smsStatus != 'sent':
    smsStatus = sms.sms_details(messageId)['message_state'].encode('utf-8')
    i = i+1
    sleep(1)
if(i == 100):
    print "Message not sent"
else:
    print "Message ("+text+") sent sucessfully from mobile number "+src+" to "+dst

""" Getting price list """
country = 'US'
price_list = sms.sms_price(country)
smsCost = float(price_list['message']['outbound']['rate'])
print "Cost of one sms : ", smsCost
if( smsCost == float(messageDetails['total_rate'])):
    print "Amount deducted according to price chart"
else:
    print "Amount not deducted according to price chart"

cash_credit = float(sms.get_account_details()["cash_credits"])
print "Cash credit of main account after sending the message : ", cash_credit

