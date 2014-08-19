from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import uuid
import datetime
from Crypto.Hash import MD5

@python_2_unicode_compatible
class ClipSignal(object):

    @staticmethod
    def pre_save(**kwargs):
        instance = kwargs.get('instance')

        # Create dataclip slug
        if not instance.slug:
            hash_key = "{}{}{}".format(
                instance.database.pk, 
                datetime.datetime.now(), 
                str(uuid.uuid1())
            )

            hash = MD5.new()
            hash.update(hash_key.encode('utf8'))

            instance.slug = hash.hexdigest()

        # Create a cache from exec query when sql_query changes
        if instance.original_sql_query != instance.sql_query:
            try:
                instance.dump_query()
            except Exception:
                pass
