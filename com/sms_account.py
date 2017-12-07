import requests

class SmsAccount():
  main_auth_id = 'MAODUZYTQ0Y2FMYJBLOW'
  main_auth_token = 'Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1'
  sub_auth_id = 'SANMEWYTRJOGMWZWQ1ZT'
  sub_auth_token = 'MjI2YmZhYTQzMzBiYjlmY2FjYzc4ZGU4YzJlZDVi'
  url = 'https://api.plivo.com/v1/Account/'


  """ For retrieving the data related to main account """
  
  def get_account_details(self):
    response = requests.get(self.url+self.main_auth_id, auth = (self.main_auth_id, self.main_auth_token))
    return(response.json())


  """ For retrieving the data related to Sub account """

  def get_subaccount_details(self):
    response = requests.get(self.url+self.main_auth_id+'/Subaccount/'+self.sub_auth_id, auth = (self.main_auth_id, self.main_auth_token))
    return(response.json())


  """ For sending message from souce number to destination """

  def sms_send(self, fromMobile, toMobile, message):
    src, dst, text = fromMobile, toMobile, message
    response = requests.post(self.url+self.main_auth_id+'/Message/', auth = (self.main_auth_id, self.main_auth_token), json = {'src':src, 'dst':dst, 'text':text})
    return(response.json())


  """ For getting the price chart """

  def sms_price(self, country):
     response = requests.get(self.url+self.main_auth_id+'/Pricing/', auth = (self.main_auth_id, self.main_auth_token), params = {'country_iso' : country} )
     return (response.json())


  """ For getting message details """

  def sms_details(self, uuid):
     response = requests.get(self.url+self.main_auth_id+'/Message/'+uuid, auth = (self.main_auth_id, self.main_auth_token))
     return (response.json())
