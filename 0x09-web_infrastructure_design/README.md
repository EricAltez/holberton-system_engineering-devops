<img src="https://blog.holbertonschool.com/wp-content/uploads/2020/04/unnamed-2.png" width="170" height="210">

# Holberton-system_engineering-devops

## 0x09-web_infrastructure_design

At the end of this project you are expected to be able to explain, without the help of Google:
* You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
* You must be able to explain what each component is doing
* You must be able to explain system redundancy
* Know all the mentioned acronyms: LAMP, SPOF, QPS

## File Descriptions
Each file contains a link to an image hosted on Imgur. These images are based on the following requirements: <br />

## Task #0
### [0-simple_web_stack](0-simple_web_stack.md)
On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via `www.foobar.com.` Start your explanation by having a user wanting to access your website. <br />
You must use:
* 1 physical server
* 1 web server (Nginx)
* 1 application server
* 1 application files (your code base)
* 1 database (MySQL)
* 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`
---------------------------------------------------------------------------------------------------
## Task #1
### [1-distributed_web_infrastructure](1-distributed_web_infrastructure.md)
On a whiteboard, design a three servers web infrastructure that host the website `www.foobar.com`. <br />
You must add to [0-simple_web_stack](0-simple_web_stack.md):
* 2 physical servers
* 1 web server (Nginx)
* 1 application server
* 1 load-balancer (HAproxy)
* 1 application files (your code base)
* 1 database (MySQL)
----------------------------------------------------------------------------------------------------
## Task #2
### [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure.md)
On a whiteboard, design a three servers web infrastructure that host the website `www.foobar.com`, it must be secured, serve encrypted traffic and be monitored. <br />
You must add to [1-distributed_web_infrastructure](1-distributed_web_infrastructure.md):
* 3 firewalls
* 1 SSL certificate to serve `www.foobar.com` over HTTPS
* 3 monitoring clients (data collector for Sumologic or other monitoring services)
---------------------------------------------------------------------------------------------------
## Task #3
### [3-scale_up](3-scale_up.md)
You must add to [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure.md):
* 1 physical server
* 1 load-balancer (HAproxy) configured as cluster with the other one
* Split components (web server, application server, database) with their own server
---------------------------------------------------------------------------------------------------
# Authors
- [Linkedin: Matias López](https://uy.linkedin.com/in/matias-l%C3%B3pez-777796194?trk=people-guest_people_search-card)
- [Linkedin: Bruno Rodríguez](https://www.linkedin.com/in/brunonra/)
- [Linkedin: Eric Altez](https://www.linkedin.com/in/eric-altez-740427169/)
