from recommendation.models import MarketOrders, MarketOrdersProducts
from gensim.models import Word2Vec
from django.db.models import Count
from datetime import datetime, timedelta


def start_synchronization_model():
    """Synchronization Word2Vec model. Takes from the MarketOrders all product id, build model and save to file"""
    try:
        all_product_in_orders = []
        for order in MarketOrders.objects.all()[0:1000]:
            product_id = []
            for i in order.rn_product_in_orders.all():
                product_id.append(str(i.productid.productid))
            all_product_in_orders.append(product_id)
        model = Word2Vec(all_product_in_orders, min_count=1, size=50, workers=3, window=3, sg=1)
        model.save("word2vec.model")
    except Exception as e:
        return e


def count_popular_products():
    """Calculate popular products for last six month and write in txt"""
    datetime_half_year = datetime.today() - timedelta(days=180)
    products_recommendation = MarketOrdersProducts.\
        objects.exclude(productid=10789).filter(created_at__gte=datetime_half_year).\
        order_by('productid').values_list('productid', flat=True).\
        annotate(Count('productid')).order_by('-productid__count')[0:20]
    return list(products_recommendation)
