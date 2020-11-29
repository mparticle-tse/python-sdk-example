import mparticle
batch = mparticle.Batch()
batch.environment = 'development'

#config
configuration = mparticle.Configuration()
configuration.api_key = 'us1-4e27eceae24a0c4a85f014ec98de88b0'
configuration.api_secret = 'ER3fm1YjEPg55IZueBgZj5-i5qjuygEw1lI-z_KiLMEu2HlINKdxMbI4X6GsZ772'
configuration.debug = True #enable logging of HTTP traffic
api_instance = mparticle.EventsApi(configuration)

# Identity
identities = mparticle.UserIdentities()
identities.customerid = '123456'
identities.email = 'user@example.com'
batch.user_identities = identities

# custom event
app_event = mparticle.AppEvent('Example', 'navigation')
batch.events = [app_event]

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

batch.events = [commerce_event]

#sessions
session_start = mparticle.SessionStartEvent()
session_start.session_id = 12345678
# session_start.timestamp_unixtime_ms = example_timestamp

session_end = mparticle.SessionEndEvent()
session_end.session_id = session_start.session_id # its mandatory that these match
# session_end.session_duration_ms = example_duration
# session_end.timestamp_unixtime_ms = example_timestamp + example_duration

batch.events = [session_start, session_end]


try: 
    api_instance.upload_events(batch)
    # you can also send multiple batches at a time to decrease the amount of network calls
    #api_instance.bulk_upload_events([batch, batch])
except mparticle.rest.ApiException as e:
    print ("Exception while calling mParticle: %s\n" % e)
