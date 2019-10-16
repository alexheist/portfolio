Personal Portfolio
==================

### What I've accomplished so far:
#### Implement CSS Grid for styling

In the past, I have used Bootstrap as my go-to CSS framework. However, I have since felt as though I'm often fighting with Bootstrap more than it helps me. I have used other CSS frameworks (particularly SemanticUI), but I found that writing my own CSS feels much cleaner, and I can accomplish exactly what I want with little to no friction.

#### Dockerize my deployment & configure hosting

This portfolio was initially created just so that I can familiarize myself more with Docker and the deployment process in general. I manage my own VPS running CentOS 7, and serve my website via Nginx.

#### De-couple the frontend from the backend

Initially, I was using Django's templating engine to handle HTML (Tag 1.0.0 & 1.0.1). This worked fine, but I wanted to learn how to use React.js, so I restructured the entire project to use React.js in the frontend and set up a Django Rest Framework API on the backend. I accomplished this utilizing `docker-compose` to orchestrate the containers.

---

### What I'm currently working on:
#### Adding SSL to my server

This is something that I have working on my development machine, but have been running into issues with using `certbot` to generate the SSL certificates on my server. This is due to some package conflicts between `yum` and `pip`, and is something I intend to have resolved soon.

---

### My future plans:
#### Add blog to my website

React.js isn't particularly great for this due to SEO reasons, however, I hope to mitigate a lot of the problem by implementing server-side rendering of those components.
