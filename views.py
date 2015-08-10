from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render
import operator
import random
from article_db.models import *
from datetime import datetime

#Provide the absolute path of templates to TEMPLATES.DIRS in settings.py in case template loading fails
total_article=5		

def replace_newline_to_br(str):
	new_content=''
	for c in str:
		if(c=='\n'):
			new_content+='</br></br>'
		new_content+=c
	return(new_content)


def trim_content(str,para):
	trimmed_content=''
	count=0
	for c in str:
		if(c=='\n'):
			trimmed_content+='</br></br>'
			count+=1
			if(count==para):
				break
		trimmed_content+=c
	return trimmed_content


def get_trimmed_data(i,para):
	temp = {'id':i,'title':Article.objects.get(id=i).title,'author':Article.objects.get(id=i).author,
			'pub_date':datetime.strptime(Article.objects.get(id=i).pub_date, '%Y-%m-%d'),'category':Article.objects.get(id=i).category,
			'hero_image':Article.objects.get(id=i).hero_image,'opt_image':Article.objects.get(id=i).opt_image,
			}
	temp['content'] = trim_content(Article.objects.get(id=i).content,para)
	return temp

def get_data(i):
	temp = {'id':i,'title':Article.objects.get(id=i).title,'author':Article.objects.get(id=i).author,
			'pub_date':datetime.strptime(Article.objects.get(id=i).pub_date, '%Y-%m-%d'),'category':Article.objects.get(id=i).category,
			'hero_image':Article.objects.get(id=i).hero_image,'opt_image':Article.objects.get(id=i).opt_image,
			}
	temp['content'] = replace_newline_to_br(Article.objects.get(id=i).content)
	return temp


def display_homepage(request):
	articles = Article.objects.all()
	
	#a1 = get_trimmed_data(1,1)
	#a2 = get_trimmed_data(2,1)
	#a3 = get_trimmed_data(3,1)
	#a4 = get_trimmed_data(4,1)
	#a5 = get_trimmed_data(5,1)
	id_list = []
	a_list = []
	#id_list=[1,2,3,4,5]
	#random_id = random.choice(id_list)
	article_list = Article.objects.all()
	for a in article_list:
		id_list.append(a.id)
		a_list.append(get_trimmed_data(a.id,1))

	random_id = random.choice(id_list)
	#article_list = [a4,a2,a3,a1,a5]
	random_article = get_trimmed_data(random_id,2)
	a_list.sort(key=operator.itemgetter('pub_date'))		#article's list gets sorted according to published date
	t = get_template('homepage.html')
	html = t.render(Context({'article': random_article, 'article_list':a_list}))
	return HttpResponse(html)

def display_article(request, id):
	article=get_data(id)
	t = get_template('content.html')
	html = t.render(Context({'article':article}))
	return HttpResponse(html)
	