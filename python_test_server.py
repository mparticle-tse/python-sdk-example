import mparticle
batch = mparticle.Batch()
batch.environment = 'development'

#config
configuration = mparticle.Configuration()
configuration.api_key = 'API KEY'
configuration.api_secret = 'SECRET'
configuration.debug = True #enable logging of HTTP traffic
api_instance = mparticle.EventsApi(configuration)

# Identity
identities = mparticle.UserIdentities()
identities.customerid = '123456'
identities.email = 'user@example.com'
batch.user_identities = identities

#deviceinfo
device_info = mparticle.DeviceInformation()
# set any IDs that you have for this user
device_info.ios_advertising_id = '07d2ebaa-e956-407e-a1e6-f05f871bf4e2'
device_info.android_advertising_id = 'a26f9736-c262-47ea-988b-0b0504cee874'
batch.device_info = device_info

# custom event
app_event = mparticle.AppEvent('Example', 'navigation')


#commerce event
product = mparticle.Product()
product.name = 'Example Product'
product.id = 'sample-sku'
product.price = 19.99

product_action = mparticle.ProductAction('purchase')
product_action.products = [product]
product_action.tax_amount = 1.50
product_action.total_amount = 21.49

commerce_event = mparticle.CommerceEvent(product_action)
# commerce_event.timestamp_unixtime_ms = example_timestamp


#sessions
session_start = mparticle.SessionStartEvent()
session_start.session_id = 12345678
# session_start.timestamp_unixtime_ms = example_timestamp

session_end = mparticle.SessionEndEvent()
session_end.session_id = session_start.session_id # its mandatory that these match
# session_end.session_duration_ms = example_duration
# session_end.timestamp_unixtime_ms = example_timestamp + example_duration

batch.events = [app_event, commerce_event, session_start, session_end]

print("im the batch events", batch.events)


try: 
    api_instance.upload_events(batch)
    # you can also send multiple batches at a time to decrease the amount of network calls
    #api_instance.bulk_upload_events([batch, batch])
except mparticle.rest.ApiException as e:
    print ("Exception while calling mParticle: %s\n" % e)
