# apcupsd-cgi-json
A simple cgi file that contains python to output a json of the APCUPSD status.

# Installation:

1. Install apache2 and apcupsd-cgi as usual:
    
    ```
    sudo apt update
    sudo apt upgrade
    sudo apt install apache2
    sudo a2enmod cgi
    sudo apt install apcupsd-cgi
    ```

2. Edit the file where the monitored devices are saved:
   
    `nano /etc/apcupsd/hosts.conf`

4. Edit the Apache configuration:
   
   `nano /etc/apache2/apache2.conf`

5. Find this section and change `denied` to `granted`:
    ```
    <Directory />
       Options FollowSymLinks
         AllowOverride None
         Require all denied
    </Directory>
    ```
    And add this to the end:

    `ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/`

6. Save and restart Apache:
   
     `sudo service apache2 restart`

7. Now access:
 
   `http://SERVER-IP/cgi-bin/apcupsd/multimon.cgi`

8. You'll see a screen similar to this. If you do, you configured `apcupsd-cgi` correctly:
   <img width="843" height="225" alt="image" src="https://github.com/user-attachments/assets/d68fc7aa-1ee0-42c6-8296-8beac8eb3ba1" />



   
