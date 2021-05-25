class QueryParamsHelper():

    def get_paged_params(request):
        page = request.args.get('page')
        per_page = request.args.get('perPage')
        order_by = request.args.get('orderBy')
        order_by_descending = request.args.get('orderByDescending') != None
        return page, per_page, order_by, order_by_descending

    def get_param(request, param_name):
        param = request.args.get(param_name)
        if param == 'undefined':
            return None
        return param



