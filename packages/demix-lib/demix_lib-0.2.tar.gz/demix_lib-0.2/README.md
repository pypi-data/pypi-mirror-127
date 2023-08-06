# DEMIX library
Library that allow you to get stats arround DEMIX tiles and DEM
### Installation
```
pip install demix_lib
```

### Get started
how to log in in order to get stats

```Python
import demix_lib

# Instantiate a login object
login = "login"
password = "password"

# When needed, put the login and passord as arguments
lon = 13.196
lat = 14.268
result = demix_lib.download_tile_at_pos(login, password, lon, lat)
```