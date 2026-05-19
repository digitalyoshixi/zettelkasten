---
tags:
  - database
aliases:
  - Schema Definition Language
  - SDL
---
```
type Creator{
	id : ID!
	name : String
	subscribers : Int
	videos : [Video]
}

type Video {
	url : String!
	creator : Creator
}

type Query {
	videos : [Video]
	creator(id: String!): Creator
}
type Mutation{
	createVideo(url: String): Video
	deleteVideo(url: String): String
}
```