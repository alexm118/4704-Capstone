from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class Pager(object):
    def __init__(self, *args, **kwargs):
        super(Pager, self).__init__()
        self.data_set = []
        self.page_size = 10
        self.paged_items = None

    def get_paged_items(self, page=1):
        paginator = Paginator(self.data_set, self.page_size)

        try:
            self.paged_items = paginator.page(page)
        except PageNotAnInteger:
            self.paged_items = paginator.page(1)
        except EmptyPage:
            self.paged_items = paginator.page(paginator.num_pages)

    @property
    def count(self):
        if self.paged_items:
            return self.paged_items.paginator.count
        else:
            return 0

    @property
    def current_page(self):
        if self.paged_items:
            return self.paged_items.number
        else:
            return 0

    @property
    def num_pages(self):
        if self.paged_items.paginator:
            return self.paged_items.paginator.num_pages
        else:
            return 0

    @property
    def previous_page(self):
        if self.paged_items:
            return self.paged_items.previous_page_number
        else:
            return 0

    @property
    def next_page(self):
        if self.paged_items:
            return self.paged_items.next_page_number
        else:
            return 0

    @property
    def start_index(self):
        if self.paged_items:
            return self.paged_items.start_index
        else:
            return 0

    @property
    def end_index(self):
        if self.paged_items:
            return self.paged_items.end_index
        else:
            return 0

    @property
    def pager_start(self):
        if self.paged_items:
            start = self.current_page - 2
            if start > 1 and start > self.num_pages - 6:
                if self.num_pages - 6 < 1:
                    return 1
                else:
                    return self.num_pages - 6
            elif start > 1:
                return start
            else:
                return 1
        else:
            return 0

    @property
    def pager_end(self):
        if self.paged_items:
            end = self.current_page + 2
            if self.num_pages <= 7:
                return self.num_pages
            elif end < self.num_pages and end < 7:
                return 7
            elif end < self.num_pages:
                return end
            else:
                return self.num_pages
        else:
            return 0

    @property
    def pager_range(self):
        return range(self.pager_start, self.pager_end + 1)

    @property
    def has_next(self):
        return self.paged_items and self.paged_items.has_next()

    @property
    def has_previous(self):
        return self.paged_items and self.paged_items.has_previous()