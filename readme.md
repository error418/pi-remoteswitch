# FMSend

You will need `wiringPi` and `rcswitch-pi` as dependencies for this project 

## Cron Configuration

Add following entries to the `crontab` configuration

    @reboot python /opt/skyswitch/emitterserver.py &

if you want to automatically switch off some recievers you can also use `cron`

    # Switch kitchen counter light off
    0 3 * * * fmsend F00000000FF0