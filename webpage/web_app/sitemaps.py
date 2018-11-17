from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from web_app.models import Course_page,College_detail

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
    	# name = Course_page.objects.filter().values('slug')
    	# nlist = list()
    	# for x in name:
    	# 	nlist.append("course/" + x['slug'])
    	return ['about']

    def location(self, item):

    	return reverse(item)



class SnippetSitemap(Sitemap):
	priority = 0.5
	changefreq = 'daily'

	def items(self):

		# name = Course_page.objects.filter().values('slug')
		
		# nlist = list()
		# for x in name:
		# 	nlist.append(x['slug']) 
		# print(nlist)
		return (Course_page.objects.all())

class CollegeSitemap(Sitemap):

	priority = 0.5
	changefreq = 'daily'

	def items(self):

		return College_detail.objects.all()




		

