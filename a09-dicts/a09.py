## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR get_types_count() FUNCTION GOES HERE ###
def get_types_count(dict):
    new_dict = {}
    for key in dict:
        new_dict[key] = len(dict[key])
    return new_dict
#### End OF MARKER


### YOUR CODE FOR get_types() FUNCTION GOES HERE ###
def get_types(dict):
    doc_types = list(dict.keys())
    return doc_types
#### End OF MARKER


### YOUR CODE FOR get_author_count() FUNCTION GOES HERE ###
def get_author_count(dict, name, doc = None):
    count = 0
    if not doc is None:
        for keys in doc:
            for key in dict[keys]:
                if "author" in key and "username" in key["author"] and key["author"]["username"] == name:
                    count += 1
        return count
    else:
        for keys in dict:
            for key in dict[keys]:
                if "author" in key and "username" in key["author"] and key["author"]["username"] == name:
                    count += 1
        return count
#### End OF MARKER



if __name__ == '__main__':
    d = {
            "articles": [{
                "slug": "how-to-train-your-mule",
                "title": "How to train your mule",
                "description": "Ever wonder how?",
                "body": "It takes a Jacobian",
                "tagList": ["mules", "training"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 0,
                "author": {
                  "username": "jake",
                  "bio": "I work at statefarm",
                  "following": False
                }
            }, {
                "slug": "and another article",
                "body": "I'm getting bored",
                "tagList": ["bored", "article"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 20,
                "author": {
                  "username": "cap",
                  "following": True
                }
            }],
            "tweets": [{
                "body": "See my article on training mules.",
                "author": {
                  "username": "jake"
                }
            }]
        }

    print(get_types(d))
    print(get_types_count(d))
    print(get_author_count(d, 'jake'))
    print(get_author_count(d, 'cap', ['articles', 'tweets']))
