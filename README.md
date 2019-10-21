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

---

### What I'm currently working on:
#### Researching Server-Side Rendering

In order for me to benefit fully from running a blog on my website, I'm going to need to implement some sort of static content strategy for SEO purposes. Since React.js is rendered on the client, it will require some extra care to work as intended.

---

### My future plans:
#### Add blog to my website

React.js isn't particularly great for this due to SEO reasons, however, I hope to mitigate a lot of the problem by implementing server-side rendering of those components.
