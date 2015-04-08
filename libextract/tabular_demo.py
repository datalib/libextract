'''THIS IS A DEMO, EXPECT TO DELETE IT.
In this file, there's really only one structure that
is key. It's named "path_children" on line 3. There's
further filtering being done using a threshold of
2 std. dev.'s away from the mean, but this is not
necessary.
'''
#!/usr/bin/env python

import lxml.html
from collections import Counter

def meanstd(x):
    """Calculate mean and standard deviation of data x[]:
    mean = {\sum_i x_i \over n}
    std = sqrt(\sum_i (x_i - mean)^2 \over n-1)
    """
    from math import sqrt
    n, mean, std = len(x), 0, 0
    for a in x:
	mean = mean + a
    mean = mean / float(n)
    for a in x:
	std = std + (a - mean)**2
    std = sqrt(std / float(n-1))
    return mean, std

def run():
    url = 'http://www.reddit.com'
    parsed_html = lxml.html.parse(url)
    parsed_body = parsed_html.xpath('//body')[0]
    xpathfinder = parsed_html.getroot().getroottree().getpath


    #######################################################
    # THIS STRUCTURE IS VITAL!
    # path_children is a dictionary with parent node
    # and the counts of occuring children tags
    path_children = {xpathfinder(elem):Counter([e.tag for e in
						elem.xpath('./*')])
		     for elem in parsed_body.xpath(".//*") if len(elem.xpath('./*')) > 0}
    #childrentagset = set([kee for kee,vee in v.iteritems() for k,v in path_children.iteritems()])

    #find topbar on reddit
    topbar_xpath = '//*[@id="sr-bar"]'
    reddit_topbar = parsed_body.xpath(topbar_xpath)[0]
    print path_children[xpathfinder(reddit_topbar)]
    #find id:siteTable - otherwords the main body with stories
    topstories_xpath = '//*[@id="siteTable"]'
    reddit_topstories = parsed_body.xpath(topstories_xpath)[0]
    print path_children[xpathfinder(reddit_topstories)]

    ##################################################################
    #find li children elements
    li_frequency = {k:v['li'] for k,v in path_children.iteritems() if v.has_key('li')}

    #find average <li> child occurrence
    mean,stddev = meanstdv(li_frequency.values())

    #high pass filter pruning out parent nodes whose li child count don't
    #meet the mean + 2*stddev threshold (or should it be like 2.3 stddev's
    #or something like that?
    highpass1_li = {k:v for k,v in li_frequency.iteritems() if v > (mean+2*stddev)}

    #well what do ya know? it points to reddit's topbar
    print highpass1_li.items()

    ##################################################################
    #find div children elements
    div_frequency = {k:v['div'] for k,v in path_children.iteritems() if v.has_key('div')}

    #find average <div> child occurrence
    mean,stddev = meanstdv(div_frequency.values())

    #high pass filter pruning out parent nodes whose div child count don't
    #meet the mean + 2*stddev threshold (or should it be like 2.3 stddev's
    #or something like that?
    highpass1_div = {k:v for k,v in div_frequency.iteritems() if v > (mean+2*stddev)}

    print highpass1_div.items()


if __name__ == '__main__':
    run()
