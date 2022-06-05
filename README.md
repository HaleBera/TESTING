# TESTING



1. Nuclei Engine 
   - Nuclei Engine is used to perform (main/core) attacks to the web addresses ("http(s)://IP_Address:Port") where our specified 10 vulnerable web      application images are running)
   - Nuclei Engine has its own attack ".yaml" files, nuclei-templates. We used 10 specified of them as the "main/core" attacks for out data set.


2. Besides the  "Main/Core" attacks we defined Pre & Post Attacks to make more realistic attack scenarios.
   - In our attack scripts we named the Pre Attack phase  as "Discovery".
   - In "Discovery" phase, the  attacker behavior is trying to be implemented. For this phase, we tried to find the common commands (terminal) and tactics i.e. nmap,ping, curl .etc
         - https://infosecwriteups.com/content-discovery-tryhackme-3254015ccd11
         - https://ivrsuresh.wordpress.com/2019/10/17/web-application-penetration-testing-with-curl/
   
