# ansiblePlaybooks

Ansible playbooks for production and lab virtual machines.  All plays deploy a Ubuntu 18.04 template via vCenter and join an AD domain before roles are applied.

`deploy_wiki.yml`

* Dokuwiki

**Pending 18.04 Build**

`deploy_media.yml`

* TvHeadend DVR
* Emby

`deploy_reverse_proxy.yml`

* Apache Reverse Proxy
* Let's Encrypt SSL Certificate Generation with GoDaddy DNS Support
* Splunk Universal Forwarder
    * Forwarding Apache access and error logs

`deploy_syslog.yml`

* Syslog-NG Receiver
    * pfSense Logs
* Splunk Universal Forwarder
    * Forwarding pfSense logs

`deploy_home_assistant.yml`

* Home Assistant home automation software
* CIFS server to allow for remote editing of Home Assistant configuration files

`deploy_nextcloud.yml`

* Nextcloud
* MySQL
* Nginx
  
`deploy_splunk.yml`

* Splunk
* CIFS Server to allow for remote editing of Splunk configuration and application files

Pending Refactor

* services.yml