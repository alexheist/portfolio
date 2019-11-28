Personal Portfolio
==================

### What I've accomplished so far:
#### Implement CSS Grid for styling

In the past, I have used Bootstrap as my go-to CSS framework. However, I have since felt as though I'm often fighting with Bootstrap more than it helps me. I have used other CSS frameworks (particularly SemanticUI), but I found that writing my own CSS feels much cleaner, and I can accomplish exactly what I want with little to no friction.

#### Dockerize my deployment & configure hosting

This portfolio was initially created just so that I can familiarize myself more with Docker and the deployment process in general. I manage my own VPS running CentOS 7, and serve my website via Nginx.

#### De-couple the frontend from the backend

Initially, I was using Django's templating engine to handle HTML (Tag 1.0.0 & 1.0.1). This worked fine, but I wanted to learn how to use React.js, so I restructured the entire project to use React.js in the frontend and set up a Django Rest Framework API on the backend. I accomplished this utilizing `docker-compose` to orchestrate the containers.

#### Adding SSL to my configuration

I have configured a working local version of https for testing purposes, and have implemented CertBot to generate SSL certificates on my server.

#### Add Blog

I have added a new set of endpoints for the API for the soon-to-be-released blog, as well as new React components. There is a `/blog` URL that will retrieve a list of published articles, in addition to `/blog/:slug` URL for displaying a specific article.

---

### What I'm currently working on:
TBD

---

### My future plans:
#### Implement Prerender.io on server

React.js isn't particularly great for this due to SEO reasons, however, I hope to mitigate a lot of the problem by implementing prerender.io.
