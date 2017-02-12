import json
import urllib

class Result(object):
	about=''
	category=''
	des=''
	hours=''
	phone=''
	price=''
	website=''

class SearchApi(object):
	id_list=[]
	page=0
	
	def make_request(self):
		latt=42.353904
		long=-71.133711
		
		data = {}
		data['type'] = 'place'
		data['distance'] = 4000
		data['access_token'] = 'EAACEdEose0cBAGn0mKHlLbM3KuqDx8p3PGdK8EAhNeCood7Ib05fv5Rk2Fa5UeE6QZAcyDmIRW1mj3lZBaISDP2tLLkhel3LpkTlzVuDuOgKwhchZAd50hxZCUD72wWzvj85YNlDoFWzalVnFLl0629770tIyZCi9iqjZCLZCLOnvqlE8XPZChkw'
		url = "https://graph.facebook.com/v2.8/search"
		url_values = urllib.urlencode(data)
		new_url= url + "?" + url_values+"&center=42.353904%2c-71.133711"
		response=urllib.urlopen(new_url)
		result=self.get_data(new_url)
		return self.get_data_for_id()
		
		
	def get_data(self,url):
		response=urllib.urlopen(url)
		result=json.load(response)
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
		result_list=[]
		access = 'EAACEdEose0cBAGn0mKHlLbM3KuqDx8p3PGdK8EAhNeCood7Ib05fv5Rk2Fa5UeE6QZAcyDmIRW1mj3lZBaISDP2tLLkhel3LpkTlzVuDuOgKwhchZAd50hxZCUD72wWzvj85YNlDoFWzalVnFLl0629770tIyZCi9iqjZCLZCLOnvqlE8XPZChkw'
		url = 'https://graph.facebook.com/v2.8/'
		extra='?fields=about,business,category,description,features,hours,phone,price_range,website&access_token='
		for i in self.id_list:
			newurl=url+str(i)+extra+access
			response=urllib.urlopen(newurl)
			result=json.load(response)
			result_list.append(self.extract_data(result))
		return result_list
		
			
	def extract_data(self,data):
		obj=Result()
		obj.about=data.get('about', [])
		obj.category=data.get('category', [])
		obj.des=data.get('des', [])
		obj.hours=data.get('hours', [])
		obj.price=data.get('price', [])
		obj.website=data.get('website', [])
		return obj
		
		
def main():
	obj=SearchApi()
	result_list=obj.make_request()
	print len(result_list)
	
if __name__=='__main__':
	main()
	
