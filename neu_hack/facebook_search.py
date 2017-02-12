import json
import urllib

class SearchApi(object):
	id_list=[]
	page=0
	
	def make_request(self):
		latt=42.353904
		long=-71.133711
		dist=4000
		data = {}
		data['type'] = 'place'
		data['distance'] = dist
		data['access_token'] = 'EAACEdEose0cBAMiwNJ2cAyGTsNBOK5KERHzj9cdD1mnjK4DcuY8LWOKqiirtYrwXcvHZCeArO7ZAMSiZAjMofIBFdGeMas9lbHlH65Pap2kqnR5VVEM8qkZBKlcZAowZCVFIt016ZBXwkqWSzOWZC3XKO2A5pwyX2lW9M8qHsa2fhtZBiXzB6TNxO'
		url = "https://graph.facebook.com/v2.8/search"
		url_values = urllib.urlencode(data)
		new_url= url + "?" + url_values+"&center=42.353904%2c-71.133711"
		response=urllib.urlopen(new_url)
		result=self.get_data(new_url)
		print len(self.id_list)
		print self.id_list
		self.get_data_for_id()
		
		
	def get_data(self,url):
		print url
		response=urllib.urlopen(url)
		result=json.load(response)
		print '_____________result: ',result
		for i in result['data']:
			self.id_list.append(i['id'])
		if 'paging' in result:
			p=result['paging']
			after= p['cursors']['after']
			if '&after' not in url:
				url=url+'&after='+after
				self.get_data(url)
				self.page+=1
			else:
				head, sep, tail = url.rpartition('&after=')
				if head is not None:
					self.page+=1
					if self.page!=10:
						url=head + '&after='+after
    					self.get_data(url)
		else:
			return

	def get_data_for_id(self):
		data={}
		access = 'EAACEdEose0cBAMiwNJ2cAyGTsNBOK5KERHzj9cdD1mnjK4DcuY8LWOKqiirtYrwXcvHZCeArO7ZAMSiZAjMofIBFdGeMas9lbHlH65Pap2kqnR5VVEM8qkZBKlcZAowZCVFIt016ZBXwkqWSzOWZC3XKO2A5pwyX2lW9M8qHsa2fhtZBiXzB6TNxO'
		url = 'https://graph.facebook.com/v2.8/'
		extra='?fields=about,business,category,description,features,hours,phone,price_range,website&access_token='
		
		for i in self.id_list:
			newurl=url+str(i)+extra+access
			
			print 'url: ',newurl
			response=urllib.urlopen(newurl)
			result=json.load(response)
			print '_____________result: ',result
			
		
		
def main():
	print 'inside main'
	obj=SearchApi()
	obj.make_request()
	
if __name__=='__main__':
	main()
	
