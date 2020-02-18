# ansiblePlaybooks

Ansible playbooks for production and lab virtual machines.  All plays deploy a Ubuntu 18.04 template via vCenter and join an AD domain before roles are applied.


## Plays
### deploy_docker.yml
Clone Ubuntu 18.04 LTS KVM template and install Docker and Docker-Compose to run the following services
* Portainer
* Traefik
* Heimdall
* Unifi Controller
* Duo Auth Proxy
* Watchtower
* Emby
* Home Assistant
* Mosquito
* AppDaemon
* [Docker idrac6](https://github.com/DomiStyle/docker-idrac6)
  
### deploy_nextcloud.yml
Clone Ubuntu 18.04 LXC template and install Nextcloud, MariaDB, and Nginx

### deploy_wiki.yml
Clone Ubuntu 18.04 LXC template and install Dokuwiki and Nginx

### restore_wiki.yml
Restore wiki content and settings from backup


## TODO
* Dokuwiki
* Splunk
* Syslog Receiver
* Guacamole
* Gitlab

