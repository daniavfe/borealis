class PFOCollectionDto():
    def __init__(self, page, page_count, per_page, order_by, order_by_descending, items):
        self.page = page
        self.page_count = page_count
        self.per_page = per_page
        self.order_by = order_by
        self.order_by_descending = order_by_descending
        self.items = items
