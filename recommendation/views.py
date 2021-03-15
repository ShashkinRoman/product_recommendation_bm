from django.shortcuts import render
from gensim.models import Word2Vec
from recommendation.models import MarketProducts
from recommendation.start_rec import count_popular_products
# from .forms import ReturnRecommendationForms
# Create your views here.

model = Word2Vec.load("word2vec.model")


def product_recommendation(request):
    return model.similar_by_word(request, 20)


def start_page(request, pk):
    try:
        product = MarketProducts.objects.get(productid=pk).productid
        if request.method == 'GET':
            similars = model.similar_by_word(str(product), 20)
            similars_products = []
            for i in similars:
                similars_products.append(i[0])
            popular_products = count_popular_products()
            return render(request, 'response_template.html', {'similars_products':  similars_products,
                                                              'popular_products': popular_products})
    except:
        return render(request, 'response_template.html',  {'recommendations': {}})
