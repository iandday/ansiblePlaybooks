# ansiblePlaybooks

Ansible playbooks for production and lab virtual machines.  All plays deploy a Ubuntu 16.04 template via vCenter and join an AD domain before roles are applied.

``deploy_media.yml``

    * TvHeadend DVR
    * Emby 

``deploy_reverse_proxy.yml``

    * Apache Reverse Proxy
    * Let's Encrypt SSL Certificate Generation with GoDaddy DNS Support
    * Splunk Universal Forwarder

``deploy_syslog.yml``

    * Syslog-NG Receiver
        * pfSense Logs
    * Splunk Universal Forwarder

Pending Refactor

  * hass.yml
  * nextclould.yml
  * services.yml
  * splunk.yml