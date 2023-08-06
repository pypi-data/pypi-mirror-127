# pandora-upload

pandora_upload is a commandline client for pan.do/ra.
You can use it to upload one or more files to your pandora instance.
No conversion is done on the client side.
To upload/sync large repositories use pandora_client

You can also use pandora-upload as a python script:

``` python
import pandora_client
item_id = pandora_client.upload(
    'http://pandora/api/',
    ['/home/example/Videos/video.mp4',
    {
        'title': 'This is an example',
        'date': '2021-11-15'
    }
)
```
