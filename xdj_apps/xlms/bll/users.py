def get_user_profile_img_url(user):
    from django.contrib.auth.models import User
    from django.conf import settings
    if not isinstance(user,User):
        raise Exception("user muste be {0}".format(User))
    from openedx.core.djangoapps.user_api.accounts.image_helpers import get_profile_image_urls_for_user
    ret = get_profile_image_urls_for_user(user)
    if ret["small"].find("/static/studio/images/")>-1:
        #/static/studio/images/profiles/default_50.png static/images/profiles/default_50.png
        ret["small"] = ret["small"].replace("/static/studio/images/profiles/","/static/images/profiles/")
        ret["large"] = ret["large"].replace("/static/studio/images/profiles/","/static/images/profiles/")
        ret["medium"] = ret["medium"].replace("/static/studio/images/profiles/","/static/images/profiles/")

        ret["small"] = settings.LMS_ROOT_URL + ret["small"]
        ret["large"] = settings.LMS_ROOT_URL + ret["large"]
        ret["medium"] = settings.LMS_ROOT_URL + ret["medium"]

    # ret["small"] = ret["small"].replace("static/studio/images/profiles/","media/profile-images/")
    # ret["large"] = ret["large"].replace("static/studio/images/profiles/","media/profile-images/")
    # ret["medium"] = ret["medium"].replace("static/studio/images/profiles/","media/profile-images/")

    return ret