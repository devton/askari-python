import uuid
from Crypto.Hash import MD5


class ClipSignal(object):
    @staticmethod
    def pre_save(**kwargs):
        instance = kwargs.get('instance')

        if not instance.slug:
            hash_key = "{}{}{}".format(
                instance.database.pk, 
                instance.database.user.pk, 
                str(uuid.uuid1())
            )

            hash = MD5.new()
            hash.update(hash_key)

            instance.slug = hash.hexdigest()
