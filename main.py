from rfeed import *
import datetime


feed = Feed(
    title="nixCraft Updated Tutorials/Posts",
    link="https://www.cyberciti.biz/atom/updated.xml",
    description="nixCraft Linux and Unix Sysadmin Blog - Recently updated posts",
    language="en-US",
    lastBuildDate=datetime.datetime.now())

print(feed.rss())
