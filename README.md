# TESTING



1. Nuclei Engine 
   - Nuclei Engine is used to perform (main/core) attacks to the web addresses ("http(s)://IP_Address:Port") where our specified 10 vulnerable web      application images are running)
   - Nuclei Engine has its own attack ".yaml" files, nuclei-templates. We used 10 specified of them as the "main/core" attacks for out data set.


2. Besides the  "Main/Core" attacks we defined Pre & Post Attacks to make more realistic attack scenarios.
   - In our attack scripts we named the Pre Attack phase  as "Discovery".
   - In "Discovery" phase, the  attacker behavior is trying to be implemented. For this phase, we tried to find the common commands (terminal) and tactics i.e. nmap,ping, curl .etc
    
         1. https://www.guru99.com/ethical-hacking-tutorials.html
             1.1 https://www.guru99.com/how-to-hack-web-server.html
         2. https://detectify.com/attack-vector
         3.https://www.rapid7.com/fundamentals/types-of-attacks/ (SQL & XSS)
         4.https://www.varonis.com/blog/cybersecurity-statistics
         5. https://infosecwriteups.com/content-discovery-tryhackme-3254015ccd11

            5.1. curl http://machine-ip -v (https://ivrsuresh.wordpress.com/2019/10/17/web-application-penetration-testing-with-curl/)



Performance Testing of the Data Set

 - Follow these: (https://www.linkedin.com/pulse/build-machine-learning-model-network-flow-tao-liu)
    - Data mining - to find out raw data those can help prediction, need domain experts
    - Features extraction - to pick up important features that relates to result accuracy
    - Clean data - to make raw data organized, structured for easy loading
    - Train data - to train data and validate data for best algorithm selection
    - Predict / Hypothesis - to predict or classify based on live data

