class QueryParamsHelper():

   def get_paged_params(request):
        page = request.args.get('page')
        per_page = request.args.get('perPage')
        order_by = request.args.get('orderBy')
        order_by_descending = request.args.get('orderByDescending')
        return page, per_page, order_by, order_by_descending



