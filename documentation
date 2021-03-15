For create new model Word2Vec for synchronization, inside worker directory write:
"venv/bin/python manage.py start_sync" (5-6 hours) by default model already create
This command takes from the MarketOrders all product id for last half year, build model and save to file word2vec.model


To take list with recommendation and popular products one can by url /start/<productid>

In models was be modificated next:
MarketProductOrders - add related_name in field orderid 'rn_product_in_orders', for fast search all products in order
MarketProducts - add related_name in field marketgroupid 'rn_group_id' for fast search categoryID and add find product substitutes
Reviews - for fix errors add related_name in next columns: addressid, clientid, masterid
In someone tables was be column 'id' with property 'null=True' - deleted

