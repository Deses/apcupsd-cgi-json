# apcupsd-cgi-json
A simple cgi file that contains python to output a json of the [APCUPSD](https://sourceforge.net/projects/apcupsd/) status. I use it to monitor the UPS from [Uptime Kuma](https://uptimekuma.org/).

#### - Uptime Kuma config
<img width="394" height="556" alt="Uptime Kuma config" src="https://github.com/user-attachments/assets/7b818a54-c393-424f-8b46-ce2448b365e9" />

#### - Uptime Kuma properly retrieving the status from the json output
<img width="321" height="109" alt="Uptime Kuma properly retrieving the status from the json output" src="https://github.com/user-attachments/assets/61cd011a-890b-4075-82b9-285222a09c1e" />

# Note:
This works for an apcupsd that it's publishing it's status through IP:3551, and I'm using `127.0.0.1:3551` by default. If you need another IP or port, modify the cgi file to suit your needs. 25 is line you'd want to change.

# Installation:

1. Install apache2 and apcupsd-cgi as usual:
    
    ```
    sudo apt update
    sudo apt upgrade
    sudo apt install apache2
    sudo a2enmod cgi
    sudo apt install apcupsd-cgi
    ```

2. Edit the file where the monitored devices are saved. You might have one monitor already set on 127.0.0.1:
   
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

9. To install the `json.cgi`, create this file:
    ```
    cd /usr/lib/cgi-bin/apcupsd/
    nano json.cgi
    ```
    Paste the contents of [json.cgi](https://github.com/Deses/apcupsd-cgi-json/blob/main/json.cgi)
    Save, grant it permissions and proper ownership (you might not need this, I didn't), and restart apache2:
    ```
    chmod 0755 json.cgi
    chown root:www-data json.cgi
    systemctl restart apache2
    ```
10. Test:
    
    `curl -s http://127.0.0.1/cgi-bin/apcupsd/json.cgi`

    If you got an output like the following, you are done.
    ```
    {"APC": "001,032,0752", "DATE": "2025-11-24 00:33:18 +0100", "HOSTNAME": "proxmox", "VERSION": "3.14.14 (31 May 2016) debian", "UPSNAME": "CP1600E", "CABLE": "USB Cable", "DRIVER": "USB UPS Driver", "UPSMODE": "Stand Alone", "STARTTIME": "2025-11-23 01:47:38 +0100", "MODEL": "CP1600EPFCLCD", "STATUS": "ONLINE", "LINEV": "239.0 Volts", "LOADPCT": "7.0 Percent", "BCHARGE": "100.0 Percent", "TIMELEFT": "87.1 Minutes", "MBATTCHG": "5 Percent", "MINTIMEL": "10 Minutes", "MAXTIME": "0 Seconds", "OUTPUTV": "239.0 Volts", "DWAKE": "-1 Seconds", "LOTRANS": "195.0 Volts", "HITRANS": "257.0 Volts", "ALARMDEL": "No alarm", "NUMXFERS": "0", "TONBATT": "0 Seconds", "CUMONBATT": "0 Seconds", "XOFFBATT": "N/A", "SELFTEST": "NO", "STATFLAG": "0x05000008", "SERIALNO": "BHYPY2000282", "NOMINV": "230 Volts", "NOMPOWER": "1000 Watts", "END APC": "2025-11-24 00:33:19 +0100"}
    ```
    

   
