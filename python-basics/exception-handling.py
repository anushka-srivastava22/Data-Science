try:
    z=12/0
except Exception as e:
    print('Exception occured', e)
    z=None

print('Division is',z)