---
tags:
  - web
aliases:
  - RSS
---
These are XML files used by RSS feeds to view for changes in:
- News sites
- Blogs
- Podcasts
# Creation
1. `npm i rss`
In your project
2. `mkdir feed.xml`
3. `nvim feed.xml/route.js`
Add this to the route.js:
```xml
import RSS from "rss";
import { metadata } from "../../layout";


// Export the route handler
export async function GET() {
    const feed = new RSS({
        title: metadata.title,
        description: metadata.description,
        site_url: metadata.url,
        feed_url: `${metadata.url}/blog/feed.xml`,
        pubDate: new Date(),
    });

	// some code for each web blog entry
	
    return new Response(feed.xml(), {
        headers: {
            'Content-Type': 'application/atom+xml; charset=utf-8',
        },
    });
}
```