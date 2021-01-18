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
* Home Assistant
* Mosquito
* AppDaemon
  
### deploy_nextcloud.yml
Clone Ubuntu 20.04 LXC template and install Nextcloud, MariaDB, and Nginx
TODO: 
- configure database backup
- bump version to current

### deploy_jellyfin.yml
Clone Ubuntu 20.04 LXC template and install Jellyfin
TODO: configure database backup



### deploy_wiki.yml
Clone Ubuntu 18.04 LTS LXC template and install Dokuwiki and Nginx



### restore_wiki.yml
Restore wiki content and settings from backup


## TODO
* Splunk
* Syslog Receiver
* Guacamole
* Gitlab
* Backup rotation

