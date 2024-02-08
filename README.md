# DTSPModule2
Coding Data dashboard for my submission for Module 2 data project
During this project i came across many problems and error codes
Because of this i had many stages that contributed towards my project.
I started off by creating a part of code that opened up an HTML tab. 
This took a bit of time as i had to figure out how to get past the firewalls and permissions that were on my laptop, as its a work laptop.
To solve this i created a VM and a container and ran the code inside this so it ran without getting in the way of my permissions that are on my work laptop.
From there i wanted to integrate a 3rd party API into my code and to do this i needed to change my APP.py file on the code to include a link with my API-URL and my personal API-key which would allow me to access the API itself and retrieve the data from it onto my HTML link.
Once i had my these two aspects opening a dashboard which fetched data from my 3rd party API, i wanted to change the style of the dashboard to make it more aesthetic and user-friendly.
This involved making a new css file in the code called 'style.css', this allowed me to write some more lines of code that changed the position and style of the dashboard, making it how i wanted it to look.
After all of these were done I had a lot of problems involving my API messing about and not retrieving data, error codes in the code and error codes in the dashboard that i was not familiar with. 
I had to ask multiple people in my company and do a lot of research to try and figure out what was causing these problems. I couldnt really find anything that showed me how to do it exactly, so i had to go through all the code debugging each line using breakpoints and try to figure out where the code was breaking down. 
When i did this i found out the code was breaking code at the point where the data was trying to be fetched by the code from the API. 
To solve this i used print commands to find the exact line that was the problem, then once i found that i rewrote that section breaking it down into the data it retrieved and using this to print just the numbers and values that i wanted, including finding the long list number that i found out related to a time stamp. 
Once i had all this information i could run the code, get my dahsboard link, click the link and enter my city to get the temperature at that time. Then go back to my code and look in the terminal to find all the time stamps listed from my print commands and see the values for not only the temperature, but also the humidity and the temperature it feels like.
