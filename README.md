# Pi-FanHAT--Raspberry-waveshare-HAT
a really wonderful HAT needs a wonderful python script to enjoy its full potential. With useful informations on a readable display.

# Why?
As it happens sometimes, I did not find what I wanted on the internet for this very nice HAT module from Waveshare.
I tried the main.py script I found on waveshare website...
What we can read in it is a - if elif elif .... - written on the wrong  inverted order that keeps the Fan at 40% what ever happens:

```
if(temp > 30):
  pwm.setServoPulse(0,20)
elif(temp > 40):
  pwm.setServoPulse(0,40)
elif(temp > 50):
  pwm.setServoPulse(0,50)
elif(temp > 55):
  pwm.setServoPulse(0,75)
elif(temp > 60):
  pwm.setServoPulse(0,90)
elif(temp > 65):
  pwm.setServoPulse(0,100)
else:
  pwm.setServoPulse(0,10)
```

   As the first condition if(temp > 30) should be always True on a Raspberry-pi system, it stops there. Typical mistake easy to fall in.
   So, I wrote something that suits perfectly to my needs:
   - a first 100% speed fan test for 2 seconds
   - corresponding fan speed with CPU temperature
   - display on 1 single line, as this display is too small (for me) for showing 2 lines at the same time (as in scripts on waveshare's)
   - informations displayed:
     - display CPU temp
     - RAM usage
     - DISK usage
     - CPU usage
     - IP
     - LOCALHOST name
     - CLOCK
     - FAN power in percent
     - FAN power with a horizontal bar
     - OS distribution
     - some non useful words as usual on a wonderful display like this oled tiny thing
