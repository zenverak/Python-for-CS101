def get_next_target(thing):
	start_link=page.find("<a href=")
	if start_link == -1:
		return None, 0
	start_quote=page.find('"', start_link)
	end_quote=page.find('"',start_quote + 1)
	url = page[start_quote +1:end_quote]
	return url, end_quote
def get_all_links(page):
	links=[]
	while True:
		url,endpos = get_next_target(page)
		if url:
			links.append(url)
			page= page[endpos:]
		else:
			break
	return links
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
def crawl_web(seed,max_depth):
	tocrawl = [seed]
	crawled = []
	next_depth=[]
	index=[]
	depth = 0
	while tocrawl and depth<=max_depth:
		page =  tocrawl.pop()
		if page not in crawled:
			stuff = get_page(page)
			add_page_to_index(index, page, stuff)
			union(next_depth,get_all_links(content))
			crawled.append(page)
		if not tocrawl:
			tocrawl = next_depth
			next_depth = []
			depth += 1
	return index		


def add_to_index(index,keyword,url):
    for ent in index:
        if ent[0]==keyword:
            ent[1].append(url)
            return
    index.append([keyword,[url]])
    return 
def lookup(index,keyword):
    for e in index:
        if e[0]==keyword:
            return e[1]
    return [] 
def add_page_to_index(index,url,content):
    content = content.split()
    for words in content:
        add_to_index(index,words, url)	
 #unless I missed it, this was never actually defined in course
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""