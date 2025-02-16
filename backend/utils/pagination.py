def paginate(queryset, page: int, page_size: int):
    skip = (page - 1) * page_size
    return queryset.skip(skip).limit(page_size)
