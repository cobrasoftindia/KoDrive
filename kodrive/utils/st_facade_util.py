
# Delete all devices that no longer have
# a folder as a dependency
def prune_devices(folder, config):
  pruned = False

  # For each device in the folder
  for d in folder['devices']:
    exists = False
    
    # Check if that device id exists in other folders
    for f in config['folders']:
      if device_exists(d['deviceID'], f):
        exists = True
        break
    
    # If no instance can be found, delete the device
    if not exists:
      pruned = True
      delete_device(d['deviceID'], config)

  return pruned

def find_folder_with_path(path, config):
  return find_folder({
    'path' : path
  }, config)

def find_folder(object, config):
  
  # list of folders
  folders = config['folders']
  
  for f in folders:
    n = 0
    d = 0

    for k in object:

      if k == 'path':
        if object[k].rstrip('/') == f[k].rstrip('/'):
          n += 1
      else: 
        if object[k] == f[k]:
          n += 1

      d += 1

    if n == d:
      return f

###
# 
# Checks whether device exists in config['devices']
#
def device_exists(client_devid, config):
  return find_device(client_devid, config) != None

def delete_device(devid, config):
  devices = config['devices']

  for i, d in enumerate(devices):
    device_id = get_devid(d)
    
    if device_id == devid:
      del devices[i]
      return True

  return False

###
#
# Return the device object in config['devices']
#
def find_device(client_devid, config=None):
    
  for d in config['devices']:
    device_id = get_devid(d)
    if device_id == client_devid:
      return d

def get_devid(dev_obj):
  if 'deviceID' in dev_obj:
    return dev_obj['deviceID']
  else:
    return dev_obj['deviceId']

