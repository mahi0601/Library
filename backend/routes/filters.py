def create_filter(title=None, author=None, language=None, topic=None, mime_type=None):
    query = {}

    if title:
        query["title"] = {"$regex": title, "$options": "i"}
    if author:
        query["authors"] = {"$regex": author, "$options": "i"}
    if language:
        query["languages"] = {"$in": language}
    if topic:
        query["$or"] = [
            {"subjects": {"$regex": topic, "$options": "i"}},
            {"bookshelves": {"$regex": topic, "$options": "i"}}
        ]
    if mime_type:
        query["formats.mime_type"] = mime_type

    return query
