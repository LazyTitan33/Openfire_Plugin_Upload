# Openfire plugin upload

Should you find yourself in an engagement with access to the Openfire Admin console, you could upload a malicious plugin (.jar file) to get RCE.

I was in such a situation and because of a shaky connection to their network, I wanted to make my life easier.

The script below doesn't have any error handling because I'm lazy. If you have issues, modify the script to go through your proxy, ensure you are hitting the correct IP, on the correct port, correct user etc. My script assumes port 9090 and default admin user. 

![image](https://user-images.githubusercontent.com/80063008/215105203-df8ca880-8261-492b-8602-cbcc07d75ec4.png)

I'll leave creating the malicious .jar plugin to your imagination and exercise.

NOTE: On the plus side, Openfire, by default, runs as NT Authority/System:

![image](https://user-images.githubusercontent.com/80063008/215106024-26a3eedb-eb5c-4919-8fe8-7a0f39aa4303.png)
