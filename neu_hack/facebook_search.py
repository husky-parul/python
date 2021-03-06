import json,time
import urllib

class Events(object):
	description=''
	end_time=''
	name=''
	place=''
	start_time=''
	

class Result(object):
	about=''
	category=''
	des=''
	hours=''
	phone=''
	price=''
	website=''
	checkins=''
	events=Events()
	name=''
	address=''
	image=''
	


class SearchApi(object):
	id_list=[]
	page=0
	access='EAACEdEose0cBACUAb0TCZAk3G766L42j2vWPV2ZCPsZCLygBSHp20Nw6XwsrbEyihQmFZBc5sZCjfog0cMCVVABwZC3U7A2i2FtJhkNUrGKDtZBBc0vXLqrY19LiMS1lLcZAHNbgthL9tBvy9msOe5S8PjZBUNRvW7ZAnO9QB4Rtkod9ZBeZCP1m4NNJ'
	
	def make_request(self):
		latt=42.353904
		long=-71.133711
		data = {}
		data['type'] = 'place'
		data['distance'] = 4000
		data['access_token'] = self.access
		url = "https://graph.facebook.com/v2.8/search"
		url_values = urllib.urlencode(data)
		new_url= url + "?" + url_values+"&center=42.353904%2c-71.133711"
		
		response=urllib.urlopen(new_url)
		result=self.get_data(new_url)
		return self.get_data_for_id()
		
	
		
		
	def get_event_data(self,id):
		event_list=[]
		url = 'https://graph.facebook.com/v2.8/'
		extra=id+'/events?access_token='+self.access
		url=url+extra
		
		response=urllib.urlopen(url)
		result=json.load(response)
		for i in result['data']:
			event=Events()
			st=i.get('start_time', '').split('T')
			print st
			
			td=time.strftime("%Y-%m-%d")
			print td
			if st[0]==td:
				event.description=i.get('description', '')
				event.end_time=i.get('end_time', '')
				event.name=i.get('name', '')
				event.place=i.get('place', '')
				event.start_time=st[0]
				event_list.append(event)
		event_list.sort(key=lambda x: x.start_time, reverse=False)
		
		return event_list
	
		
		
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
		access = self.access
		url = 'https://graph.facebook.com/v2.8/'
		extra='?fields=about,business,category,cover,description,features,hours,phone,price_range,website,checkins,single_line_address,name&access_token='
		for i in self.id_list:
			newurl=url+str(i)+extra+access
			response=urllib.urlopen(newurl)
			result=json.load(response)
			result_obj=self.extract_data(result)
			if result_obj is not None:
				result_obj.events=self.get_event_data(i)
				result_list.append(result_obj)
		result_list.sort(key=lambda x: x.checkins, reverse=True)
		return result_list
		
			
	def extract_data(self,data):
		obj=Result()
		if data.get('category', '') in ["Local Business","Pub","Restaurant"]:
			obj.about=data.get('about', '')
			obj.category=data.get('category', '')
			obj.des=data.get('description', '')
			obj.hours=data.get('hours', '')
			obj.price=data.get('price', '')
			obj.website=data.get('website', '')
			obj.checkins=data.get('checkins', '')
			obj.name=data.get('name', '')
			obj.address=data.get('single_line_address', '')
			l= data.get('cover', [])
			if len(l)!=0:
				obj.image=l['source']
			else:
				obj.image=''
			print '-------: ',obj.name, '--------: ', obj.category
			return obj
		
		
def main():
	obj=SearchApi()
	result_list=obj.make_request()
	print len(result_list)
	
if __name__=='__main__':
	main()
	
