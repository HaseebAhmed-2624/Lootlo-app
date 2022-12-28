# def swap(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     print("a's value is", a)
#     print("b's value is", b)
#
#
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     swap(a, b)

#
# def get_domain(url):
#
#     scheme_index = url.find("://")
#     if scheme_index != -1:
#         url = url[scheme_index + 3:]
#         scheme_index = url.find("www.")
#         if scheme_index != -1:
#             url = url[scheme_index + 4:]
#     else:
#
#         url = url[url.find(":") + 1:]
#
#     path_index = url.find(".com")
#     if path_index != -1:
#         url = url[:path_index]
#     return url
#
#
# if __name__ == '__main__':
#     url = str(input())
#     print(get_domain(url))

# def MSF(n=0, l=50):
#     for i in range(n, l + 1):
#         if i % 5 == 0:
#             print("is our")
#
#         elif i % 3 == 0:
#             print("Food")
#
#         elif i % 4 == 0:
#             print("common")
#         elif i % 8 == 0:
#             print("gound")
#         else:
#             print("Food is our common ground.")
#
#
# if __name__ == '__main__':
#     n = int(input())
#     l = int(input())
#
#     MSF(n, l)
#
# def generate_hashtag(sentence):
#     if not sentence:
#         return False
#
#     # Split the string into words and capitalize each word
#     words = [word.capitalize() for word in sentence.split()]
#
#     # Join the words with a hashtag and check the length
#     tag = "#" + "".join(words)
#     if len(tag) > 140:
#         return False
#     else:
#         return tag
#
# if __name__ == '__main__':
#     sentence=str(input())
#     print(generate_hashtag(sentence))
#
# {
#     "username":
#         "Tge"
#     ,
#     "password":
#         "This field is required."
#     ,
#     "password2":
#         "This field is required."
#     ,
#     "email":
#         "r@e.com"
#     ,
#     "first_name":
#         "This field is required."
#     ,
#     "last_name":
#         "This field is required."
#     ,
#     "address":
#         "This field is required."
#     ,
#     "city":
#         "This field is required."
#     ,
#     "postal_code":
#         1
#
# }