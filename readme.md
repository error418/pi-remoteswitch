# FMSend

You will need `wiringPi` and `rcswitch-pi` as dependencies for this project.

## Python Dependencies

This project depends on [flask](http://flask.pocoo.org/ "Flask"), which you can retrieve via `pip`

## rcswitch-pi

You will need a forked implementation of rcswitch-pi. You can retrieve it [here](https://github.com/Error418/rcswitch-pi).

The `send.cpp` is modified in this fork to directly accept tri-state codes as a program argument.

## Cron Configuration

Add following entries to the `crontab` configuration

    @reboot python /opt/skyswitch/emitterserver.py &

if you want to automatically switch off some recievers you can also use `cron`

    # Switch kitchen counter light off
    0 3 * * * fmsend F00000000FF0