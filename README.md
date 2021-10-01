# Gaggia backend

This python-service is a backend service to the espresso machine Gaggia Classic.
It is suppose to be able to

- track temperatures and save them
- have a PID to controll the temperature

Using a Raspberry Pi adn some temp probes

## how it works

This is actually a two parted service.
One service does the PID work and controlls the temperature and saves it to a Redis database.
The other service is a API to interact with the PID worker.
