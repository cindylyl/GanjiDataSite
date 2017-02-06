from django.shortcuts import render
from ganji.models import Info
from django.core.paginator import Paginator


# Create your views here.

def top3(d1, d2, area):
    pipeline = [
        {'$match': {'$and': [{'pub_date': {'$gte': d1, '$lte': d2}}, {'area': area}]}},
        {'$group': {'_id': '$cates', 'counts': {'$sum': 1}}},
        {'$sort': {'counts': -1}},
        {'$limit': 3}
    ]

    for i in Info._get_collection().aggregate(pipeline):
        data = {
            'name': i['_id'],
            'data': [i['counts']],
            'type': 'column'
        }
        yield data


series_hd = [i for i in top3('2015.12.25', '2015.12.27', '海淀')]
series_mtg = [i for i in top3('2015.12.25', '2015.12.27', '门头沟')]
series_bjzb = [i for i in top3('2015.12.25', '2015.12.27', '北京周边')]
series_xc = [i for i in top3('2015.12.25', '2015.12.27', '西城')]
series_dc = [i for i in top3('2015.12.25', '2015.12.27', '东城')]
series_cy = [i for i in top3('2015.12.25', '2015.12.27', '朝阳')]
series_cw = [i for i in top3('2015.12.25', '2015.12.27', '崇文')]
series_sjs = [i for i in top3('2015.12.25', '2015.12.27', '石景山')]
series_sy = [i for i in top3('2015.12.25', '2015.12.27', '顺义')]
series_xw = [i for i in top3('2015.12.25', '2015.12.27', '宣武')]
series_tz = [i for i in top3('2015.12.25', '2015.12.27', '通州')]
series_dx = [i for i in top3('2015.12.25', '2015.12.27', '大兴')]
series_yj = [i for i in top3('2015.12.25', '2015.12.27', '燕郊')]
series_my = [i for i in top3('2015.12.25', '2015.12.27', '密云')]
series_pg = [i for i in top3('2015.12.25', '2015.12.27', '平谷')]
series_hr = [i for i in top3('2015.12.25', '2015.12.27', '怀柔')]
series_yq = [i for i in top3('2015.12.25', '2015.12.27', '延庆')]
series_cp = [i for i in top3('2015.12.25', '2015.12.27', '昌平')]
series_ft = [i for i in top3('2015.12.25', '2015.12.27', '丰台')]
series_fs = [i for i in top3('2015.12.25', '2015.12.27', '房山')]
series_bm = [i for i in top3('2015.12.25', '2015.12.27', '不明')]


# print(series_hd)

def post_num():
    post_times = []
    cate_list = []
    for i in Info._get_collection().find():
        cate_list.append(i['cates'])
    cate_index = list(set(cate_list))
    for index in cate_index:
        post_times.append(cate_list.count(index))

    for cate, times in zip(cate_index, post_times):
        data = {
            'name': cate,
            'data': [times],
            'type': 'column'
        }
        yield data


series_num = [data for data in post_num()]


def post_percent1(d):
    pipeline = [
        {'$match': {'pub_date': d}},
        {'$group': {'_id': '$cates', 'count': {'$sum': 1}}},
        {'$sort': {'count': 1}}
    ]
    for i in Info._get_collection().aggregate(pipeline):
        yield [i['_id'], i['count']]


series_percent1 = [{
    'name': 'cate_percentage',
    'data': [i for i in post_percent1('2015.12.25')],
    'type': 'pie'
}]


def post_percent2(d):
    pipeline = [
        {'$match': {'pub_date': d}},
        {'$group': {'_id': '$area', 'count': {'$sum': 1}}},
        {'$sort': {'count': 1}}
    ]
    for i in Info._get_collection().aggregate(pipeline):
        yield [i['_id'], i['count']]


series_percent2 = [{
    'name': 'area_percentage',
    'data': [i for i in post_percent2('2015.12.25')],
    'type': 'pie'
}]


def doc(request):
    limit = 20
    arti_info = Info.objects
    paginator = Paginator(arti_info, limit)
    page = request.GET.get('page', 1)
    loaded = paginator.page(page)
    context = {
        'Info': loaded,
        'count': arti_info.count()
    }

    return render(request, 'doc.html', context)


def index(request):
    return render(request, 'main.html')


def chart(request):
    context = {
        'chart_bjzb': series_bjzb,
        'chart_hd': series_hd,
        'chart_dc': series_dc,
        'chart_xc': series_xc,
        'chart_mtg': series_mtg,
        'chart_cy': series_cy,
        'chart_cw': series_cw,
        'chart_sjs': series_sjs,
        'chart_sy': series_sy,
        'chart_xw': series_xw,
        'chart_tz': series_tz,
        'chart_dx': series_dx,
        'chart_yj': series_yj,
        'chart_my': series_my,
        'chart_pg': series_pg,
        'chart_hr': series_hr,
        'chart_yq': series_yq,
        'chart_cp': series_cp,
        'chart_ft': series_ft,
        'chart_fs': series_fs,
        'chart_bm': series_bm,
        'chart_num': series_num,
        'chart_percent1': series_percent1,
        'chart_percent2': series_percent2

    }

    return render(request, 'chart.html', context)
